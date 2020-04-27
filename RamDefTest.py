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
  

introBack = pg.image.load("PNG/intro.png")


SCREEN_WIDTH    = 1280
SCREEN_HEIGHT   = 720



halfWinHeight   = SCREEN_HEIGHT   / 2
halfWinWIDTH    = SCREEN_WIDTH    / 2

screen          = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


def text_objects0(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface = font.render(text, True, BLUE)
    return textSurface, textSurface.get_rect()


def text_objects2(text, font):
    textSurface = font.render(text, True, GREEN)
    return textSurface, textSurface.get_rect()



def button(msg, x, y, w, h, iv, av, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(screen, av, (x, y, w, h))

        if click[0] == 1 and action != None:
            if action == "quit": # quit
                #end sound
                #button click too
                pg.quit()
                quit

            elif action == "restart":
                #button click
                engine()

            #elif action == "next":
                #button click
                #tutorial goes as ()
            #elif action == "skip_Tutorial":
                #button click
                #skips tutorial as ()

    else:
        pg.draw.rect(screen, iv, (x, y, w, h))
        smallText = pg.font.Font("freesansbold.ttf", 25)

        textSurf, textRect = text_objects0(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))

        screen.blit(textSurf, textRect)



backgroundRect = introBack.get_rect()
def intro():

    intro = True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()


        screen.blit(introBack, backgroundRect)

        button("Start", 340, 475, 200, 50, GREEN, BLUE, "restart")
        button("Quit", 640, 475, 200, 50, RED, BLUE, "quit")

        pg.display.update()
        clock.tick(0)






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


class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(image_file)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location




all_sprite_list = pg.sprite.Group()
wall_list = pg.sprite.Group()

bg = Background("png\schizophrenic.jpg", [0, 0])
bg.image = pg.image.load("png\schizophrenic.jpg")
all_sprite_list.add(bg)



#player image and added to sprite list to be on screen
player = Player(100, 50)
player.image = pg.image.load("png\heya.jpg")
player.walls = wall_list
all_sprite_list.add(player)










def engine():   #main game loop 
 
    done = False  


    while not done:    

        for event in pg.event.get():     #ends game, can insert pg.QUIT() anywhere to end it.
            if event.type == pg.QUIT:
                done = True


            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_LEFT:
                    player.changespeed(-5, 0)

                if event.key == pg.K_RIGHT:
                    player.changespeed(5, 0)

                if event.key == pg.K_UP:
                    player.changespeed(0, -5)

                if event.key == pg.K_DOWN:
                    player.changespeed(0, 5)


            elif event.type == pg.KEYUP:

                if event.key == pg.K_LEFT:
                    player.changespeed(5, 0)

                if event.key == pg.K_RIGHT:
                    player.changespeed(-5, 0)

                if event.key == pg.K_UP:
                    player.changespeed(0, 5)

                if event.key == pg.K_DOWN:
                    player.changespeed(0, -5)

        all_sprite_list.update()
        all_sprite_list.draw(screen)

        pg.display.flip()

        clock.tick(60)

        



intro()    

pg.quit()