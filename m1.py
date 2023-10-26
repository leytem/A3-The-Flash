from tkinter import *
from PIL import ImageTk, Image
import winsound

def play():
    winsound.PlaySound('piglevelwin2mp3-14800.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

window = Tk()
window.geometry('700x500')

frame = Frame(window, width=1000, height=700)
frame.pack()

canvas = Canvas(frame, width=700, height=500)
canvas.pack()
# Create anoverlay image on the canvas
def button_clicked():
    print("Button clicked!")
button_back = Button(frame, text="level two", command=button_clicked, bg='red', border=10,font=('BLOODY TYPE PERSONAL USE', 30))
button_back.pack()
button_back.place(x=240, y=150, width=240,height=120)
play()
window.mainloop()