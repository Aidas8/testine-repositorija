from tkinter import *
langas = Tk()

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

meniu.add_cascade(label="meniu", menu=submeniu)
submeniu.add_command(label="pirmas")
submeniu.add_command(label="antras")
langas.mainloop()
