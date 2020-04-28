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
endscreen = pg.image.load("PNG/sgtest.png")

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


def outro():

    outro = True
    #music here
    
    while outro:
        for event in pg.event.get():
            if event.type == pg.quit:
                pg.quit()
                quit()
        screen.blit(endscreen, backgroundRect) #find endscreen image

        largeText = pg.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects0("Delta build d282.56.2", largeText)
        TextRect.center = (1000, 25)
        screen.blit(TextSurf, TextRect)

        button("AAAAAAA", 540, 450, 200, 50, RED, DARKRED, "quit")
        button("BBBBBBB", 540, 550, 200, 50, RED, DARKRED, "restart")

        pg.display.update()
        clock.tick(0)    

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
        direction = pg.mouse.get_pos() - self.pos
        radius, angle = direction.as_polar()
        self.image = pg.transform.rotate(self.orig_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    #def shoot(self):
        #music('MP3\GunShotSound-v3.wav')
        #playSound()
        #bullet = Bullet(pg.mouse.get_pos()) #where it comes out
        #all_sprite_list.add(bullet)
        #bullets.add(bullet)
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, dest_x, dest_y):
        """ Constructor.
        It takes in the starting x and y location.
        It also takes in the destination x and y position.
        """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Set up the image for the bullet
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
        # Move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y
 
        # Because rect.x and rect.y are automatically converted
        # to integers, we need to create different variables that
        # store the location as floating point numbers. Integers
        # are not accurate enough for aiming.
        self.floating_point_x = start_x
        self.floating_point_y = start_y
 
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
 
        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        velocity = 5
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity
    
'''
class Bullet(pg.sprite.Sprite):

    def __init__(self,position):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = pg.image.load("PNG\BULLET.png")
        #self.rect = self.image.get_rect()
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.math.Vector2(position)
        #self.rect.bottom = y
        #self.rect.centerx = x
        self.speed = 10
        #self.pos = Vector2(pos)

    def update(self):
        self.rotate()
        #self.trajectory()
        #self.rect.y += self.speedy #what direction it shoots
        #self.position + self.speed
        if self.rect.bottom < 0:
            self.kill()
       
    def trajectory(self):
        mouse_position = pg.mouse.get_pos()
        direction = mouse_position - self.position
        velocity = direction.normalize() * self.speed

        self.position += velocity
        self.rect.topleft = self.position

    def rotate(self):
        direction = pg.mouse.get_pos() - self.position
        radius, angle = direction.as_polar()
        self.image = pg.transform.rotate(self.orig_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        #elif self.rect.top < 0:
        #    self.kill()

        #elif self.rect.left < 0:
        #    self.kill()

        #elif self.rect.right < 0:
        #    self.kill()
    
    def set_target(self, pos):
        self.target = pygame.Vector2(pos)

'''


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
#bullets = pg.sprite.Group()
bullet_list = pg.sprite.Group()
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





#listTOP = [top1, top2]
#listBOTTOM = [bottom1, bottom2]
#listLEFT = [left1, left2]
#listRIGHT = [right1, right2]

#mobs spawning
#ElDorito = [(1280, 720), (0,0), (1280, 0), (0, 720)]

top1 = random.randint(0, 1280)     # y = 720 stays constant, 1280 is var 0 - 1280
bottom1 = random.randint(0, 1280)      # y = 0 styas constant, 1280 is var 0-1280
left1 = random.randint(0, 720)      # x = 0 stays constant, 720 is var 0 - 720 
right1 = random.randint(0, 720)  # x = 1280 stays constant, 0-720 is var  
#maxmobs = 4
#sampled_list = random.sample(ElDorito, maxmobs)

#random.choice(ElDorito,)

#my1list = [(1280, 720), (0,0), (1280, 0), (0, 720),(640, 720) ,(640, 720), (0, 360), (0, 360) ]
#top, bottom, left, right. all have x or y as one constant value at alltimes

# X !> Y
mobRandSpawn = [ (720, top1 ), (0, bottom1), (left1, 0), (right1, 1280) ]

#for i in range(25):
#    m = Mob(random.choice(mobRandSpawn))
 #   all_sprite_list.add(m)
 #   mobs.add(m)

#player image and added to sprite list to be on screen
player = Player((640,360)) #start position
all_sprite_list.add(player)





#```


player.rect.x = SCREEN_WIDTH / 2
player.rect.y = SCREEN_HEIGHT / 2



pg.init()

def engine():   #main game loop 
    countT = 0
    done = False  
    
    
    top1 = random.randint(0, 1280)     # y = 720 stays constant, 1280 is var 0 - 1280
    bottom1 = random.randint(0, 1280)      # y = 0 styas constant, 1280 is var 0-1280
    left1 = random.randint(0, 720)      # x = 0 stays constant, 720 is var 0 - 720 
    right1 = random.randint(0, 720)  # x = 1280 stays constant, 0-720 is var        
    mobRandSpawn = [ (720, top1 ), (0, bottom1), (left1, 0), (right1, 1280) ]

    while not done:    

        for event in pg.event.get():     #ends game, can insert pg.QUIT() anywhere to end it.
            if event.type == pg.QUIT:
                done = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                bullet = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)
                all_sprite_list.add(bullet)
                bullet_list.add(bullet)




            #if event.type == pg.KEYDOWN:

            #    if event.key == pygame.K_SPACE:
            #        player.shoot()


            #elif event.type == pg.KEYUP:

        #player.update()
        #m.update(player)

        all_sprite_list.update()

        #bullethit = pygame.sprite.groupcollide(mobs, bullet, True, True)

        #for bullethi in bullethit:
            #sound goes here for death of mob or bullet hit sound
            #score += 1
            #m = Mob(random.choice(mobRandSpawn))
            #all_sprite_list.add(m)
            #mobs.add(m)

        #for bullet in bullet_list:
            #block_hit_list = pygame.sprite.spritecollide(bullet, mobs, True)

            #for mobs in block_hit_list:
            #    bullet_list.remove(bullet)
            #    all_sprite_list.remove(bullet)
            #    score += 1
            #    print(score)

            #if bullet.rect.y < -10:
            #    bullet_list.remove(bullet)
            #    all_sprites_list.remove(bullet)

        BarnDead = pg.sprite.spritecollide(player, mobs, True)


        if BarnDead:
            #music goes here
            countT += 1
            if countT == 4:   # health = 4
                done = True
                outro()
            
            else:
                m = Mob(random.choice(mobRandSpawn))
                all_sprite_list.add(m)
                mobs.add(m)
                pass
            

           
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