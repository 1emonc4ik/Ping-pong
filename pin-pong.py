from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((1200, 720))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('bckg.jpg'), (1200, 720))

mixer.init()
mixer.music.load('goldn.ogg')
mixer.music.play()

game = True
clock = time.Clock()
FPS = 60
life = 10

font.init()
font1 = font.SysFont('Arial', 40)
lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 605:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 605:
            self.rect.y += self.speed




while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
