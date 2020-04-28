import pygame, time, random
from pygame.locals import *


#change mob spawn locations, hitboxes, sound



pg = pygame
pg.init()


#loads images for screens
pg.display.set_caption('Defence')
introt = pg.image.load("png/intro.png")
loppt = pg.image.load("png/loss2.png")
ladu = pg.image.load("png/sgtest.png")
voitekr = pg.image.load("png/sgtest.png")

backgroundRect = introt.get_rect()

#music shortcuts
musica = pg.mixer.music.load
mainsound = pg.mixer.Sound('MP3\dote.wav')

#colours
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
BRIGHTGREEN = (34,139,34)
RED = (255, 0, 0)
DARKRED = (200, 0, 0)
GREEN = (0, 255, 0)

#specify screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# specify half-screen timensions
halfWinHeight = SCREEN_HEIGHT / 2
halfWinWIDTH = SCREEN_WIDTH / 2

#screen pfft
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#defines music starting, when called
def music_on():
    pg.mixer.music.play()

#defines text objects with random numbers because i liked them
def text_objects2(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def text_objects4(text, font):
    textSurface = font.render(text, True, BLUE)
    return textSurface, textSurface.get_rect()

#defines buttons and their actions
def button(msg, x, y, w, h, iv, av, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(screen, av, (x, y, w, h))

        if click[0] == 1 and action != None:
            if action == "quit":
                musica('MP3\count.wav')
                music_on()
                time.sleep(0.5)

                musica('MP3\count.wav')
                music_on()
                time.sleep(2)

                pg.quit()
                quit

            elif action == "more":
                musica('MP3\count.wav')
                music_on()

                intro()

            elif action == "edasi":
                musica('MP3\count.wav')
                music_on()

                keskmine()

    else:
        pg.draw.rect(screen, iv, (x, y, w, h))
        smallText = pg.font.Font("freesansbold.ttf", 25)

        textSurf, textRect = text_objects2(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))

        screen.blit(textSurf, textRect)


def intro():   #intro screen
    intro = True

    musica('MP3\intro.wav')
    music_on()

    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.blit(introt, backgroundRect)
     

        button("advance", 340, 475, 200, 50, GREEN, BRIGHTGREEN, "edasi")
        button("r2n", 640, 475, 200, 50, RED, DARKRED, "quit")


        pg.display.update()

        clock.tick(0)


def keskmine():   #tutorial screen
    keskmine = True

    while keskmine:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.blit(ladu, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects4("move with arrow keys", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT - 100))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects4("fire with space", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 160))
        screen.blit(TextSurf, TextRect)

        largeText = pg.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects4("dont let em get you", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 220))
        screen.blit(TextSurf, TextRect)

        pg.display.update()

        time.sleep(1)

        musica('sound\woman mad.wav')
        music_on()

        time.sleep(4)

        clock.tick(0)

        engine()




def winn():   #win screen 
    winn = True
    
    musica('MP3\end.wav')
    music_on()
    
    while winn:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit

        screen.blit(voitekr, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects4("sleepover time!", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 3))
        screen.blit(TextSurf, TextRect)





        button("GG!", 350, 400, 200, 50, RED, DARKRED, "quit")

        pg.display.update()

        clock.tick(0)


def outro(): #death screen
    outro = True
    musica('sound\lossSound.mp3')
    music_on()
    
    while outro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        screen.blit(loppt, backgroundRect)

        largeText = pg.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects4("Delta ehitis d282.56.2", largeText)
        TextRect.center = (600, 585)
        screen.blit(TextSurf, TextRect)

        button("GET WELL!", 540, 600, 200, 50, RED, DARKRED, "quit")


        largeText = pg.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects4("You cant restart what you couldnt finish!", largeText)
        TextRect.center = (600, 340)
        screen.blit(TextSurf, TextRect)

        pg.display.update()

        clock.tick(0)

#creating our background class
class Background(pg.sprite.Sprite):

    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(image_file)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#creates our score, size, text and everything
def score(surf, text, size, x, y):
    largeText = pg.font.Font('freesansbold.ttf', size)
    textSurf = largeText.render(text, True, RED)
    textRect = textSurf.get_rect()
    textRect.midtop = (x-390, y)

    surf.blit(textSurf, textRect)

#creates player class
class Player(pg.sprite.Sprite):

    def __init__(self, x, y):  #initializes player class
        
        super().__init__()

        self.image = pg.Surface([53, 67])
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y): #defines player change speed functions

        self.change_x += x
        self.change_y += y

    def update(self): #defines updates so that it wont get stuck after first loop and hitboxes

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

    def shoot(self): #shoots bullets

        bullet = Bullet(self.rect.centerx, self.rect.bottom - 25)
        all_sprite_list.add(bullet)
        bullets.add(bullet)
 
class Bullet(pg.sprite.Sprite): #creates bullet class

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 19))
        self.image = pg.image.load("png\BULLET.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.x += self.speedy

        if self.rect.centerx > 1280: #kills if gets out of bounds
            self.kill()



class Mob(pg.sprite.Sprite): #creates mob class

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((60, 1000))
        self.image = pg.image.load("png\mob.png")
        self.image = pg.transform.scale(self.image, [60, 100])

        self.rect = self.image.get_rect()
#        self.rect.x = 900
#        self.rect.y = 500
        
        
        self.rect.x = random.randrange(1280, 1500)
        self.rect.y = random.randrange(20, 700)        

        self.speedx = random.randrange(-5, -2)

    def update(self): #movement and spawn locations
        self.rect.x += self.speedx

        if self.rect.top > self.rect.left < -60 or self.rect.right > SCREEN_WIDTH + 60:
            self.rect.x = random.randrange(1280, 1500)
            self.rect.y = random.randrange(20, 700)
            self.speedy = random.randrange(-7, -5)


class Wall(pg.sprite.Sprite): #creates our wall class for player to not get out

    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

#sprites lists
all_sprite_list = pg.sprite.Group()
mobs = pg.sprite.Group()
bullets = pg.sprite.Group()
wall_list = pg.sprite.Group()

#background image when playing
bg = Background("png\Yground.png", [0, 0])
bg.image = pg.image.load("png\Yground.png")
all_sprite_list.add(bg)

#init player sprite
player = Player(640, 340)
player.image = pg.image.load("png\opiumMike.png")
player.walls = wall_list

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

#spawns mobs in
for i in range(10):
    m = Mob()
    all_sprite_list.add(m)
    mobs.add(m)

all_sprite_list.add(player)

clock = pg.time.Clock()

#maingame loop
def engine():
    skoor = 0
    done = False
    pg.mixer.Sound.play(mainsound)
    
    while not done:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                done = True

            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_LEFT:
                    player.changespeed(-5, 0)

                elif event.key == pg.K_RIGHT:
                    player.changespeed(5, 0)

                elif event.key == pg.K_UP:
                    player.changespeed(0, -5)

                elif event.key == pg.K_DOWN:
                    player.changespeed(0, 5)

                elif event.key == pygame.K_SPACE:

                    musica('MP3\sara.wav')
                    music_on()
                    player.shoot()

            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    player.changespeed(5, 0)

                elif event.key == pg.K_RIGHT:
                    player.changespeed(-5, 0)

                elif event.key == pg.K_UP:
                    player.changespeed(0, 5)

                elif event.key == pg.K_DOWN:
                    player.changespeed(0, -5)

        all_sprite_list.update()

        hitted = pygame.sprite.groupcollide(mobs, bullets, True, True)

        for hitte in hitted:
            musica('MP3\sike.wav')
            music_on()

            skoor += 1

            m = Mob()
            all_sprite_list.add(m)
            mobs.add(m)


        mobdead = pg.sprite.spritecollide(player, mobs, False)

        if mobdead:
            musica('MP3\died.wav')
            music_on()

            time.sleep(1.2)
            pg.mixer.Sound.stop(mainsound)
            outro()

        all_sprite_list.draw(screen)

        score(screen, str(skoor), 30, 450, 60)

        pg.display.flip()

        clock.tick(60)
        if skoor == 15:
            pg.mixer.Sound.stop(mainsound)
            winn()
            

intro()
pg.quit()
