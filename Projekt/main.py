# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.config import Config
from kivy.graphics import *
from kivy.core.image import Image
import tkinter as tk
from tkinter import filedialog as fd 
import cv2
from segmentacja import *

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

Builder.load_file('appgui.kv')


class guiapp(Widget):
    pass

    image = ""
    filepath = ""
  

    def filebrowser(self):
        roottk = tk.Tk()
        roottk.withdraw()
        # self.img.canvas.clear()
        self.filepath = fd.askopenfilename(initialdir = "./",title = "ML: Uploading custom file",filetypes = (("jpeg, png files","*.jpg *.png"),("all files","*.*"))) 
        self.image = cv2.imread(self.filepath) 
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.img.source = self.filepath
        # texture = Image(self.filepath).texture
        # with self.canvas:
        #     Color(1, 1, 1, 1)
        #     Rectangle(texture = texture, pos=self.img.pos, size=self.img.size)
        
    def kozakfunkcja(self):
        answer = predict_digit_letter(self.image)
        x = answer.split(";")
        conv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.recognised_text.text = conv[int(x[0])]
        self.accuracy.text = x[1]

    def kozakclear(self):
        self.recognised_text.text = "Python Alvaaros"
        self.accuracy.text = "1.000"
        self.filepath = "pyton.jpg"
        self.img.source = self.filepath
        # self.img.canvas.clear()
        # texture = Texture.create(size=(640, 480), colorfmt='rgba')
        # with self.img.canvas:
        #     Rectangle(texture=texture, pos=self.img.pos, size=self.img.size)
        
    # def on_touch_down(self, touch):
    #     self.img.canvas.add(Color(rgb=(0, 0, 0)))
    #     touch.ud['line'] = Line(points=(touch.x, touch.y))
    #     self.img.canvas.add(touch.ud['line'])
    #     super().on_touch_down(touch)

    # def on_touch_move(self, touch):
    #     touch.ud['line'].points += [touch.x, touch.y]
    #     super().on_touch_move(touch)
        
        
class Application(App):
    def build(self):
        self.title = 'Python Alvaaros :D'
        
        
        return guiapp()
    

if __name__ == "__main__":
    Application().run()
    
    