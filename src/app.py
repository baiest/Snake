from model.Models import *
from controller.Actions import *
from view.View import *
from time import sleep
import pygame
class App:
    def __init__(self):
        self.state = initial_state()
        pass
        
    def start(self):
        print('Inicia el Juego')
        view = View(self)
        view.start(self.state)
        while True:
            self.state = Actions.move_snake(Actions(), self.state)
            view.render(self.state)
            sleep(0.1)
            
if __name__ == '__main__':
    app = App()
    app.start()