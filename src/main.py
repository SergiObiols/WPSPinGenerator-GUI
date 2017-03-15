#  Method that let us to center the window on the middle of the screen

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

#Creating the window with full-screen

def createWindow(networkInterface):
	window.destroy()
	mainWindow = Tk()
	mainWindow.resizable(0,0)
	width = mainWindow.winfo_screenwidth()
	height = mainWindow.winfo_screenheight()
	mainWindow.geometry(str(width/2) + "x" + str(height/2))
	mainWindow.title("WPSPinGenerator-GUI")
	center(mainWindow)
	airmonInterface = os.popen("airmon-ng start "+networkInterface+" | grep monitor | awk '{print $5}'").read()[:-2]
	print(airmonInterface)
