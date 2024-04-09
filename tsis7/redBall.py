import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
x = 250
y = 250
run = True
while run:
  screen.fill('cyan')

  pygame.draw.circle(screen, 'red', (x, y), 25.0)

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        y-=20
      if event.key == pygame.K_DOWN:
        y+=20
      if event.key == pygame.K_RIGHT:
        x+=20
      if event.key == pygame.K_LEFT:
        x-=20
    if event.type == pygame.QUIT:
      run = False
pygame.quit()
