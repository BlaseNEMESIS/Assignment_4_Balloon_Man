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
#Version 0.25 - Added the Coin Class - Also adjusted image sizes

import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

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
        
#Creates the coin sprite and its movement      
class Coin(pygame.sprite.Sprite):
    #method to initialize the coin sprite
    def __init__(self):
        #create the coin sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    #end of initialize method
    
    #method to update coin sprite
    def update(self):
        #scroll horizontally until the right side of the coin hits the edge
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
    #end of update method
    
    #method to reset coin sprite       
    def reset(self):
        #randomly select the height the coin will be spawn from
        randomy = random.randint(0, 480)
        self.rect.center = (640, randomy)
    #end of reset method
#end of Coin class

#Main method    
def main():
    #create game screen
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Balloon Man! mpCoin - adding the Coin Sprite")
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    #create variables for the sprite classes
    balloonMan = BalloonMan()
    coin = Coin()
    
    #store the sprite variables into allSprites
    allSprites = pygame.sprite.Group(balloonMan, coin)
    #set the fps
    clock = pygame.time.Clock()
    keepGoing = True
    #run the game until the game is over
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        #clear the sprites, update them and then drawn them        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
#end of main method
if __name__ == "__main__":
    main()
            
