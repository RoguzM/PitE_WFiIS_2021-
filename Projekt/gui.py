# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.config import Config
import tkinter as tk
from tkinter import filedialog as fd 
# import cv2
#from ... import ...
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

Builder.load_file('appgui.kv')

class guiapp(Widget):
    pass

    name = ""
    image = ""

    def filebrowser(self):
        roottk = tk.Tk()
        roottk.withdraw()
        filepath = fd.askopenfilename(initialdir = "./",title = "ML: Uploading custom file",filetypes = (("jpeg, png files","*.jpg *.png"),("all files","*.*"))) 
        # print(name)
        # image = cv2.imread(filepath)
        # rozmiar do przeskalowania
        # image = cv2.resize(image, (96, 96), interpolation=cv2.INTER_LINEAR)
        self.img.source = filepath
        
    def recon(self):
        x = 2
        # answer = function(image)
        # x = answer.split(";")
        # self.recognised_text.text = x[0]
        # self.accuracy.text = x[1]

class Application(App):
    def build(self):
        self.title = 'Python Alvaaros :D'
        
        
        return guiapp()
    

if __name__ == "__main__":
    Application().run()
    
    