from unittest import TestCase
import sys
sys.path.append('src')
from model.Models import *

class InicializacionTest(TestCase):
    def test_crear_estado_inicial(self):
        """
        Estado inicial contenga todos sus valores
        """
        state = initial_state()
        attr_state = state.__dict__.values()
        tipos_atributos = [Tablero, Snake, Food, Direction, bool]
        existe_atributo = [type(attr) in tipos_atributos for attr in attr_state]
        result = not False in existe_atributo
        
        self.assertTrue(result)