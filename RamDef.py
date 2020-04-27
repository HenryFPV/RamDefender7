import pygame, time, random
from pygame.locals import *

pg = pygame
pg.init()
clock = pg.time.Clock()

#introBack = pg.image.load("PNG/heya.jpg")


BLACK           = (0, 0, 0)
BLUE            = (50, 50, 255)

BRIGHTGREEN     = (34,139,34)
GREEN           = (0, 255, 0)

RED             = (255, 0, 0)
DARKRED         = (200, 0, 0)
  


SCREEN_WIDTH    = 1280
SCREEN_HEIGHT   = 720



halfWinHeight   = SCREEN_HEIGHT   / 2
halfWinWIDTH    = SCREEN_WIDTH    / 2

screen          = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


#backgroundRect = introBack.get_rect()
#def intro():
#    intro = True

#    while intro:
#        for event in pg.event.get():
#            if event.type == pg.QUIT:
#                pg.quit()
#                quit()
        
#        screen.blit(introBack, backgroundRect)

#        pg.display.update()

#        clock.tick(0)
#        time.sleep(1)
#        engine()


'''#


class Player(pg.sprite.sprite):
    def __init__(self, x, y):

        super().__init__()

        self.image = pg.Surface([100,50]) #player hitbox
        self.rect  = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = None



    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y


    def update(self):
        self.rect.x += self.change_x

        block_hit_list = pg.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.Left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pg.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom





    def shoot(self):
        #shooting code

'''#

#class Bullet(pg.sprite.sprite):
 #   def __init__(self, x, y):
        #add bullet stuff



#player = Player(100, 50)
#player.image = pg.image.load("png\heya.jpg")
#player.walls = wall_list
#all_sprite_list.add(player)


def engine():   #main game loop 
    #score = 0   # initializes score counter
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


        #all_sprite_list.update()
        #all_sprite_list.draw()

        #pg.display.flip()

        #clock.tick(60)

        



engine()    

pg.quit()