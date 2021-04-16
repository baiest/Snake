import pygame
from pygame.locals import *
from time import sleep
from model.Models import Direction
from pynput.keyboard import Key, Listener

class View:
    color_tablero = (0, 0, 0)
    color_snake = (255,255,255)
    color_food = (0,0,255)

    def __init__(self, app):
        self._pixel = 10
        self.app = app
    
    def start(self, state):
        size = (
            self._pixel * state.tablero.rows + (self._pixel * state.tablero.rows) // 3,
            self._pixel * state.tablero.cols
        )
        self.window = pygame.display.set_mode(size)
        self.window.fill(self.color_tablero)
    
    def leer(self):
        with Listener(
            on_press=self._key_event) as listener:
            listener.join()

    def render(self, state):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                self._key_event(Key.esc)
                quit()
                
        self.window.fill(self.color_tablero)
        self._render_snake(state.snake.posiciones)
        self._render_food(state.food)
        pygame.display.flip()
    
    def _render_snake(self, snake):
        for cord in snake:
            pygame.draw.polygon(self.window, self.color_snake,  self._cuadrado(cord.row, cord.col), 0)
        

    def _render_food(self, cord):
        pygame.draw.polygon(self.window, self.color_food,  self._cuadrado(cord.row, cord.col), 0)
    
    def _cuadrado(self, y, x):
        return [((x)   * self._pixel,   (y+1) * self._pixel),
                ((x+1) * self._pixel,   (y+1) * self._pixel),
                ((x+1) * self._pixel,   y     * self._pixel),
                ((x)   * self._pixel,   y     * self._pixel)]
        
    def _key_event(self, key):
        print(f"{key}")
        if(key is Key.esc):
            quit()

        if(key == Key.up):
            print("up")
            self.app.send_action(Direction.UP)
        if(key == Key.down):
            self.app.send_action(Direction.DOWN)
        if(key == Key.right):
            self.app.send_action(Direction.RIGHT)
        if(key == Key.left):
            self.app.send_action(Direction.LEFT)