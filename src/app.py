from model.Models import *
class App:
    def __init__(self):
        pass
        
    def start(self):
        print('Inicia el Juego')
        state = State(
            Tablero(10,10),
            Snake([Cord(5,5), Cord(4,5)]),
            Food(6,6),
            Direction.RIGHT
        )

if __name__ == '__main__':
    app = App()
    app.start()