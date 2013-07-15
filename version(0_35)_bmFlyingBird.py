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
#Version 0.3 - Added the Balloon Class - Adjusted image sizes again
#Version 0.35 - Added the Flying Bird Class

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

#method flying bird creates a flying bird sprite
class FlyingBird(pygame.sprite.Sprite):
    #method that initializes the flying bird sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("flying_bird.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    #end of __init__ method

    #method that updates the flying bird sprite
    def update(self):
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy
        #if the flying bird sprite hits the bottom of the screen,
        #the top of the screen or passes the left side of the
        #screen run the reset method
        if self.rect.top > screen.get_height() or self.rect.bottom < 0 or self.rect.right < 0:
            self.reset()       
    #end of update method
    
    #method reset the flying bird sprite
    def reset(self):
        #randomly select the height the coin will be spawn from
        randomy = random.randint(0, 460)
        self.rect.center = (640, randomy)
        self.dx = random.randrange(12, 15)
        self.dy = random.randrange(-3, 3)
    #end of reset method
#end of flying bird class

#Main method    
def main():
    #create game screen
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Balloon Man! mpFlyingBird - adding the Flying Bird Sprite")
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    #create variables for the sprite classes
    balloon = Balloon()
    balloonMan = BalloonMan()
    coin = Coin()
    flyingBird = FlyingBird()
    
    #store the sprite variables into allSprites
    allSprites = pygame.sprite.OrderedUpdates(balloon, coin, balloonMan, flyingBird)
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
            
