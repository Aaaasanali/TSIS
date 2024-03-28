import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 200))


def play(num):
  if num == 1:
    pygame.mixer.music.load('song1.mp3')
  if num == 2:
    pygame.mixer.music.load('song2.mp3')
  if num == 3:
    pygame.mixer.music.load('song3.mp3')
  pygame.mixer.music.play()


que = 0
paused = False
vol = 1.0
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        pygame.mixer.music.unload
        if que < 4:
          que += 1
          play(que)
        if que == 4:
          que = 1
          play(que)

      if event.key == pygame.K_LEFT:
        pygame.mixer.music.unload
        if que > 0:
          que -= 1
          play(que)
        if que == 0:
          que = 3
          play(que)

      if event.key == pygame.K_SPACE:
        if paused:
          print("unpaused")
          pygame.mixer.music.unpause()
          paused = False
        else:
          print("paused")
          pygame.mixer.music.pause()
          paused = True
      
      if event.key == pygame.K_UP:
        vol += 0.1
        pygame.mixer.music.set_volume(vol)
      if event.key == pygame.K_DOWN:
        vol -= 0.1
        pygame.mixer.music.set_volume(vol)

    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
  
