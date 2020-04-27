import pygame, time, random
from pygame.locals import *
import math
from pygame.math import Vector2



pg = pygame
clock = pg.time.Clock()

music = pg.mixer.music.load

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

def playSound():
    pg.mixer.music.play()

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



class Mob(pg.sprite.Sprite):

    def __init__(self):
        super(Mob, self).__init__()

        self.image = pygame.Surface((90, 53))
        self.image = pg.image.load("png\mob.png")
        self.image = pg.transform.scale(self.image, [90, 53])



        self.rect = self.image.get_rect()
        #self.rect.x = 1280
        #self.rect.y = 720
        
        
        self.rect.x = random.randrange(1280, 1500)
        self.rect.y = random.randrange(20, 720)        

        self.speedx = random.randrange(-5, -2)

    def update(self):
        self.rect.x += self.speedx

        if self.rect.top > self.rect.left < -60 or self.rect.right > SCREEN_WIDTH + 60:
            self.rect.x = random.randrange(1200, 1280)
            self.rect.y = random.randrange(20, 710)
            self.speedy = random.randrange(-7, -5)




class Player(pg.sprite.Sprite):

    def __init__(self, pos, x, y ):##############

        super().__init__()

        self.image = pg.Surface([56, 79])
        self.image = pg.image.load("png\chartest2.png")
        self.orig_image = self.image


        self.rect = self.image.get_rect()

        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.pos = Vector2(pos)

    def changespeed(self, x, y):

        self.change_x += x
        self.change_y += y

    def update(self):
        self.rotate()

        self.rect.x += self.change_x

        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left

            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            else:
                self.rect.top = block.rect.bottom


    
    def rotate(self):
        # The vector to the target (the mouse position).
        direction = pg.mouse.get_pos() - self.pos
        # .as_polar gives you the polar coordinates of the vector,
        # i.e. the radius (distance to the target) and the angle.
        radius, angle = direction.as_polar()
        # Rotate the image by the negative angle (y-axis in pygame is flipped).
        self.image = pg.transform.rotate(self.orig_image, -angle)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)
    

    def shoot(self):

        bullet = Bullet(self.rect.centerx +30 , self.rect.bottom -53) #where it comes out
        all_sprite_list.add(bullet)
        bullets.add(bullet)

    

class Bullet(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = pg.image.load("PNG\BULLET.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.x += self.speedy #what direction it shoots

        if self.rect.bottom < 0:
            self.kill()




class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(image_file)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



class Wall(pg.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


#sprite lists
all_sprite_list = pg.sprite.Group()
wall_list = pg.sprite.Group()
bullets = pg.sprite.Group()
mobs = pg.sprite.Group()




#bachground image
bg = Background("png\sgtest.png", [0, 0])
bg.image = pg.image.load("png\sgtest.png")
all_sprite_list.add(bg)

#wall boundaries
#1
wall = Wall(0, 720, 1280, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
#2
wall = Wall(0, 0, 1280, 0)
wall_list.add(wall)
all_sprite_list.add(wall)
#3
wall = Wall(1280, 0, 0, 720)
wall_list.add(wall)
all_sprite_list.add(wall)
#4
wall = Wall(0, 0, 0, 720)
wall_list.add(wall)
all_sprite_list.add(wall)


for i in range(10):
    m = Mob()
    all_sprite_list.add(m)
    mobs.add(m)

#player image and added to sprite list to be on screen
player = Player((640, 360),640, 360 ) #start position


player.walls = wall_list
all_sprite_list.add(player)








pg.init()

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

                elif event.key == pygame.K_SPACE:

                    music('MP3\GunShotSound-v3.wav')
                    playSound()

                    player.shoot()


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