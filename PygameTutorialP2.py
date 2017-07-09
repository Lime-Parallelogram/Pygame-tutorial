import pygame
import pygame.display
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((100,150))
pygame.draw.rect(screen,(000,255,000), (25,25,50,50),0)
pygame.display.update()

def update_disp(font, clicks):
    pygame.draw.rect(screen, (000, 000, 000), (25, 100, 75, 50), 0)
    screen.blit(font.render(str(clicks), True, (000,255,000)), (25, 100))
    pygame.display.update()

clicks = 0
font = pygame.font.SysFont("Arial", 50)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if x > 25 and x < 75 and y > 25 and y < 75:
                clicks += 1
                update_disp(font,clicks)
        if event.type == pygame.KEYDOWN:
            if event.key == K_r:
                clicks = 0
                update_disp(font,clicks)
