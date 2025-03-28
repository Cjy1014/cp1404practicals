from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilograms"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, text):
        miles = float(text) if text.replace(',', '').isdigit() else 0
        km = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{km:.5f}"

    def handle_increment(self, text, change):
        miles = int(text) + change if text.isdigit() else change
        self.root.ids.output_miles.text = str(miles)
        self.handle_convert(str(miles))


MilesConverterApp().run()



