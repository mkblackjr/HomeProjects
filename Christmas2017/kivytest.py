import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer

class MyW(Widget):

    def __init__(self, **kwargs):
        super(MyW, self).__init__(**kwargs)
        player= VideoPlayer( source='Christmas2017.mpg',state='play', options={'allow_stretch': True}, size=(600,600))
        self.add_widget(player)

class e5App(App):

    def build(self):
       return MyW()

e5App().run()