import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)


block_color = white

fox_width = 40

dodged = 0


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Polowanie na lisa')
clock = pygame.time.Clock()

foxImg = pygame.image.load('C:/Pictures/fox.png')
arrowImg = pygame.image.load('C:/Pictures/arrow.png')
backgroundImg = pygame.image.load('C:/Pictures/background.png')
shieldImg = pygame.image.load('C:/Pictures/grass.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Suma uników: "+str(count), True, black)
    gameDisplay.blit(text,(640,10))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
def shield(x,y):
    gameDisplay.blit(shieldImg,(x,y))
def fox(x,y):
    gameDisplay.blit(foxImg,(x,y))
def arrow(x,y):
    gameDisplay.blit(arrowImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def text_objects2(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,text2):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    normalText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextSurf2, TextRect2 = text_objects2(text2, normalText)
    TextRect.center = ((display_width/2),(display_height/2))
    TextRect2.center = ((display_width/2),(display_height/2+50))
    gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(TextSurf2, TextRect2)

    pygame.display.update()

    time.sleep(10)

    game_loop()
    
    

def died(dodged):
    message_display('Umarłeś', 'Wynik: ' + str(dodged) )
    
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1
    shieldOn = 0

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:           
                    x_change = -5
                    shieldOn = 0
                    print('shieldOff')
                    
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    shieldOn = 1
                    print('shieldOn')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
            
     
        x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        fox(x,y)
        if shieldOn == 1:
            shield(x,y)
        arrow(thing_startx,thing_starty)

        
        thing_starty += thing_speed
        things_dodged(dodged)
        gameDisplay.blit(backgroundImg,(0,0))

        if shieldOn == 0:
            if x > display_width - fox_width or x < 0:
                died(dodged)

            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0,display_width)
                dodged += 1
                thing_speed += 1
                thing_width += (dodged * 1.2)

            if y < thing_starty+thing_height:
                if x > thing_startx and x < thing_startx + thing_width or x+fox_width > thing_startx and x + fox_width < thing_startx+thing_width:
                    print('x crossover')
                    died(dodged)
        
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()