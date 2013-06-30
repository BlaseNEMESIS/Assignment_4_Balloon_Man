# Source File Name: bmSky.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: Saturday June 29th 2013
#Program Description: This is the test code for the object collision.  
#My goal in this code is have object collision cause different effects 

#Version 0.1 - Code from Lesson 7
#Version 1.0 - Have the background scrolling and added more bird enemies

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
        
        #if there is no pygame.mixer sound will not work
        if not pygame.mixer:
            print("problem with sound")
        else:
            #initialize the sounds
            pygame.mixer.init()
            self.sndYay = pygame.mixer.Sound("yay.ogg")
            self.sndThunder = pygame.mixer.Sound("thunder.ogg")
            self.sndEngine = pygame.mixer.Sound("engine.ogg")
            self.sndEngine.play(-1)

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

#class flying bird creates a flying bird sprite
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

#Creates the sky image scrolling background
class SkyBackground(pygame.sprite.Sprite):
    #initialize the sky background
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sky_background.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
    #end of __init__ method
    
    #update the sky background    
    def update(self):
        self.rect.left -= self.dx
        if self.rect.left <= -560:
            self.reset() 
    #end of update method
    
    #reset the sky background
    def reset(self):
        self.rect.right = 1000

    #end of the reset method
#end SkyBackground class

#Main method    
def main():
    #create game screen
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Balloon Man! bmSky.py - scrolling background")
    #create the background for the game screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    #create variables for the sprite classes
    balloon = Balloon()
    balloonMan = BalloonMan()
    coin = Coin()
    
    #enemy variables
    flyingBird1 = FlyingBird()
    flyingBird2 = FlyingBird()
    flyingBird3 = FlyingBird()
    flyingBird4 = FlyingBird()
    flyingBird5 = FlyingBird()
    
    skyBackground = SkyBackground()
    
    #store the sprite variables into good sprites and enemy sprites
    goodSprites = pygame.sprite.OrderedUpdates(skyBackground, balloon, coin, balloonMan)
    enemySprites = pygame.sprite.Group(flyingBird1, flyingBird2, flyingBird3, flyingBird4, flyingBird5)
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
                
        #check collisions good items
        if balloonMan.rect.colliderect(balloon.rect):
            balloonMan.sndYay.play()
            balloon.reset()
        if balloonMan.rect.colliderect(coin.rect):
            balloonMan.sndYay.play()
            coin.reset()
        
        #check collision for hitting enemies    
        hitEnemies = pygame.sprite.spritecollide(balloonMan, enemySprites, False)
        if hitEnemies:
            balloonMan.sndThunder.play()
            for theFlyingBird in hitEnemies:
                theFlyingBird.reset()
                
        #update the sprites and then drawn them        
        goodSprites.update()
        goodSprites.draw(screen)
        
        enemySprites.update()
        enemySprites.draw(screen)
        
        pygame.display.flip()
    
    #turn off the snd Engine for the balloon man
    balloonMan.sndEngine.stop()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
