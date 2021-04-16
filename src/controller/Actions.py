from model.Models import Cord, Direction
import random
class Actions:
    def __init__(self):
        pass

    def move_snake(self, state):
        next_direction = state.direction
        next_position = self._calc_position_snake(state)
        if ((state.food.row == next_position.row) 
        and (state.food.col == next_position.col)):
            self._crecer_snake(state, next_position)
            state = self._generar_food(state)
        elif (self._movimiento_valido(state, next_direction)):
            self._move_snake_to(state, next_position)
        return state

    def _crecer_snake(self, state, next_position):
        new_snake = [next_position] + state.snake.posiciones
        state.snake.posiciones = new_snake
        return state

    def _generar_food(self, state):
        random.seed()
        food_col = random.randint(0, state.tablero.cols)
        random.seed()
        food_row = random.randint(0, state.tablero.rows)

        state.food = Cord(food_row, food_col)
        return state

    def _calc_position_snake(self, state):
        current_position = state.snake.posiciones[0]

        dic_direction = {
            Direction.UP.value: Cord(
                current_position.row - 1,
                current_position.col),
            Direction.DOWN.value: Cord(
                current_position.row + 1,
                current_position.col),
            Direction.RIGHT.value: Cord(
                current_position.row,
                current_position.col + 1),
            Direction.LEFT.value: Cord(
                current_position.row,
                current_position.col - 1)
        }
        current_position = dic_direction[state.direction.value]
        return current_position
    
    def change_direction(self, state, direction):
        if (self._movimiento_valido(state, direction)):
            state.direction = direction
        return state

    def _move_snake_to(self, state, next_position):
        new_position = [next_position] + state.snake.posiciones[:-1]
        state.snake.posiciones = new_position
        return state

    def _movimiento_valido(self, state, direction):
        if (state.direction == Direction.UP):
            if(direction != Direction.DOWN):
                return True
        elif (state.direction == Direction.DOWN):
            if(direction != Direction.UP):
                return True
        elif (state.direction == Direction.RIGHT):
            if(direction != Direction.LEFT):
                return True
        elif (state.direction == Direction.LEFT):
            if(direction != Direction.RIGHT):
                return True
        
        return False