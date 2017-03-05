#imports modules
import pygame
import pygame.display

#initializes modules
pygame.init()
pygame.display.init()

#sets caption and sets up display
pygame.display.set_caption("Pygame Tutorial")
screen = pygame.display.set_mode((640,480))

#fills in screen white
screen.fill((255,255,255))

#draws shapes on the screen
pygame.draw.rect(screen, (0, 255, 0), (1, 1, 40, 40), 0) #draws rectangle on screen
pygame.draw.line(screen, (0,255,0), (51,1), (151, 101), 3) #draws a line between two points on screen
pygame.draw.circle(screen, (0,255,0), (200,200), 65, 5) #draws a circle from a centeral point
pygame.draw.polygon(screen, (0,0, 255), [(400,400), (450, 350), (500,400)], 0) #plots and joins a list of points

#puts text on screen
font = pygame.font.SysFont("dejavusans", 72) #defines font
text = font.render("Hello world", True, (255,0,0)) #creates text object ready for blit
screen.blit(text, (21,200)) #blits text object to screen

#puts picture on  screen
image = pygame.image.load("/home/pi/Pictures/LOGO.png") #loads image into variable
Simage = pygame.transform.scale(image, (190, 97)) #scaled image down to new dimensions
screen.blit(Simage, (21, 400)) #blits the scaled version of the image to the screen

pygame.display.update() #updates the screen and draws all of the changes to the window
