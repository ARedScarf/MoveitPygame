import pygame,time,os,tkinter
start = False
bg = 0

pygame.init()
img = pygame.image.load('planet.png')
station = pygame.image.load('station.png')
ship = pygame.image.load('ship.png')
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
#screen = pygame.display.set_mode((400, 300))
BLACK = (  0,   0,   0)
done = False
is_blue = True
x = 30
y = 30
DISPLAYSURF.blit(img,(0,0))

def changeShip():
        global ship
        ship = pygame.image.load('Spacman.png')
        DISPLAYSURF.blit(ship,(x,y))
        
        
while not done:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            time.sleep(0.05)
            DISPLAYSURF.blit(img,(0,0))
            DISPLAYSURF.blit(ship,(x,y))
            DISPLAYSURF.blit(station,(100,100))
            y -= 3
        if pressed[pygame.K_DOWN]:
            time.sleep(0.05)
            DISPLAYSURF.blit(img,(0,0))
            DISPLAYSURF.blit(ship,(x,y))
            DISPLAYSURF.blit(station,(100,100))
            
            y += 3
        if pressed[pygame.K_LEFT]:
            time.sleep(0.05)
            DISPLAYSURF.blit(img,(0,0))
            DISPLAYSURF.blit(ship,(x,y))
            DISPLAYSURF.blit(station,(100,100))
            x -= 3
        if pressed[pygame.K_RIGHT]:
            time.sleep(0.05)
            DISPLAYSURF.blit(img,(0,0))
            DISPLAYSURF.blit(ship,(x,y))
            DISPLAYSURF.blit(station,(100,100))
            x += 3
            
        if x > 100 and x < 220:
                if y > 100 and y < 200:
                        #changeBG()
                        
                        
                        #station = pygame.image.load('station.png')
                        #ship = pygame.image.load('ship.png')
                        if bg == 0:
                             img = pygame.image.load('station1.png')
                             ###station = pygame.image.load('station.png')
                             #ship = pygame.image.load('ship.png')
                             DISPLAYSURF.blit(img,(0,0))
                             bg += 1
                             changeShip()
                        if bg == 2:
                             img2 = pygame.image.load('station.png')
                             DISPLAYSURF.blit(img2,(0,0))
                             print('Allo')
                             bg += 1

        
        pygame.display.flip()
