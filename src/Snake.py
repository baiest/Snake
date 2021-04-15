from pynput.keyboard import Key, Listener
import numpy as np
import time
import pygame
from pygame.locals import *
import random

pygame.init()
size= (700, 500)
screen = pygame.display.set_mode(size)

bg = (0,0,0)
screen.fill(bg)

nxC, nyC = 50, 50

dimX= 500 // nxC
dimY= size[1] // nyC

myfont = pygame.font.SysFont("arial black", 28)
matriz= np.zeros((nxC , nyC))
snake = 2
point = 0
serx, sery = 5, 10
eatx, eaty = random.randint(0,nyC-1), random.randint(0,nyC-1)
matriz[serx, sery]=1
colax, colay = 5, 10
key = 'right'
keyCola = 'right'
direc = []
game_over = False
running = True
flag = True
vel = 0.02
boost = 5
esperaMsg =  500

i=1 #Retraso para la cola

pygame.display.flip()

#BUCLE DE EJECUCION
while not game_over:
     """
     if snake == boost:
          vel= vel / 2
          boost += boost
     """
     newMatriz = np.copy(matriz)
     screen.fill(bg)
     time.sleep(vel)

     newMatriz[eatx, eaty]=2
     
     ev = pygame.event.get()
     
     if running:     
          if i > snake:
               keyCola = direc[0]
               if (keyCola == 'right'):
                    newMatriz[colax, colay]=0
                    colax+=1
               
               if ( keyCola == 'left'):
                    newMatriz[colax, colay]=0
                    colax-=1
                         
               if (keyCola == 'up'):
                    newMatriz[colax, colay]=0
                    colay-=1
                    
               if (keyCola == 'down'):
                    newMatriz[colax, colay]=0
                    colay+=1

               direc.pop(0)
          else:
               i+=1
          
          #MOVIMIENTO DE LA SERPIENTE
          if (key == 'right'):
               newMatriz[serx,sery]=1
               serx+=1

          if (key == 'left'):
               newMatriz[serx,sery]=1
               serx-=1
                    
          if (key == 'up'):
               newMatriz[serx,sery]=1
               sery-=1
               
          if (key == 'down'):
               newMatriz[serx,sery]=1
               sery+=1
          try:
               if newMatriz[serx,sery]==1:
                    game_over = True
          except IndexError:
               pass
          direc.append(key)
     
     if serx > nxC-1:
          serx = 0
     if colax > nxC-1:
          colax = 0
     if sery > nyC-1:
          sery = 0
     if colay > nyC-1:
          colay = 0

     if serx < 0:
          serx = nxC-1
     if colax < 0:
          colax = nxC-1
     if sery < 0:
          sery = nyC-1
     if colay < 0:
          colay = nyC-1
     
     if((serx, sery)==(eatx, eaty)):
          newMatriz[eatx,eaty]=0
          while True:
              eatx, eaty = random.randint(0,nyC-1), random.randint(0,nyC-1)
              if (matriz[eatx,eaty]!=1):
                   break
          snake+=1 
          point+= 1
     for event in ev:
          if event.type is pygame.QUIT:
                quit()
                break
     
          if (event.type is pygame.KEYDOWN):
               newKey = pygame.key.name(event.key)
               if newKey == 'right' and key !='left':
                    key = newKey
               if newKey == 'up' and key !='down':
                    key = newKey
               if newKey == 'left' and key !='right':
                    key = newKey
               if newKey == 'down' and key !='up':
                    key = newKey

               if newKey not in ['right', 'left', 'up', 'down']:
                    running = False
               else:
                    running = True

     for y in range(0, nyC):
          for x in range (0, nxC):
                              
               poly = [((x)   * dimX,   y     * dimY),
                       ((x+1) * dimX,   y     * dimY),
                       ((x+1) * dimX,   (y+1) * dimY),
                       ((x)   * dimX,   (y+1) * dimY)]
               if(newMatriz[x, y]==1):
                    pygame.draw.polygon(screen, (255,255,255), poly, 0)
               if(newMatriz[x, y]==2):
                    pygame.draw.polygon(screen, (0,255,0), poly, 0)
     
     pygame.draw.line(screen, (0,0, 150), (500, 0), (500, 500), 2)
     pause = myfont.render("Any button:", 1, (255,255,255))
     mspause = mecontrol = myfont.render("pause", 1, (255,255,255))
     mecontrol = myfont.render("Move snake:", 1, (255,255,255))
     control = myfont.render("←  →", 1, (255,255,255))
     control2 = myfont.render("↑", 1, (255,255,255))
     control3 = myfont.render("↓", 1, (255,255,255))
     screen.blit(pause, (515, 170))
     screen.blit(mspause, (562, 210))
     screen.blit(control, (567, 385))
     screen.blit(control2, (600, 365))
     screen.blit(control3, (600,410))
     screen.blit(mecontrol, (505,320))
     
     if snake>2:
          label = myfont.render("Score:", 1, (255,255,255))
          score = myfont.render( str(point), 1, (255,255,255))
          screen.blit(label, (560, 30))
          screen.blit(score, (590, 100))

     else:
          label = myfont.render("Hello!", 1, (255,255,255))
          screen.blit(label, (560, 30))

     pygame.display.flip()
     matriz = np.copy(newMatriz)