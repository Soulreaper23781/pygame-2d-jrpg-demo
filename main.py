import pygame
import player
import time

#Initiate pygame
pygame.init()
 
#Create our screen, set caption, initiate clock
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Python/Pygame Animation")
clock = pygame.time.Clock()

'''Here we create our player object. The (200, 200) values are passed to the
position parameter in our Player class. This means the top-left corner of our
character will be drawn at x-y position (200, 200) on the screen. We similary
pass our sprite sheet to the constructor, where all the methods we wrote
previously do their work and transform this into a single frame on the screen.'''
player = player.Player((200, 200), 'serge_walk.png')

#Create main loop
game_over = False
while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    #Call our event handler, fill the screen, and blit (draw) player to the screen
    player.handle_event(event)
    screen.fill(pygame.Color('black'))
    screen.blit(player.image, player.rect)
    
    pygame.display.flip()
    
    #The clock is an easy way to control our animation speed
    clock.tick(15)

pygame.quit ()