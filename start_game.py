import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
frame = tk.Frame(window, width=500, height=500)
frame.pack()

canvas = tk.Canvas(frame, width=400, height=400)
canvas.pack()

oval = canvas.create_oval(10,10,90,90,fill="white")

def move_():
    canvas.move(oval,10,0)

def move_to():
    canvas.moveto(oval,10,10)

buttonMove= tk.Button(frame,text="Move",command=move_)
buttonMove.pack()

buttonMoveTo= tk.Button(frame,text="Move To",command=move_to)
buttonMoveTo.pack()

window.mainloop()