# Source File Name: bmBalloon.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: Saturday June 29th 2013
#Program Description: This is the test code for the Balloon Sprite.  My goal in this code is to add
#the balloon to the screen and have it move. 

#Version 0.1 - Code from Lesson 7
#Version 1.0 - Completed goals for ballon sprite class - Coin randomly moves from the bottom to 
#the top of the screen and randomly selects a x value to move from

import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

#Creates the balloon sprite and its movement      
class Balloon(pygame.sprite.Sprite):
    #method to initialize the coin sprite
    def __init__(self):
        #create the balloon sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("balloon.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dy = 5
    #end of initialize method
    
    #method to update balloon sprite
    def update(self):
        #scroll vertically until the bottom of the ballon hits the top
        self.rect.centery -= self.dy
        if self.rect.bottom < 0:
            self.reset()
    #end of update method
    
    #method to reset coin sprite       
    def reset(self):
        #randomly select the height the coin will be spawn from
        randomx = random.randint(0, 640)
        self.rect.center = (randomx, 480)
    #end of reset method
#end of Balloon class

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
    balloon = Balloon()
    balloonMan = BalloonMan()
    coin = Coin()
    
    #store the sprite variables into allSprites
    allSprites = pygame.sprite.Group(balloon, coin, balloonMan)
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
            
