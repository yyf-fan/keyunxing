# -*- coding: utf-8 -*-
import pygame
import os

from Constants import *
from Player import Player


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player('Player')
        self.background = pygame.image.load(os.path.join('img', 'bg.jpg'))
        self.running = True
        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            # выход из программы
            if event.type == pygame.QUIT:
                self.running = False
            # передвижение игрока
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.moving = [1, 0, 0, 0]

                if event.key == pygame.K_LEFT:
                    self.player.moving = [0, 0, 1, 0]

                if event.key == pygame.K_UP:
                    self.player.moving = [0, 0, 0, 1]

                if event.key == pygame.K_DOWN:
                    self.player.moving = [0, 1, 0, 0]

                # Действия игрока
                if event.key == pygame.K_SPACE:
                    if self.player.state != DEAD:
                        self.player.state = DEAD
                    else:
                        self.player.state = ALIVE

                if event.key == pygame.K_z:
                    if self.player.state != SHOOT:
                        self.player.state = SHOOT
                    else:
                        self.player.state = ALIVE

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving[RIGHT] = 0

                if event.key == pygame.K_LEFT:
                    self.player.moving[LEFT] = 0

                if event.key == pygame.K_UP:
                    self.player.moving[UP] = 0

                if event.key == pygame.K_DOWN:
                    self.player.moving[DOWN] = 0

    def render(self):
        # отрисовка всего
        self.screen.blit(self.background, (0, 0))
        self.player.render(screen)
        self.player.render_ui(screen)
        pygame.display.flip()

    def main_loop(self):
        # главный цикл программы
        while self.running:
            if self.player.state != DEAD:
                self.player.move()
            self.render()
            self.handle_events()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)
