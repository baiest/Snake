from model.Models import Cord, Direction
class Actions:
    def __init__(self):
        pass

    @staticmethod
    def move_snake(self, state):
        next_position = self._calc_position_snake(state)
        self._move_snake_to(state, next_position)
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

    def _move_snake_to(self, state, next_position):
        new_position = [next_position] + state.snake.posiciones[::1]
        state.snake.posiciones = new_position
        return state

        
