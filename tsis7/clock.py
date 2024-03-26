import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((1400, 1050))

clock = pygame.image.load('mickeyclock.jpeg.png').convert_alpha()
minute1 = pygame.image.load('mickeyMinute.png').convert_alpha()
hour1 = pygame.image.load('mickeyHour.png').convert_alpha()

running = True
while running:
  now = datetime.datetime.now()
  time = now.time().replace(microsecond=0, second=0)

  minute = time.replace(hour=0)
  minute_str = minute.strftime("%H%M%S")

  hour = time.replace(minute=0)
  hour_str = hour.strftime("%H%M%S")  

  hour_int = int(hour_str)/10000
  minute_int = int(minute_str)/100

  hour_angle = (-50 - 30*hour_int)
  minute_angle = (58 - 6*minute_int)

  minute = pygame.transform.rotate(minute1,  minute_angle)
  minute_rect = minute.get_rect(center = (700, 525))

  hour = pygame.transform.rotate(hour1, hour_angle)
  hour_rect = hour.get_rect(center = (700, 525))
  screen.blit(clock, (0,0))
  screen.blit(minute, minute_rect)
  screen.blit(hour, hour_rect)
  
  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()  
