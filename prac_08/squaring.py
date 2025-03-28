"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Jingyang Cai
Started 28/3/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Jingyang Cai'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 150)
        self.title = "Square Number"
        return Builder.load_file('squaring.kv')

    def handle_calculate(self, value):
        """ handle calculation, output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"


SquareNumberApp().run()