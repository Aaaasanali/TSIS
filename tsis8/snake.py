import pygame, time
import random
pygame.init()

screen_width = 1000
screen_height = 1000

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

#game vars
cell_size = 50
direction = 1
score = 0
food = False
dis_food = False
timer = 0
scale = 0

#snake list
snake_pos = [[int(screen_width/2), int(screen_width/2)]]
snake_pos.append([int(screen_width/2), int(screen_width/2)+cell_size])
snake_pos.append([int(screen_width/2), int(screen_width/2)+cell_size*2])
snake_pos.append([int(screen_width/2), int(screen_width/2)+cell_size*3])

fnt = pygame.font.Font('Roboto-Regular.ttf', 40)

#colors
bg = (148, 217, 108)
body_inner = (50,175,25)
body_outer = (100, 100, 100)
red = (232, 72, 99)
food_colors = [(138, 19, 39), (138, 75, 19), (86, 19, 138)]

def draw_screen():
  screen.fill(bg)

def draw_food(food_ind):
  if food_ind == 0:
    food_score = 1
    color = food_colors[0]
  if food_ind == 1:
    food_score = 3
    color = food_colors[1]
  if food_ind == 2:
    food_score = 5
    color = food_colors[2]
  pygame.draw.rect(screen, color, (food_x, food_y, cell_size, cell_size))
  return food_score

def draw_dis_food(scale):
  pygame.draw.rect(screen, (196, 162, 159), (dis_food_x, dis_food_y, cell_size-scale, cell_size-scale))

def add_piece():
  new_piece = list(snake_pos[-1])
  if direction == 1:
    new_piece[1] += cell_size
  if direction == 3:
    new_piece[1] -= cell_size
  if direction == 2:
    new_piece[0] -= cell_size
  if direction == 4:
    new_piece[0] += cell_size
  snake_pos.append(new_piece)


#game loop
run = True
while run:
  draw_screen()
  #ordinary food spawner
  if not food:
    food_x = random.randrange(0, screen_width, cell_size)
    food_y = random.randrange(0, screen_width, cell_size)
    food_ind = random.randint(0, 2)
    food = True
  else:
    food_score = draw_food(food_ind)
  #food collision detection
  if snake_pos[0] == [food_x, food_y]:
    draw_screen()
    score += food_score
    food = False
    for i in (0, food_score):  
      add_piece()
  #dissapearing food spawner
  if not dis_food:
    dis_food_x = random.randrange(0, 600, cell_size)
    dis_food_y = random.randrange(0, 600, cell_size)
    dis_food = True
  else:
    draw_dis_food(scale)
  #dissapearing food collision detection
  if snake_pos[0] == [dis_food_x, dis_food_y]:
    draw_screen()
    score += 1
    timer = 0
    scale = 0
    dis_food = False
    add_piece()
  #dissapearing food timer
  if timer < 100:
    scale+=1
    if cell_size-scale == 0:
      timer = 0
      scale = 0
      dis_food = False
  #screen collision detection
  if snake_pos[0][0] >= screen_width or snake_pos[0][0] < 0 or snake_pos[0][1] >= screen_height or snake_pos[0][1] < 0:
    screen.fill('red')
    run = False
  #snake's body collision detection
  for coord in snake_pos[1:]:
    if coord == snake_pos[0]:
      screen.fill('red')
      run = False
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    #key checking
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and direction != 3:
        direction = 1
        continue
      if event.key == pygame.K_RIGHT and direction != 4:
        direction = 2
        continue
      if event.key == pygame.K_DOWN and direction != 1:
        direction = 3
        continue
      if event.key == pygame.K_LEFT and direction != 2:
        direction = 4
        continue
  #snake movement based on direction
  snake_pos = snake_pos[-1:] + snake_pos[:-1]
  if direction == 1:
    snake_pos[0][0] = snake_pos[1][0]
    snake_pos[0][1] = snake_pos[1][1]-cell_size
  if direction == 3:
    snake_pos[0][0] = snake_pos[1][0]
    snake_pos[0][1] = snake_pos[1][1]+cell_size
  if direction == 2:
    snake_pos[0][0] = snake_pos[1][0]+cell_size
    snake_pos[0][1] = snake_pos[1][1]
  if direction == 4:
    snake_pos[0][0] = snake_pos[1][0]-cell_size
    snake_pos[0][1] = snake_pos[1][1]
  #snake draw
  head = 1
  for x in snake_pos:
    if head == 0:
      pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
      pygame.draw.rect(screen, body_inner, (x[0]+1, x[1]+1, cell_size-2, cell_size-2))
    if head == 1:
      pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
      pygame.draw.rect(screen, red, (x[0]+1, x[1]+1, cell_size-2, cell_size-2))
      head = 0
  #ticks
  timer += 1
  clock.tick(10)
  #score blit
  score_text = fnt.render(str(score), 1, 'black')
  screen.blit(score_text, (20,0))
  #display update
  pygame.display.update()
time.sleep(2)
pygame.quit()
