from enum import Enum
class Tablero:
    def __init__(self, rows, cols):
        self.rows,self.cols = rows, cols

class Cord:
    def __init__(self, row, col):
        self.row, self.col = row, col

class Snake:
    def __init__(self, posiciones):
        self.posiciones = posiciones

class Food(Cord):
    def __init__(self, row, col):
        Cord.__init__(self, row, col)

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
    

def initial_state():
    return State(
        Tablero(10, 10),
        Snake([Cord(5,5), Cord(4,5)]),
        Food(6, 6),
        Direction.RIGHT)