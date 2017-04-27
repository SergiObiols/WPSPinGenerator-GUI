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
	mainWindow.configure(bg='#A9E5BB')
	width = mainWindow.winfo_screenwidth()
	height = mainWindow.winfo_screenheight()
	mainWindow.geometry(str(width/2) + "x" + str(height/2))
	mainWindow.title("WPSPinGenerator-GUI")
	center(mainWindow)

	frameWindow = Frame (mainWindow)
	frameWindow.pack(side = LEFT)
	frameWindow.configure(bg='#A9E5BB')

	# Creating the button to scan all the networks interfaces

	buttonScan = Button(mainWindow, text="Scan Networks", font=("Helvetica", 10), bg='#2D1E2F', fg='white',height=1, width=15, command= lambda: scanNetworks(airmonInterface))
	buttonScan.config(activebackground='#2D1E2F', activeforeground='white')
	buttonScan.place(relx=0.95, y=50,anchor="e")

	# Creating the button show all the networks interfaces storaged on the system

	buttonNetwork = Button(mainWindow, text="Storaged Networks", font=("Helvetica", 10), bg='#2D1E2F', fg='white', height=1, width=15)
	buttonNetwork.config(activebackground='#2D1E2F', activeforeground='white')
	buttonNetwork.place(relx=0.95, y=125,anchor="e")

	buttonAttack = Button(mainWindow, text="Attack", font=("Helvetica", 10), bg='#2D1E2F', fg='white', height=1, width=15)
	buttonAttack.config(activebackground='#2D1E2F', activeforeground='white')
	buttonAttack.place(relx=0.95, y=200,anchor="e")

	buttonInterface = Button(mainWindow, text="Change NIC", font=("Helvetica", 10), bg='#2D1E2F', fg='white', height=1, width=15)
	buttonInterface.config(activebackground='#2D1E2F', activeforeground='white')
	buttonInterface.place(relx=0.95, y=275,anchor="e")

	os.popen("airmon-ng start " + networkInterface)
	airmonInterface = os.popen("ifconfig | grep mon | awk '{print $1}' | sed 's/:$//'").read()
	print airmonInterface

	networksList = Listbox(frameWindow, height=26, width=100, selectmode=SINGLE, font=("Helvetica", 10))
	networksList.config(yscrollcommand=scroll.set)
	networksList.pack()

def scanNetworks(airmonInterface):

	networksLists = subprocess.Popen("airodump-ng " + airmonInterface, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
	time.sleep(30)
	os.killpg(os.getpgid(networksLists.pid), signal.SIGTERM)

	print "List networks //TODO"