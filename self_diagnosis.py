from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

# one type to show result
from kivy.uix.popup import Popup




#call kivy file
Builder.load_file("Main.kv")






# start screen
class ScreenOne(Screen):
   pass

# fill personal information
class ScreenTwo(Screen):
    pass

#option
class ScreenThree(Screen):
    pass


# select / write symptoms
class ScreenFour(Screen):
    pass


# display result
class ScreenFive(Screen):
    pass



screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="Screen_one"))
screen_manager.add_widget(ScreenTwo(name="Screen_two"))
screen_manager.add_widget(ScreenThree(name="Screen_three"))
screen_manager.add_widget(ScreenFour(name="Screen_Four"))


class KivyApp(App):
    def build(self):
        return screen_manager


samle = KivyApp()

samle.run()



