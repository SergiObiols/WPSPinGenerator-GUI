#Creating the window with full-screen

def createWindow(networkInterface):
	window.destroy()
	mainWindow = Tk()
	mainWindow.resizable(0,0)
	width = mainWindow.winfo_screenwidth()
	height = mainWindow.winfo_screenheight()
	mainWindow.geometry(str(width) + "x" + str(height))
	mainWindow.title("WPSPinGenerator-GUI")
	airmonInterface = os.popen("airmon-ng start "+networkInterface+" | awk '{print $5}' | tail -n 2").read()[:-3]
	print(airmonInterface)
