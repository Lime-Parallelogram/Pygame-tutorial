#Imports modules
import pygame
import pygame.display
from pygame.locals import *

pygame.init()

#Sets up screen
screen = pygame.display.set_mode((100,150))
pygame.draw.rect(screen,(000,255,000), (25,25,50,50),0) #Draws green button
pygame.display.update()

#Updates the display with the new text (click count)
def update_disp(font, clicks):
    pygame.draw.rect(screen, (000, 000, 000), (25, 100, 75, 50), 0) #Draws a black rectangle over the existing text --Change colour to match background
    screen.blit(font.render(str(clicks), True, (000,255,000)), (25, 100))
    pygame.display.update()

#Defines variables
clicks = 0
font = pygame.font.SysFont("Arial", 50)
running = True


while running:
    for event in pygame.event.get():
        
        #If you press the 'x' button
        if event.type == pygame.QUIT:
            running = False #End while loop
            pygame.display.quit() #Close display
            
        #If you press a button on the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos #Gets the position of the mouse click
            #Checks to see if the click position is within the green square (button)
            if x > 25 and x < 75 and y > 25 and y < 75:
                clicks += 1
                update_disp(font,clicks)
                
        #If you press any key
        if event.type == pygame.KEYDOWN:
            #If the key you pressed was r
            if event.key == K_r:
                #Reset click count
                clicks = 0
                update_disp(font,clicks)
