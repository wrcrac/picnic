from tkinter import *
class window_one:
  def __init__(self):
    Button(main_window,text="Quit",command=self.quit) .grid()
    Button(main_window,text="Picnic Table",command=self.picnic) .grid()

  def quit(self):
    main_window.destroy()

  def picnic(self):
    canvas.create_oval(105,70,125,90,fill="red",outline="blue",width=5)
    canvas.create_oval(135,70,155,90,fill="red",outline="blue",width=5)
    canvas.create_oval(165,70,185,90,fill="red",outline="blue",width=5)
    canvas.create_oval(70,135,90,115,fill="red",outline="blue",width=5)
    canvas.create_oval(220,135,200,115,fill="red",outline="blue",width=5)
    canvas.create_oval(105,160,125,180,fill="red",outline="blue",width=5)
    canvas.create_oval(135,160,155,180,fill="red",outline="blue",width=5)
    canvas.create_oval(165,160,185,180,fill="red",outline="blue",width=5)
    canvas.create_rectangle(100,100,190,150,fill="pink",outline="green",width=5)
    canvas.update()

main_window = Tk()
canvas = Canvas(main_window,width=400,height=300,bg='lightgrey')
canvas.grid()

window_one()