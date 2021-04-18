from unittest import TestCase
import sys
sys.path.append('src')
from view.View import View
from model.Models import initial_state
from app import App
from model.Models import Direction
from controller.Actions import Actions
from time import sleep

class ViewTest(TestCase):
    def setUp(self):
        self.state = initial_state()
        self.app = App()
        self.actions = Actions()

    def test_render_view(self):
        """
        1 Renderizacion de la app
        """
        view = View(self.app)
        view.start(self.state)
        view.render(self.state)

        self.assertIsNotNone(view.window)

    def test_render_move_snake(self):
        view = View(self.app)
        view.start(self.state)
        moves = 5
        while moves > 0:
            self.state = self.actions.move_snake(self.state)
            view.render(self.state)
            sleep(0.05)
            moves =- 1

        self.assertNotEqual(hash(self.state), hash(initial_state()))