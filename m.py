import winsound
import threading
from tkinter import *

root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()

def playsound():
    winsound.PlaySound("sound/TB7L64W-winning.wav", winsound.SND_ALIAS)

threadsound = threading.Thread(target=playsound)

def printtext():
    threadsound.start()
    print("Hi")

button = Button(root, text=("button"), command=printtext)
button.pack()    

root.mainloop()