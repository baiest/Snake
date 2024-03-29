from model.Models import *
from controller.Actions import *
from view.View import *
from time import sleep

class App:
    
    def __init__(self):
        self.state = initial_state()
        self.actions = Actions()
        pass
        
    def start(self):
        print('Inicia el Juego')
        view = View(self)
        view.start(self.state)
        while not self.state.game_over:
            self.state = self.actions.move_snake(self.state)
            view.render(self.state)
            sleep(0.05)

    def send_action(self, direction):
        self.state = self.actions.change_direction(self.state, direction)
        return self.state
if __name__ == '__main__':
    app = App()
    app.start()