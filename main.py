from Tkinter import *

#Creating the window with full-screen

window = Tk()
window.resizable(0,0)
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(str(width) + "x" + str(height))
window.title("WPSPinGenerator-GUI")
window.mainloop()
