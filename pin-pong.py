from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((720, 500))
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
    def __init__(self, player_image, player_x, player_y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
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

rackett_l = Player('racket.png', 5, 200, 25, 150, 15)
rackett_r = Player('racket.png', 695, 200, 25, 150, 15)
ball = GameSprite('ball.png', 320, 250, 50, 50, 10)

while game:
    window.blit(background, (0, 0))
    rackett_l.reset()
    rackett_r.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)

