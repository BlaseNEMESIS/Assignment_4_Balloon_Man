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
#Version 0.4 - Removed the orignal code not looked at yet.  Added collision logic to my code
#with sound effects.  The sound effects are from lesson 7.  Will add original sounds to my
#code later on.
#Version 0.5 - Added screen scrolling for the sky background and also added 5 birds to the game
#instead of just one bird
#Version 0.6 - Added a scoreboard to the game.  When colliding with a balloon you gain one life
#When colliding with a coin you gain 50 points.  When colliding with a flying bird you lose
#one life.  If you run out of lives the game resets
#Version 0.7 - Added an intro to the game and when you lose the intro loads up with your last
#score - Need to work on making it so that when you lose you can actually quit out with escape
#Version 0.8 - Have the game over screen working also allow you to quit out when you 
#select escape on the game over screen or intro screen.

import pygame, random, sys
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

#create the scoreboard sprite
class Scoreboard(pygame.sprite.Sprite):
    #initialize the scoreboard
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
    #end of __init__ method
    
    #update the scoreboard    
    def update(self):
        self.text = "lives: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
    #end of update method
#end of Scoreboard Class

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

#game method runs the game
def game():
    pygame.display.set_caption("Balloon Man! bmScore.py - Scoreboard")
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
    
    scoreboard = Scoreboard()
    skyBackground = SkyBackground()
    
    #store the sprite variables into good sprites, enemy sprites and score Sprite
    goodSprites = pygame.sprite.OrderedUpdates(skyBackground, balloon, coin, balloonMan)
    enemySprites = pygame.sprite.Group(flyingBird1, flyingBird2, flyingBird3, flyingBird4, flyingBird5)
    scoreSprite = pygame.sprite.Group(scoreboard)
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
                
        #check collisions if you hit the balloon give the player a life
        if balloonMan.rect.colliderect(balloon.rect):
            balloonMan.sndYay.play()
            balloon.reset()
            scoreboard.lives +=1
        
        #check collision if you hit the coin increase score by 50    
        if balloonMan.rect.colliderect(coin.rect):
            balloonMan.sndYay.play()
            coin.reset()
            scoreboard.score += 50
        
        #check collision for hitting enemies    
        hitEnemies = pygame.sprite.spritecollide(balloonMan, enemySprites, False)
        if hitEnemies:
            balloonMan.sndThunder.play()
            scoreboard.lives -= 1
            #if your run out of lives run a game over
            if scoreboard.lives <= 0:
                scoreboard.lives = 5
                score = scoreboard.score
                scoreboard.score = 0
                gameOver(score)
            for theFlyingBird in hitEnemies:
                theFlyingBird.reset()
                
        #update the sprites and then drawn them        
        goodSprites.update()
        enemySprites.update()
        scoreSprite.update()
        
        goodSprites.draw(screen)
        enemySprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    #turn off the snd Engine for the balloon man
    balloonMan.sndEngine.stop()
    
    #return mouse cursor
    pygame.mouse.set_visible(True)
    return score
#end of game method

#game over method display the game over screen
def gameOver(score):
    #create a varaible to store the skybackground
    skyBackground = SkyBackground()
    #load the skybackground into allSprites
    allSprites = pygame.sprite.Group(skyBackground)
    insFont = pygame.font.SysFont(None, 40)
    
    #set the loss variable
    loss = (
    "Ballon Man... Has fallen.",
    "You score is: %d" % score ,
    "",
    "Click the mouse to go back to the intro,", 
    "escape to quit..."
    )
    
    #add the instructions
    insLabels = []    
    for line in loss:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
    
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if the user presses the mouse down start the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                intro()
            #if the user enter the escape key they are done playing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        
        allSprites.update()
        allSprites.draw(screen)

        #display the loss message on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
    pygame.mouse.set_visible(True)
#end of gameOver method
    
#intro method runs the introduction to the game
def intro():
    #create variables to store sprites
    balloonMan = BalloonMan()
    skyBackground = SkyBackground()
    
    #load the balloon man and skybackground into the allSprites variable
    allSprites = pygame.sprite.OrderedUpdates(skyBackground, balloonMan)
    insFont = pygame.font.SysFont(None, 40)

    #set the instructions variable
    instructions = (
    "Balloon Man.",
    "Instructions:  Your are the Balloon Man,.",
    "Fly over coins to collect points,",
    "but be careful not to fly too close",    
    "to the flying birds. If the birds hit you lose ",
    "a life but never fear collecting balloons,",
    "will give you more health."
    "",
    "Good Luck!",
    "",
    "Click the mouse to start, escape to quit..."
    )

    #add the instructions
    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if the user presses the mouse down start the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                game()
            #if the user enter the escape key they are done playing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
    
        allSprites.update()
        allSprites.draw(screen)

        #display the instructions on the screen
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
    balloonMan.sndEngine.stop()
    pygame.mouse.set_visible(True)
#end of intro method

#Main method    
def main():
    intro()
#end of main method
if __name__ == "__main__":
    main()
            
