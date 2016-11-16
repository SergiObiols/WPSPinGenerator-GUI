execfile("src/__init__.py")

# Method to get all the networks interfaces availables at the system

def allInterfaces():
	iw = subprocess.Popen('iw dev'.split(), stdout=subprocess.PIPE)
	args = shlex.split("awk '$1==\"Interface\"{print $2}'")
	awk = subprocess.Popen(args, stdin=iw.stdout, stdout=subprocess.PIPE)
	return iter(awk.stdout.readline, b'')

# Creating a windows to select network interface

window = Tk()
window.resizable(0,0)
width = window.winfo_screenwidth()/4
height = window.winfo_screenheight()/4
window.geometry(str(width) + "x" + str(height))
window.title("Select Network Interface")
scroll = Scrollbar(window)
networkList = Listbox(window, height = 10, width = 80, selectmode = SINGLE)
networkList.config(yscrollcommand = scroll.set)
scroll.config(command = networkList.yview)

#Insert network interface in list

interface_list = allInterfaces()
for interface in interface_list:
		networkList.insert(END,interface[:-1])
networkList.select_set(0)
networkList.pack()

# Creating the button and the listbox to select network interface
buttonSelectNetwork = Button(window, text="Select",command=lambda: createWindow(networkList.get(networkList.curselection()))).pack()

window.mainloop()
