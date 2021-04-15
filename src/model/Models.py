from enum import Enum
class Tablero:
    def __init__(self, rows, cols):
        self.rows,self.cols = rows, cols

class Cord:
    def __init__(self, row, col):
        self.roe, self.col = row, col

class Snake:
    def __init__(self, posiciones):
        self.posiciones = posiciones

class Food(Cord):
    def __init__(self, row, col):
        super()

class Direction(Enum):
    RIGHT = 'right'
    LEFT = 'left'
    UP = 'up'
    DOWN = 'down'    

class State:
    def __init__(self, tablero, snake, food, direction):
        self.tablero = tablero
        self.snake = snake
        self.food = food
        self.direction = direction
        
    


