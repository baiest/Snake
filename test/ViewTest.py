from unittest import TestCase
import sys
sys.path.append('src')
from view.View import View
from model.Models import initial_state
from app import App

class ViewTest(TestCase):
    def test_render_view(self):
        """
        1 Renderizacion de la app
        """
        state = initial_state()
        view = View(App())
        view.start(state)
        view.render(state)