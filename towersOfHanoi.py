import pygame

pygame.init()   
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')         

# Frame rate    
#   1.Ceiling = max frame rate,     2.Floor = min frame rate
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:       # pygame.QUIT    'X' close window button     
      pygame.quit()                     # quit from pygame 
      exit()                            # exit program, even if more code below no error


  pygame.display.update()               # update screen as per user input
  clock.tick(60)                        # Ceiling = 60fps,    while loop must not run more than 60 times per sec
