# Source File Name: balloonMan.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: July 11th 2013
#Program Description: You are the balloon man.  Fly around the sky collecting coins to increase
#your score.  Also keep an eye out for balloons as they will give you an extra balloon.  Watch
#out though birds fly through the sky and colliding with them will cause you to lose a balloon.
#If you run out of ballons the game is over.

#Version 0.1 - Code from Lesson 7
#Version 0.2 - Added the Balloon Man Class
    
import pygame
pygame.init()

#Creates the balloon man sprite and its controls
class BalloonMan(pygame.sprite.Sprite):
    #initializtion of the ballon man
    def __init__(self):
        #load the sprite onto the screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("balloon_man.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
    #end of __init__ method    
        
    #update the sprite of balloon man  
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
    #end of update method
#end of the balloonMan class
 
#The main method        
def main():
    
    #set the dimensions for the game screen
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Balloon Man! mpBallonMan.py - creating the Ballon Man sprite")

    #add the background to the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    
    #set a variable for the BalloonMan class
    balloonMan = BalloonMan()
    
    #add the ballonman sprite to variable allSprites
    allSprites = pygame.sprite.Group(balloonMan)
    #set the fps to 30
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        #clear the sprites from the screen and the background, update the sprites and then 
        #draw them back on the screen.        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
#end of main method
if __name__ == "__main__":
    main()
            
