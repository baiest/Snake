import pygame
from time import sleep
class View:
    color_tablero = (0, 0, 0)
    color_snake = (255,255,255)
    color_food = (0,0,255)

    def __init__(self, app):
        self._pixel = 40
        self.app = app
    
    def start(self, state):
        size = (
            self._pixel * state.tablero.rows + (self._pixel * state.tablero.rows) // 3,
            self._pixel * state.tablero.cols
        )
        self.window = pygame.display.set_mode(size)
        self.window.fill(self.color_tablero)

    def render(self, state):
        for event in pygame.event.get():
            self._key_event(event)
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
        
    def _key_event(self, event):
        dic_event = {
            pygame.QUIT.value: quit()
        }