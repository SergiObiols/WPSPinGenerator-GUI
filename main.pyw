from Tkinter import *

#Creating the window with full-screen

def createWindow():
	window.destroy()
	mainWindow = Tk()
	mainWindow.resizable(0,0)
	width = mainWindow.winfo_screenwidth()
	height = mainWindow.winfo_screenheight()
	mainWindow.geometry(str(width) + "x" + str(height))
	mainWindow.title("WPSPinGenerator-GUI")


# Creating a windows to select network interface

window = Tk()
window.resizable(0,0)
width = window.winfo_screenwidth()/4
height = window.winfo_screenheight()/4
window.geometry(str(width) + "x" + str(height))
window.title("Select Network Interface")
buttonSelectNetwork = Button(window, text="Select",command=createWindow)
buttonSelectNetwork.pack(side=BOTTOM)
window.mainloop()





