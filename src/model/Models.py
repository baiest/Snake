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
    def __init__(self, tablero, snake, food, direction, game_over=False):
        self.tablero = tablero
        self.snake = snake
        self.food = food
        self.direction = direction
        self.game_over = game_over
    

def initial_state():
    return State(
        Tablero(30, 30),
        Snake([Cord(2,5), Cord(4,5), Cord(3,5), Cord(2,5), Cord(1,5)]),
        Food(6, 6),
        Direction.RIGHT)