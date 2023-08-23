from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.base import runTouchApp
from kivy.uix.image import Image

Window.clearcolor = (89 / 255.0, 7 / 255.0, 45, 3)
Window.size = (400, 600)


class Name(App):
    def build(self):
        imj = Image(
            source='img3.png'
        )

        return imj


runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint:{'top':1}
    ActionView:
        ActionPrevious:
            title:'MY FIRST APP'
        ActionButton:
            text:'Home'
        ActionButton:
            text:'Back'
            color: 100/255.0,0,0.3,1

        ActionGroup:
            text:'More'
            color:.3,.6,0.2,1
            ActionButton:
                text:'EST'
                color:.4,.6,2,1
            ActionButton: 
                text:'FS'
                color:.4,.6,2,1
            ActionButton:
                text:'ENSA'
                color:.4,.6,2,1
            ActionButton: 
                text:'ENCG'
                color:.4,.6,2,1

'''))

if __name__ == '__main__':
    Name().run()
