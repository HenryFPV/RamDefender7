import pygame 
from pygame.math import Vector2
pg = pygame 

class Player(pg.sprite.Sprite):

    def __init__(self, pos, x, y):
        super().__init__()
        self.image = pg.Surface((50, 30), pg.SRCALPHA)
        pg.draw.polygon(self.image, pg.Color('steelblue2'),
                        [(0, 0), (50, 15), (0, 30)])
        self.orig_image = self.image  # Store a reference to the original.
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = None

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


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()



all_sprite_list = pg.sprite.Group()

player = Player((300, 220,), 20, 20)

all_sprite_list.add(player)







done = False

while not done:
    for event in pg.event.get():
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

                    music('MP3\GunShotSound.mp3')
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

    all_sprite_list.draw(screen)
    screen.fill((30, 30, 30))
    all_sprite_list.draw(screen)

    pg.display.flip()
    clock.tick(30)