# -*- coding: utf-8 -*-
import pygame

from Constants import *


class Player:
    def __init__(self, name):
        self.direction = DOWN
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = ['img/archer_r.png', 'img/archer_d.png', 'img/archer_l.png', 'img/archer_u.png']
        self.images = []

        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0, 0, 64, 64))
            i.append(temp.subsurface(64, 0, 64, 64))
            i.append(temp.subsurface(128, 0, 64, 64))
            self.images.append(i)

        self.moving = [0, 0, 0, 0]

    def move(self):
        if self.moving[RIGHT] == 1:
            self.direction = RIGHT
            self.x += PLAYER_SPEED

        if self.moving[LEFT] == 1:
            self.direction = LEFT
            self.x -= PLAYER_SPEED

        if self.moving[UP] == 1:
            self.direction = UP
            self.y -= PLAYER_SPEED

        if self.moving[DOWN] == 1:
            self.direction = DOWN
            self.y += PLAYER_SPEED

        # проверка коллизий с границами экрана
        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDTH - 60: self.x = SCREEN_WIDTH - 60
        if self.y >= SCREEN_HEIGHT - 64: self.y = SCREEN_HEIGHT - 64

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):
        screen.blit(pygame.image.load('img/hpframe.png'), (self.x + 12, self.y + 58))
        m = 1
        z = self.hp // 5
        while m <= z:
            screen.blit(pygame.image.load('img/hptick.png'), (self.x+11+m*2, self.y + 59))
            m += 1
