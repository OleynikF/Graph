# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 30 # частота кадров в секунду

A = [[10, HEIGHT - 20], [20, HEIGHT - 30], [50, HEIGHT - 60], [0, HEIGHT], [100, HEIGHT - 100], [85, HEIGHT - 95] ]
A.sort()
d = len(A)
# создаем игру и окно

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph")
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    for i in range(d):
        pygame.draw.circle(screen, BLACK,A[i], 5)
    for i in range(d - 1):
        pygame.draw.line(screen, RED,
                   A[i], A[i + 1], 5)
    for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
