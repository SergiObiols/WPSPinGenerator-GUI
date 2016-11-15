from Tkinter import *
import socket
import fcntl
import struct
import array


#Creating the window with full-screen

def createWindow():
	window.destroy()
	mainWindow = Tk()
	mainWindow.resizable(0,0)
	width = mainWindow.winfo_screenwidth()
	height = mainWindow.winfo_screenheight()
	mainWindow.geometry(str(width) + "x" + str(height))
	mainWindow.title("WPSPinGenerator-GUI")
	
# Method to get all the networks interfaces availables at the system

def allInterfaces():
	max_possible = 128  # arbitrary. raise if needed.
	bytes = max_possible * 32
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	names = array.array('B', '\0' * bytes)
	outbytes = struct.unpack('iL', fcntl.ioctl(s.fileno(),0x8912,struct.pack('iL', bytes, names.buffer_info()[0])))[0]
	namestr = names.tostring()
	lst = []
	for i in range(0, outbytes, 40):
		name = namestr[i:i+16].split('\0', 1)[0]
		ip   = namestr[i+20:i+24]
		lst.append((name, ip))
	return lst


# Creating a windows to select network interface

window = Tk()
window.resizable(0,0)
width = window.winfo_screenwidth()/4
height = window.winfo_screenheight()/4
window.geometry(str(width) + "x" + str(height))
window.title("Select Network Interface")

# Creating the button and the listbox to select network interface 

interface_list = allInterfaces()

scroll = Scrollbar(window)
networkList = Listbox(window, height = 10, width = 80, selectmode = SINGLE)
networkList.config(yscrollcommand = scroll.set)
scroll.config(command = networkList.yview)
for i in interface_list:
	networkList.insert(END,i[0])
	networkList.select_set(0)
networkList.pack()

buttonSelectNetwork = Button(window, text="Select",command=createWindow)
buttonSelectNetwork.pack(side=BOTTOM)

window.mainloop()





