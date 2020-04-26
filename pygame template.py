# Pygame modules

# Template for the pygame programs

import pygame, random
from myshape import *
# Pygame initialization
pygame.init()
pygame.mixer.init() # Sounds

#window creation - Tuple with width and height
width=800
height=800

# add new colors to the dictionary
BLACK = (0,0,0)
colors_dictionary= { 'red': (255,0,0) , 'green': (0,255,0), 'blue': (0,0,255) , 'pink':(255,0,102)}


tuple_screen=(width,height)
screen=pygame.display.set_mode(tuple_screen)
pygame.display.set_caption("My First game")
#my_image = pygame.image.load("user.png")
#Game loop
#Events - pressing akey, clicking a button
flag=True
while flag:
    # Input /Events
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            flag=False
    #update your game
    shapes_group.update()
    # Display
    screen.fill((0,255,0))
    #shapes_group.draw(screen)
    # Fill Green
    #my_image = pygame.image.load("bg.jpg")
    #my_image1 = pygame.image.load("villan.png")
    #screen.blit(my_image,[0,0])
    #screen.blit(my_image1,[350,100])
    for key,value in colors_dictionary.items():
        #pygame.draw.rect(screen,value,(100,100,150,150))
        #DRaw any shape up to you
        #pygame.draw.polygon(screen,value,[(30,70),(90,120),(10,50),(200,300)])
        pygame.display.update() # update screen display.flip() will do same as update()
pygame.quit()



