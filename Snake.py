from tkinter import *
from pynput.keyboard import Key, Listener
import numpy as np
import os
import time
import pygame
import random

pygame.init()

size= (500, 500)
screen = pygame.display.set_mode(size)

bg= 25,25, 25

screen.fill(bg)

nxC, nyC = 50, 50

dimX= size[0] // nxC
dimY= size[1] // nyC

matriz= np.zeros((nxC , nyC))
snake = 2
serx, sery = 5, 10
eatx, eaty = random.randint(0,nyC-1), random.randint(0,nyC-1)
matriz[serx, sery]=1
colax, colay = 5, 10
key = 'right'
keyCola = 'right'
direc = []
game_over = False

i=1 #Retraso para la cola

pygame.display.flip()

#BUCLE DE EJECUCION
while not game_over:
     
     newMatriz = np.copy(matriz)
     screen.fill(bg)
     time.sleep(0.1)

     newMatriz[eatx, eaty]=2
     
     ev = pygame.event.get()

     if serx >= nxC:
          serx = 0
     if colax >= nxC:
          colax = 0
     if sery >= nyC:
          sery = 0
     if colay >= nyC:
          colay = 0
          
     if i > snake:
          keyCola = direc[0]
          if (keyCola == 'right'):
               newMatriz[colax, colay]=0
               colax+=1

          if (keyCola == 'left'):
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

     direc.append(key)

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
         eatx, eaty = random.randint(0,nyC-1), random.randint(0,nyC-1)
         snake+=1
         print(snake)
     
     for event in ev:
          if event.type is pygame.QUIT:
                quit()
                break
     
          if (event.type is pygame.KEYDOWN):
               key = pygame.key.name(event.key)
                    
     for y in range(0, nyC):
          for x in range (0, nxC):
                              
               poly = [((x)   * dimX,   y     * dimY),
                       ((x+1) * dimX,   y     * dimY),
                       ((x+1) * dimX,   (y+1) * dimY),
                       ((x)   * dimX,   (y+1) * dimY)]
               if (newMatriz[x, y]==0):
                    pygame.draw.polygon(screen, (125,125,125), poly, 1)
               elif(newMatriz[x, y]==1):
                    pygame.draw.polygon(screen, (255,255,255), poly, 0)
               else:
                    pygame.draw.polygon(screen, (0,255,0), poly, 0)

     pygame.display.flip()
     matriz = np.copy(newMatriz)

     
