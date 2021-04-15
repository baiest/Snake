from model.Models import *
from view.View import *
from time import sleep
import threading

class App:
    def __init__(self):
        self.state = initial_state()
        pass
        
    def start(self):
        print('Inicia el Juego')
        view = View(self)
        hilo_render = threading.Thread(name='render', target=self._init_hilo, args=(view,))
        view.start(self.state)
        hilo_render.start()

    def _init_hilo(self, view):
        view.render(self.state)
        sleep(3)
if __name__ == '__main__':
    app = App()
    app.start()