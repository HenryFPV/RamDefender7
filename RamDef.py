import pygame, time, random
from pygame.local import *

pg = pygame
pg.init()





BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
BRIGHTGREEN = (34,139,34)
RED = (255, 0, 0)
DARKRED = (200, 0, 0)
GREEN = (0, 255, 0)

























clock = pg.time.Clock()

def engine():   #main game loop 
    score = 0   # initializes score counter
    done = False   #keeps the engine() running until set to True

    #beginning audio goes here ...

    while not done:     #wgile done is not True


        for event in pg.event.get():     #ends game, can insert pg.QUIT() anywhere to end it.
            if event.type == pg.QUIT():
                done = True


            elif event.type == pg.KEYDOWN:

                if event.type == pg.K_LEFT:
                    player.changespeed(-5, 0)

                if event.type == pg.K_RIGHT:
                    player.changespeed(5, 0)

                if event.type == pg.K_UP:
                    player.changespeed(0, -5)

                if event.type == pg.K_DOWN:
                    player.changespeed(0, 5)


            elif event.type == pg.KEYUP:

                if event.type == pg.K_LEFT:
                    player.changespeed(5, 0)

                if event.type == pg.K_RIGHT:
                    player.changespeed(-5, 0)

                if event.type == pg.K_UP:
                    player.changespeed(0, 5)

                if event.type == pg.K_DOWN:
                    player.changespeed(0, -5)
            
            
        all_sprite_list.update()
        all_sprite_list.draw()

        pg.display.flip()

        Clock.tick(60)

        



intro()    

pg.quit()