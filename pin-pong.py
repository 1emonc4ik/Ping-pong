from pygame import *
from random import randint
from time import time as timer

win_wight = 720
win_height = 500
window = display.set_mode((win_wight, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('bckg.jpg'), (win_wight, win_height))

mixer.init()
mixer.music.load('goldn.ogg')
mixer.music.play()

game = True
clock = time.Clock()
FPS = 60
life = 10
finish = False

speed_x = 3
speed_y = 3
font.init()
win_1 = font.SysFont('Roboto', 40).render('win: Player_1', True, (255, 0, 0))
lose_2 = font.SysFont('Roboto', 40).render('lose: Player_2', True, (255, 0, 0))
win_2 = font.SysFont('Roboto', 40).render('win: Player_2', True, (255, 0, 0))
lose_1 = font.SysFont('Roboto', 40).render('lose: Player_1', True, (255, 0, 0))
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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

rackett_l = Player('racket.png', 5, 200, 25, 150, 15)
rackett_r = Player('racket.png', 695, 200, 25, 150, 15)
ball = GameSprite('ball.png', 320, 250, 70, 70, 10)

while game:
    if finish != True:
        window.blit(background, (0, 0))
        rackett_l.reset()
        rackett_l.update_l()
        rackett_r.reset()
        rackett_r.update_r()
        ball.reset()
        ball.rect.y -= speed_y
        ball.rect.x -= speed_x
        if sprite.collide_rect(ball, rackett_l) or sprite.collide_rect(ball, rackett_r):
            speed_x *= -1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0 :
            finish = True
            window.blit(win_2, (330 - 50, 300))
            window.blit(lose_1, (330 - 50, 200))
        
        if ball.rect.x > win_wight :
            finish = True
            window.blit(win_1, (330 - 50, 300))
            window.blit(lose_2, (330 - 50, 200))


        for e in event.get():
            if e.type == QUIT:
                game = False
        display.update()
        clock.tick(FPS)

