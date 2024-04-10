import pygame, time
import random
pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
color = 'black'
detect = False
brush_size = 10
mode = 1
x = 0
y = 0
x0 = 0
y0 = 0


screen.fill('white')
#game loop
run = True
while run:
  #mouse keys checker
  left = pygame.mouse.get_pressed()[0]
  mouse = pygame.mouse.get_pos()

  #interface colors and placing
  tab = pygame.draw.rect(screen, 'grey', (0, 0, screen_width, 100))
  red = pygame.draw.rect(screen, 'red', (50, 0, 50, 50))
  black = pygame.draw.rect(screen, 'black', (0, 0, 50, 50))
  green = pygame.draw.rect(screen, 'green', (100, 0, 50, 50))
  yellow = pygame.draw.rect(screen, 'yellow', (150, 0, 50, 50))

  brush = pygame.draw.circle(screen, 'black', (300, 35), 25)

  rect_out = pygame.draw.rect(screen, 'black', (450, 5, 55, 55))
  rect_in = pygame.draw.rect(screen, 'grey', (455, 10, 45, 45))

  eraser_top = pygame.draw.rect(screen, 'cyan', (900, 10, 30, 15))
  eraser_bot = pygame.draw.rect(screen, (237, 247, 255), (900, 25, 30, 55))

  right_tr = pygame.draw.polygon(screen, 'black', ((520, 5), (520, 60), (570, 60)))

  eq_tr = pygame.draw.polygon(screen, 'black', ((620, 5), (580, 60), (660, 60)))

  rhombus = pygame.draw.polygon(screen, 'black', ((700, 5), (670, 35), (700, 65), (730, 35)))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    #mousewheel checker
    elif event.type == pygame.MOUSEWHEEL and mode == 1:
      if event.y == 1:
        brush_size += 3
      elif event.y == -1:
        brush_size -= 3

  #checking mouse clicking on colors
  if left and red.collidepoint(mouse):
    color = 'red'
  if left and black.collidepoint(mouse):
    color = 'black'
  if left and green.collidepoint(mouse):
    color = 'green'
  if left and yellow.collidepoint(mouse):
    color = 'yellow'
  #checking mouse clicking on tools
  if left and brush.collidepoint(mouse):
    mode = 1
  if left and (rect_in.collidepoint(mouse) or rect_out.collidepoint(mouse)):
    mode = 2
  if left and right_tr.collidepoint(mouse):
    mode = 3
  if left and eq_tr.collidepoint(mouse):
    mode = 4
  if left and rhombus.collidepoint(mouse):
    mode = 5
  if left and (eraser_bot.collidepoint(mouse) or eraser_top.collidepoint(mouse)):
    color = 'white'

  #brush and circle mode
  if left and mode == 1 and mouse[1] > 100:
    pygame.draw.circle(screen, color, mouse, brush_size)
  #rectangle mode
  if left and mode == 2 and mouse[1] > 100:
    if not detect:
      x, y = mouse
      x0 = mouse[0]
      y0 = mouse[1]
      detect = True
    elif x <= mouse[0] and y <= mouse[1]:
      pygame.draw.rect(screen, color, (x, y0, 5, 5))
      pygame.draw.rect(screen, color, (x0, y, 5, 5))
      x += 5
      y += 5
    elif x >= mouse[0] and y >= mouse[1] and x > x0 and y > y0:
      pygame.draw.rect(screen, 'white', (x, y0, 5, 5))
      pygame.draw.rect(screen, 'white', (x0, y, 5, 5))
      x -= 5
      y -= 5
  if not left and mode == 2:
    if detect:
      for i in range(x0, x, 5):
        pygame.draw.rect(screen, color, (x, y0, 5, 5))
        pygame.draw.rect(screen, color, (x0, y, 5, 5))
        x0 += 5
        y0 += 5
        print('draw')
    pygame.draw.rect(screen, color, (x0, y, 5, 5))
    detect = False
  #right triangle mode
  if left and mode == 3: 
    if not detect:
      x0,y0 = mouse
      x, y = mouse
      detect = True
    elif y <= mouse[1]:
      pygame.draw.rect(screen, color, (x, y, 5, 5))
      x += 5
      y += 5
    elif y >= mouse[1] and y > y0:
      pygame.draw.rect(screen, 'white', (x, y, 5, 5))
      pygame.draw.rect(screen, 'white', (x, y, 5, 5))
      x -= 5
      y -= 5
  if not left and mode == 3:
    if detect:
      for i in range(x0, x, 5):
        pygame.draw.rect(screen, color, (x, y, 5, 5))
        x -= 5
      for i in range(y0, y, 5):
        pygame.draw.rect(screen, color, (x0, y, 5, 5))
        y -= 5
    detect = False
  #eq triangal mode
  if left and mode == 4:
    if not detect:
      x1, y = mouse
      x2 = x1
      x0, y0 = mouse
      detect = True
    elif y <= mouse[1]:
      pygame.draw.rect(screen, color, (x1, y, 5, 5))
      pygame.draw.rect(screen, color, (x2, y, 5, 5))
      x1 += 5
      x2 -= 5
      y += 5
    elif y >= mouse[1] and y > y0:
      pygame.draw.rect(screen, 'white', (x1, y, 5, 5))
      pygame.draw.rect(screen, 'white', (x2, y, 5, 5))
      x1 -= 5
      x2 += 5
      y -= 5
  if not left and mode == 4:
    if detect:
      for i in range(x2, x1, 5):
        pygame.draw.rect(screen, color, (x2, y, 5, 5))
        x2 += 5
    detect = False
  #rhombus mode
  if left and mode == 5:
    if not detect:
      x1, y = mouse
      x2 = x1
      x0, y0 = mouse
      detect = True
    elif y <= mouse[1]:
      pygame.draw.rect(screen, color, (x1, y, 5, 5))
      pygame.draw.rect(screen, color, (x2, y, 5, 5))
      x1 += 5
      x2 -= 5
      y += 5
    elif y >= mouse[1] and y > y0:
      pygame.draw.rect(screen, 'white', (x1, y, 5, 5))
      pygame.draw.rect(screen, 'white', (x2, y, 5, 5))
      x1 -= 5
      x2 += 5
      y -= 5
  if not left and mode == 5:
    if detect:
      print(x2, x1)
      for i in range(x2, x1, 10):
        pygame.draw.rect(screen, color, (x2, y, 5, 5))
        pygame.draw.rect(screen, color, (x1, y, 5, 5))
        x2 += 5
        x1 -= 5
        y+= 5
    detect = False
  pygame.display.update()

pygame.quit()
