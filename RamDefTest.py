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

'''#

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

'''#

class Mob(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Mob, self).__init__()
        
        self.image = pygame.Surface((90, 53))
        self.image = pg.image.load("png\mob.png")
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.math.Vector2(position)
        self.speed = 2


    def attack(self):
        player_position = player.rect.topleft
        direction = player_position - self.position
        velocity = direction.normalize() * self.speed

        self.position += velocity
        self.rect.topleft = self.position

    def update(self):
        self.rotate()
        self.attack()
        
    
    def rotate(self):
        direction = (640,360) - self.position #change value in first () to change mob looking direction
        radius, angle = direction.as_polar()
        self.image = pg.transform.rotate(self.orig_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)



class Player(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface([50, 30])
        self.image = pg.image.load("PNG\chartest2.png")
        
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.walls = None


    def update(self):
        self.rotate()

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
        self.rect.y += self.speedy #what direction it shoots

        if self.rect.bottom < 0:
            self.kill()

        #elif self.rect.top < 0:
        #    self.kill()

        #elif self.rect.left < 0:
        #    self.kill()

        #elif self.rect.right < 0:
        #    self.kill()
    
    def set_target(self, pos):
        self.target = pygame.Vector2(pos)




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
players = pg.sprite.Group()



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






#mobs spawning
#ElDorito = [(1280, 720), (0,0), (1280, 0), (0, 720)]

#maxmobs = 4
#sampled_list = random.sample(ElDorito, maxmobs)

#random.choice(ElDorito,)



my1list = [(1280, 720), (0,0), (1280, 0), (0, 720),(640, 720) ,(640, 720), (0, 360), (0, 360) ]

for i in range(4):
    m = Mob(random.choice(my1list))
    all_sprite_list.add(m)
    mobs.add(m)

#player image and added to sprite list to be on screen
player = Player((640,360)) #start position
all_sprite_list.add(player)





#```






pg.init()

def engine():   #main game loop 
    countT = 0
    done = False  


    while not done:    

        for event in pg.event.get():     #ends game, can insert pg.QUIT() anywhere to end it.
            if event.type == pg.QUIT:
                done = True
            
            #if event.type == pygame.MOUSEBUTTONDOWN:
             #   for bullets in all_sprite_list():
             #       bullet.set_target(pygame.mouse.get_pos())


            if event.type == pg.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    music('MP3\GunShotSound-v3.wav')
                    playSound()

                    player.shoot()


            #elif event.type == pg.KEYUP:

        #player.update()
        #m.update(player)

        all_sprite_list.update()

        bullethit = pygame.sprite.groupcollide(mobs, bullets, True, True)

        for bullethi in bullethit:
            #sound goes here for death of mob or bullet hit sound
            #score += 1
            m = Mob(random.choice(my1list))
            all_sprite_list.add(m)
            mobs.add(m)


        BarnDead = pg.sprite.spritecollide(player, mobs, True)


        if BarnDead:
            #music goes here
            countT += 1
            if countT == 4:   # health = 4
                done = True
                pg.quit
                quit
            else:
                pass

            m = Mob(random.choice(my1list))
            all_sprite_list.add(m)
            mobs.add(m)
            #time.sleep(1.2)
            #outro
            pg.quit
            quit


        all_sprite_list.draw(screen)
        screen.blit(player.image, player.rect)

        pg.display.flip()

        clock.tick(60)

        



intro()    

pg.quit()