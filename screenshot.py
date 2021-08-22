import pyautogui
import random
from tkinter import *
number = 0

def ss():
 global number
 myScreenshot = pyautogui.screenshot()
 myScreenshot.save(f'screenshot{number}.png')
 number += 1


tk = Tk()
tk.config(height = 20, width = 20)




clickthing =  Button(tk, text="Take Screenshot",  command=ss,)
clickthing.config(height = 20, width = 20)
clickthing.grid(row = 0, column = 3, padx = 100)

clickthing.pack()
tk.mainloop()
