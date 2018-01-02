######################################################################
###################### Shalini_Christmas_UI.py #######################
######################################################################

                                #
                               ###
                              #####
                             #######
                            #########
                           ###########
                          #############
                               ###

######################################################################
############################# IMPORTS ################################
######################################################################

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.image import AsyncImage

filepath = "Users/mblackjr/Documents/Professional/MichiganAerospace/GithubRepositories/MVS/Meteora.ttf"
print(filepath)
# from kivy.core.text import LabelBase
# LabelBase.register(name="Meteora",fn_regular=filepath)

######################################################################
############################# SETTINGS ###############################
######################################################################

from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')

######################################################################
############################ GUI ELEMENTS ############################
######################################################################

class InitialScreen(Screen):
	pass


class MainScreen(Screen):
	pass


class GUI(ScreenManager):
	pass

######################################################################
####################### APPLICATION DEFINITION #######################
######################################################################

class XmasAdventure_App(App):
	# Class Variables

	def build(self):
		self._gui = GUI()
		return self._gui

	def on_start(self):
		pass

	def on_stop(self):
		pass


######################################################################
########################### Code Execution ###########################
######################################################################

if __name__ == "__main__":
	XmasAdventure_App().run()


