import pygame, time, random
from pygame.locals import *


pg = pygame
clock = pg.time.Clock()
pg.init()

BLACK           = (0, 0, 0)
BLUE            = (50, 50, 255)

BRIGHTGREEN     = (34,139,34)
GREEN           = (0, 255, 0)

RED             = (255, 0, 0)
DARKRED         = (200, 0, 0)
  

introBack = pg.image.load("PNG/heya.jpg")


SCREEN_WIDTH    = 1280
SCREEN_HEIGHT   = 720



halfWinHeight   = SCREEN_HEIGHT   / 2
halfWinWIDTH    = SCREEN_WIDTH    / 2

screen          = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])



#backgroundRect = introBack.get_rect()
def intro():

    intro = True
    while intro:
        for event in pg.event.get():
            if event.type== pg.QUIT:
                pg.quit()
                quit()


        #screen.blit(introBack, backgroundRect)
        screen.blit(pg.Color.r)
        pg.display.update()

        clock.tick(0)
        time.sleep(1)
        engine()





class Player(pg.sprite.Sprite):
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

        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.Left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom







all_sprite_list = pg.sprite.Group()
wall_list = pg.sprite.Group()



player = Player(100, 50)
#player.image = pg.image.load("png\heya.jpg")
player.walls = wall_list
all_sprite_list.add(player)





def engine():   #main game loop 
 
    done = False  


    while not done:    

        for event in pg.event.get():     #ends game, can insert pg.QUIT() anywhere to end it.
            if event.type == pg.QUIT:
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
        all_sprite_list.draw(screen)

        pg.display.flip()

        clock.tick(60)

        



intro()    

pg.quit()