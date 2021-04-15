from unittest import TestCase
from model.Models import *
class InicializacionTest(TestCase):
    def test_crear_estado_inicial(self):
        state = State(
            Tablero(10,10),
            Snake([Cord(5,5), Cord(4,5)]),
            Food(Cord(6,6)),
            Direction.RIGHT
        )
