from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class HelperWidgetCreator:
	def __init__(self, teks="", font_size=18):
		self.teks = teks
		self.font_size = font_size
		
	def frame(self, orientation="vertical", padding=10, spacing=10, size_hint_y=1):
		return BoxLayout(
			orientation=orientation,
			padding=padding,
			spacing=spacing,
			size_hint_y=size_hint_y
		)
	

class MyApp(App):
	def __init__(self, helper, **kwargs):
		super().__init__(**kwargs)
		self.setup = helper
		
	def build(self):
		self.title = "Aplikasi keuangan"
		Window.size = (360,640)
		Window.clearcolor = (1,1,1,1)
		
		self.main_layout = self.setup.frame("vertical")
		return self.main_layout
		
if __name__ == "__main__":
	myApp = MyApp(HelperWidgetCreator()) 
	myApp.run()