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
snake=2
cola=0
serx, sery = 5, 10
colx, coly = 5-snake, 10
eatx, eaty = random.randint(0,nyC-1), random.randint(0,nyC-1)
matriz[serx, sery]=1
matriz[eatx, eaty]=2
key = 'righ'
key2= 'rigt'

pygame.display.flip()

def game_over():
     final = False
     if (serx < 0 or sery < 0):
          final = True
     if(serx > nxC-1 or sery > nyC-1):
          final = True
     return final
#BUCLE DE EJECUCION
while not game_over():

     newMatriz = np.copy(matriz)
     screen.fill(bg)
     time.sleep(0.1)

     newMatriz[eatx, eaty]=2
     
     ev = pygame.event.get()
     newMatriz[colx,coly]=2
     newMatriz[serx,sery]=1
     print(cola)
     #MOVIMIENTO DE LA SERPIENTE
     if (key == 'right'):
          serx+=1
          if(coly==sery):
               key2='right'
                
     if (key == 'left'):
          serx-=1
          if(coly==sery):
               key2='left'
               
     if (key == 'up'):
          sery-=1
          if(colx==serx):
               key2='up'
       
          
     if (key == 'down'):
          sery+=1
          if(colx==serx):
               key2='down'

     if(cola>=snake):
          newMatriz[colx,coly]=2
          if (key2 == 'right'):
               colx+=1
                     
          if (key2 == 'left'):
               colx-=1
                    
          if (key2 == 'up'):
               coly-=1
               
          if (key2 == 'down'):
               coly+=1
     else:
          cola+=1
     
     if((serx, sery)==(eatx, eaty)):
         newMatriz[eatx,eaty]=0
         eatx, eaty = random.randint(0,nyC-1), random.randint(0,nyC-1)
         snake+=1
         cola=0
     
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
                    pygame.draw.polygon(screen, (125,125,125), poly, 0)
               elif(newMatriz[x, y]==1):
                    pygame.draw.polygon(screen, (255,255,255), poly, 0)
               else:
                    pygame.draw.polygon(screen, (0,255,0), poly, 0)

     pygame.display.flip()
     matriz = np.copy(newMatriz)

     
