import pygame

running = True

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
