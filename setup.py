execfile("src/__init__.py")

# Method to get all the networks interfaces availables at the system

def allInterfaces():
	iw = subprocess.Popen('iw dev'.split(), stdout=subprocess.PIPE)
	args = shlex.split("awk '$1==\"Interface\"{print $2}'")
	awk = subprocess.Popen(args, stdin=iw.stdout, stdout=subprocess.PIPE)
	return iter(awk.stdout.readline, b'')

# Method that let us to center the window on the middle of the screen

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

# Creating a windows to select network interface

window = Tk()
window.resizable(0,0)
width = window.winfo_screenwidth()/4
height = window.winfo_screenheight()/4
window.geometry(str(width) + "x" + str(height))
window.title("WPSPinGenerator-GUI")
window.configure(bg='#A9E5BB')
center(window)
scroll = Scrollbar(window)

#Creating the frame to add the diferents objects in to the window

frameWindow = Frame (window)
frameWindow.pack(side = TOP)
frameWindow.configure(bg='#A9E5BB')

labelWindow = Label(frameWindow,text="Welcome to WPSPinGenerator-GUI", font=("Helvetica", 12), bg='#A9E5BB')
labelWindow.pack(side=TOP)

labelWindow2 = Label(frameWindow,text="Available Networks Interfaces", font=("Helvetica", 10), pady=10, bg='#A9E5BB')
labelWindow2.pack(side=TOP)

#Insert network interface in list

networkList = Listbox(frameWindow, height = 5, width = 40, selectmode = SINGLE, font=("Helvetica", 10))
networkList.config(yscrollcommand = scroll.set)
scroll.config(command = networkList.yview)
interface_list = allInterfaces()
for interface in interface_list:
		networkList.insert(END,interface[:-1])
networkList.select_set(0)
networkList.pack()

# Creating the button and the listbox to select network interface

buttonSelectNetwork = Button(window, text="Select Network Interface", font=("Helvetica", 10), bg='#2D1E2F', fg='white')
buttonSelectNetwork.config(activebackground='#2D1E2F', activeforeground='white', command=lambda: createWindow(networkList.get(networkList.curselection())))
buttonSelectNetwork.pack(side=BOTTOM)

window.mainloop()
