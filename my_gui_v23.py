#Date: 6/20/2021
#Author: Robert Lyttle

##import libraries
import numpy as np
import os
import sys
import datetime
import time
import socket
import glob
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter.filedialog import askopenfilename, asksaveasfilename
import threading

cv2 = 0
var = 0
BANNER_SPEED = 0
BANNER = 0
RED = 255  # 0 - 255
BLUE = 255 # 0 - 255
GREEN = 255 # 0 - 255
x,y,w,h = 0,640,560,100
WIDTH = 1280
HEIGHT = 720
button1 = False
button5 = False
FORWARD = False
BACK = False
button2 = False
COUNT = 0

#get files
class Debugger1:
        def __init__(self, x,DATE, FILE):
                self.x = x
                self. DATE = DATE
                self.FILE = FILE

        def command_0():
                var.set('Missing VIDEO TIME make sure video file matches naming convention')
                messagebox.showinfo("showeinfo")
                messagebox.destroy("testing.....")

        #file namer
        def command_1():
                global count 
                while True:
                        COUNT = COUNT + 1
                        time.sleep(1)

        def command_2():
                pass

        def command_3():
                pass

        def command_4(a,b,c,d,e,f,g,h,j,k,frame,font,i):
                i = int(i)
                font_size = 0.4
                cv2.putText(frame,'Date: '+a,(10+i,50),font,font_size,(BLUE,GREEN,RED),1)
                cv2.putText(frame,'Time: '+b,(10+i,75),font,font_size,(BLUE,GREEN,RED),1)
                cv2.putText(frame,'PVR Line Number: '+k,(10+i,95),font,font_size,(BLUE,GREEN,RED),1)
                cv2.putText(frame,'Lane: '+c,(10+i,115),font,font_size,(BLUE,GREEN,RED),1)
                cv2.putText(frame,'Direction: '+d,(10+i,135),font,font_size,(BLUE,GREEN,RED),1)
                cv2.putText(frame,'Length: '+e,(10+i,155),font,font_size,(BLUE,GREEN,RED),1)
                cv2.putText(frame,'Speed: '+f,(10+i,175),font,font_size,(BLUE,GREEN,RED),1)
                cv2.putText(frame,'Class: '+g,(10+i,195),font,font_size,(BLUE,GREEN,RED),1)
                cv2.putText(frame,'Axle: {} {}'.format(h, j),(10+i,215),font,font_size,(BLUE,GREEN,RED),1)

        def command_5():
                pass

        def command_6():
                pass

        def command_7():
                entry100.delete(0, END)
                entry100.insert(END, BANNER[0])
                entry101.delete(0, END)
                entry101.insert(END, BANNER[3])
                entry102.delete(0, END)
                entry102.insert(END, BANNER_SPEED)
                entry103.delete(0, END)
                entry103.insert(END, BANNER[5])
                entry104.delete(0, END)
                entry104.insert(END, BANNER[10])
                entry105.delete(0, END)
                entry105.insert(END, BANNER[11])
                entry106.delete(0, END)
                entry106.insert(END, BANNER[6])
                entry107.delete(0, END)
                entry107.insert(END, BANNER[12])

        def command_8():
                pass

        def command_9():
                pass

        def command_10():
                pass

        def command_11():
                pass

#get files
def file0():
	"""Open a file for editing."""
	global FILE
	FILE = askopenfilename(filetypes=[("Files", "*.pvr"), ("All Files", "*.*")])
	entry102.delete(0, END)
	entry102.insert(END, FILE)
	print('file: ', FILE)

#converter time to seconds
def converter(converter):
	t = converter
	h,m,s = t.split(':')
	convert = float(datetime.timedelta(hours=float(h),minutes=float(m),seconds=float(s)).total_seconds())
	return convert

#get video files
def file1():
	"""Open a file for editing."""
	global FILE2
	FILE2 = askopenfilename(filetypes=[("Files", "*.mp4"), ("All Files", "*.*")])
	entry101.delete(0, END)
	entry101.insert(END, FILE2)
	print()

#Create buttons
def button_0():
	global button0
	button0 = "button0"
	def run1():
		Button(window, text="Button_0", state=DISABLED)
	thread = threading.Thread(target=run1)
	thread.start()
	print(button0)
#
def button_1():
        global button1
        button1 = not button1
        print('Pause again: ', button1)
#
def button_2():
        global button2
        button2 = not button2
        count0 = 0
        def run():
                Debugger1.command_1()
                entry101.delete(0, END)
                entry101.insert(END, count0)
                print("Button_4")
                
        thread1 = threading.Thread(target=run)
        thread1.start()
        print(button2)

def button_3():
        global BACK
        BACK = not BACK
        print('Back: ', BACK)
        entry102.delete(0, END)
        entry102.insert(END, BACK)
        
def button_4():
	global FORWARD
	FORWARD = not FORWARD
	print('Forward: ', FORWARD)
	
def button_5():
        print("Button 5")
        def run2():
                global button5
                button5 = not button5
                print(button5)
        thread2 = threading.Thread(target=run2)
        thread2.start()

def clear():
        entry100.delete(0, END)
        entry101.delete(0, END)
        entry102.delete(0, END)
        entry103.delete(0, END)
        entry104.delete(0, END)
        entry105.delete(0, END)
        entry106.delete(0, END)
        entry107.delete(0, END)
        entry108.delete(0, END)
        entry109.delete(0, END)
        entry110.delete(0, END)
        entry111.delete(0, END)
        entry112.delete(0, END)
        entry113.delete(0, END)
        entry114.delete(0, END)

def add_camera():
	global camera
	camera = entry101.get()
	print('Camera: ',camera)
	entry101.delete(0, END)
	
def stop():
	stop = True
	entry100.delete(0, END)
	entry101.delete(0, END)
	entry102.delete(0, END)
	entry103.delete(0, END)
	entry104.delete(0, END)
	entry105.delete(0, END)
	entry106.delete(0, END)
	entry107.delete(0, END)
	entry108.delete(0, END)
	entry109.delete(0, END)
	print(stop)

def exit():
        global stop
        stop = True
        entry100.delete(0, END)
        entry102.delete(0, END)
        entry103.delete(0, END)
        print(stop)
        window.destroy()

#settings menu main tab
def communication_wizard(object):
        Tabs = Tk()
        Tabs.geometry("400x400")
        Tabs.title("Connection Wizard")
        tabControl = ttk.Notebook(Tabs)

        comm_tab_1 = ttk.Frame(tabControl)
        comm_tab_2 = ttk.Frame(tabControl)
        comm_tab_3 = ttk.Frame(tabControl)
        comm_tab_4 = ttk.Frame(tabControl)

        tabControl.add(comm_tab_1, text ='TCP')
        tabControl.add(comm_tab_2, text ='Serial')
        tabControl.add(comm_tab_3, text ='Bluetooth')
        tabControl.add(comm_tab_4, text ='Wifi')
        tabControl.pack(expand = 8, fill ="both")

        #tab 1 TCP settings menu label
        tabControl = ttk.Notebook(comm_tab_1)
        comm_l1 = Label(comm_tab_1, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        comm_l1 = Label(comm_tab_1, text="IP address: ").grid(row=3, column=0, sticky="wn", padx=5)
        comm_l2 = Label(comm_tab_1, text="Subnet mask: ").grid(row=4, column=0, sticky="wn", padx=5)
        comm_l3 = Label(comm_tab_1, text="Default gateway: ").grid(row=5, column=0, sticky="wn", padx=5)
        comm_l4 = Label(comm_tab_1, text="Prefered DNS server: ").grid(row=6, column=0, sticky="wn", padx=5)
        comm_l5 = Label(comm_tab_1, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        comm_l6 = Label(comm_tab_1, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #tab 2 Serial/CAN settings menu label
        tabControl = ttk.Notebook(comm_tab_2)
        comm_l1 = Label(comm_tab_2, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        comm_l1 = Label(comm_tab_2, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        comm_l2 = Label(comm_tab_2, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        comm_l3 = Label(comm_tab_2, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        comm_l4 = Label(comm_tab_2, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        comm_l5 = Label(comm_tab_2, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        comm_l6 = Label(comm_tab_2, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #tab 3 Bluetooth settings menu label
        tabControl = ttk.Notebook(comm_tab_3)
        comm_l1 = Label(comm_tab_3, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        comm_l1 = Label(comm_tab_3, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        comm_l2 = Label(comm_tab_3, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        comm_l3 = Label(comm_tab_3, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        comm_l4 = Label(comm_tab_3, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        comm_l5 = Label(comm_tab_3, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        comm_l6 = Label(comm_tab_3, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #tab 3 Wifi settings menu label
        tabControl = ttk.Notebook(comm_tab_4)
        comm_l1 = Label(comm_tab_4, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        comm_l1 = Label(comm_tab_4, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        comm_l2 = Label(comm_tab_4, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        comm_l3 = Label(comm_tab_4, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        comm_l4 = Label(comm_tab_4, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        comm_l5 = Label(comm_tab_4, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        comm_l6 = Label(comm_tab_4, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)
        
        #tab 1 TCP settings menu entry box
        comm_1_0 = Entry(comm_tab_1, width=20)
        comm_1_1 = Entry(comm_tab_1, width=20)
        comm_1_2 = Entry(comm_tab_1, width=20)
        comm_1_3 = Entry(comm_tab_1, width=20)
        comm_1_4 = Entry(comm_tab_1, width=20)
        comm_1_5 = Entry(comm_tab_1, width=20)

        #tab 2 Serial/CAN settings menu entry box
        comm_2_0 = Entry(comm_tab_2, width=20)
        comm_2_1 = Entry(comm_tab_2, width=20)
        comm_2_2 = Entry(comm_tab_2, width=20)
        comm_2_3 = Entry(comm_tab_2, width=20)
        comm_2_4 = Entry(comm_tab_2, width=20)
        comm_2_5 = Entry(comm_tab_2, width=20)

        #tab 3 Buetooth settings menu entry box
        comm_3_0 = Entry(comm_tab_3, width=20)
        comm_3_1 = Entry(comm_tab_3, width=20)
        comm_3_2 = Entry(comm_tab_3, width=20)
        comm_3_3 = Entry(comm_tab_3, width=20)
        comm_3_4 = Entry(comm_tab_3, width=20)
        comm_3_5 = Entry(comm_tab_3, width=20)

        #tab 3 Wifi settings menu entry box
        comm_4_0 = Entry(comm_tab_4, width=20)
        comm_4_1 = Entry(comm_tab_4, width=20)
        comm_4_2 = Entry(comm_tab_4, width=20)
        comm_4_3 = Entry(comm_tab_4, width=20)
        comm_4_4 = Entry(comm_tab_4, width=20)
        comm_4_5 = Entry(comm_tab_4, width=20)

        #get TCP, Serial/CAN, Bluetooth, and Wifi settings menu entries
        def get_entry(TAB_NUM):
                global comm_100 # TCP
                global comm_101 # TCP
                global comm_102 # TCP
                global comm_103 # TCP
                global comm_104 # TCP
                global comm_105 # TCP

                global comm_200 # Serial/CAN
                global comm_201 # Serial/CAN
                global comm_202 # Serial/CAN
                global comm_203 # Serial/CAN
                global comm_204 # Serial/CAN
                global comm_205 # Serial/CAN

                global comm_300 # Bluetooth
                global comm_301 # Bluetooth
                global comm_302 # Bluetooth
                global comm_303 # Bluetooth
                global comm_304 # Bluetooth
                global comm_305 # Bluetooth

                global comm_400 # Wifi
                global comm_401 # Wifi
                global comm_402 # Wifi
                global comm_403 # wifi
                global comm_404 # wifi
                global comm_405 # wifi

                #tab 1 get TCP settings
                comm_100 = comm_1_0.get()
                comm_101 = comm_1_1.get()
                comm_102 = comm_1_2.get()
                comm_103 = comm_1_3.get()
                comm_104 = comm_1_4.get()
                comm_105 = comm_1_5.get()

                #test - getting values from TCP settings entry boxes and display them into entry boxes below:
                entry100.delete(0, END)
                entry100.insert(END, comm_1_0.get())
                entry101.delete(0, END)
                entry101.insert(END, comm_1_1.get())
                entry102.delete(0, END)
                entry102.insert(END, comm_1_2.get())
                entry103.delete(0, END)
                entry103.insert(END, comm_1_3.get())
                entry104.delete(0, END)
                entry104.insert(END, comm_1_4.get())
                entry105.delete(0, END)
                entry105.insert(END, comm_1_5.get())
                
                #tab 2 get Serial/CAN Settings
                comm_200 = comm_2_0.get()
                comm_201 = comm_2_1.get()
                comm_202 = comm_2_2.get()
                comm_203 = comm_2_3.get()
                comm_204 = comm_2_4.get()
                comm_205 = comm_2_5.get()

                #tab 3 get Bluetooth settings
                comm_300 = comm_3_0.get()
                comm_301 = comm_3_1.get()
                comm_302 = comm_3_2.get()
                comm_303 = comm_3_3.get()
                comm_304 = comm_3_4.get()
                comm_305 = comm_3_5.get()

                #tab 4 get Wifi settings
                comm_400 = comm_4_0.get()
                comm_401 = comm_4_1.get()
                comm_402 = comm_4_2.get()
                comm_403 = comm_4_3.get()
                comm_404 = comm_4_4.get()
                comm_405 = comm_4_5.get()

                #test - getting values from  Serial/CAN settings entry boxes and display them into entry boxes below:
                entry107.delete(0, END)
                entry107.insert(END, comm_2_0.get())
                entry108.delete(0, END)
                entry108.insert(END, comm_2_1.get())
                entry109.delete(0, END)
                entry109.insert(END, comm_2_2.get())
                entry110.delete(0, END)
                entry110.insert(END, comm_2_3.get())
                entry111.delete(0, END)
                entry112.insert(END, comm_2_4.get())
                entry113.delete(0, END)
                entry114.insert(END, comm_2_0.get())

                print("Tab_NUMBER: ", TAB_NUM)
                print("E0: ", comm_100)
                print("E1: ", comm_101)
                print("E2: ", comm_102)
                print("E3: ", comm_103)
                print("E4: ", comm_104)
                print("E5: ", comm_105)

        #tab 1, 2, 3, and 4 settings window menu labels
        e_label1 = Label(comm_tab_1, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        e_label2 = Label(comm_tab_2, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        e_label3 = Label(comm_tab_3, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        e_label4 = Label(comm_tab_4, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)

        #tab 1 settings menu buttons
        Button(comm_tab_1, text="+").grid(row=9, column=1, sticky="wne")
        Button(comm_tab_1, text="-").grid(row=10, column=1, sticky="wne")
        Button(comm_tab_1, text="Setting_3").grid(row=11, column=1, sticky="wne")
        Button(comm_tab_1, text="Setting_4").grid(row=12, column=1, sticky="wne")

        #tab 2 settings menu buttons
        Button(comm_tab_2, text="+").grid(row=9, column=1, sticky="wne")
        Button(comm_tab_2, text="-").grid(row=10, column=1, sticky="wne")
        Button(comm_tab_2, text="Setting_3").grid(row=11, column=1, sticky="wne")
        Button(comm_tab_2, text="Setting_4").grid(row=12, column=1, sticky="wne")
        def kill_set():
                Tabs.destroy()

        def submit():
                message1 = "Submitted"
                print("Message1: ", message1)
                get_entry(button_select)
                Tabs.destroy()

        #tab 1 settings menu buttons
        Button(comm_tab_1, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        Button(comm_tab_1, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #tab 2 settings menu buttons
        Button(comm_tab_2, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        Button(comm_tab_2, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #tab 1 settings menu window show entry boxes on screen
        comm_1_0.grid(row=3, column=1, sticky="wne")
        comm_1_1.grid(row=4, column=1, sticky="wne")
        comm_1_2.grid(row=5, column=1, sticky="wne")
        comm_1_3.grid(row=6, column=1, sticky="wne")
        comm_1_4.grid(row=7, column=1, sticky="wne")
        comm_2_5.grid(row=8, column=1, sticky="wne")

        #tab 2 settings menu window show entry boxes on screen
        comm_2_0.grid(row=3, column=1, sticky="wne")
        comm_2_1.grid(row=4, column=1, sticky="wne")
        comm_2_2.grid(row=5, column=1, sticky="wne")
        comm_2_3.grid(row=6, column=1, sticky="wne")
        comm_2_4.grid(row=7, column=1, sticky="wne")
        comm_2_5.grid(row=8, column=1, sticky="wne")
        Tabs.mainloop()

#call settings funtions here
def settings_menu(object):
        global button1
        global button_select
        button_select = object
        button1 = not button1
        print('Pause again: ', button1)
        communication_wizard(object)

#call "control" functions here
#call funtions here
def control_menu(object):
        global button1
        global button_select
        button_select = object
        button1 = not button1
        print('Pause again: ', button1)
        troubleshoot_wizard(object)

                
def set_date():
	# Create Calendar Object
	root = Tk()

	# Set geometry
	root.geometry("400x400")
	root.title('Date')

	# Add Calender
	cal = Calendar(root, selectmode = 'day', year = 2020, month = 5, day = 22)
	cal.pack(pady = 20)
	def grad_date():
		date.config(text = 'Selected date is: ' + cal.get_date())
		video_date = cal.get_date()
		month, day, year = video_date.split('/')
		global DATE
		DATE  = '0{}/0{}/{}'.format(day, month, year)
		entry100.delete(0, END)
		entry100.insert(END, DATE)
		print('Date: ', DATE)
		root.destroy()

	# Add Button and Label
	btn_sel = Button(root, text = "Submit", command = grad_date)
	btn_sel.pack(pady = 20)

	date = Label(root, text = "")
	date.pack(pady = 20)

	# Excecute Tkinter
	root.mainloop()

#main window screen
window_tabs = Tk()
window_tabs.geometry("800x800")
window_tabs.title("Debugger1")
tabControl = ttk.Notebook(window_tabs)

window = ttk.Frame(tabControl)
window_1 = ttk.Frame(tabControl)
troubleshoot_wizard = ttk.Frame(tabControl)

tabControl.add(window, text ='Sensor')
tabControl.add(window_1, text ='Diagnostics')
tabControl.pack(expand = 1, fill ="both")

#troubleshooter wizard allows for live interaction with your code
def troubleshoot_wizard():
        troubleshooter = Tk()
        troubleshooter.geometry("600x600")
        troubleshooter.title("Troubleshoot Wizard")
        tabControl = ttk.Notebook(troubleshooter)

        control_1 = ttk.Frame(tabControl)
        control_2 = ttk.Frame(tabControl)
        control_3 = ttk.Frame(tabControl)
        control_4 = ttk.Frame(tabControl)

        tabControl.add(control_1, text ='Channel: 1')
        tabControl.add(control_2, text ='Channel: 2')
        tabControl.add(control_3, text ='Channel: 3')
        tabControl.add(control_4, text ='Channel: 4')
        tabControl.pack(expand = 8, fill ="both")

        #control 1 menu label
        tabControl = ttk.Notebook(control_1)
        ctrl_l_1_1 = Label(control_1, text="Input Control").grid(row=2, column=0, sticky="wn", padx=5)
        ctrl_l_1_2 = Label(control_1, text="Value_0: ").grid(row=3, column=0, sticky="wn", padx=5)
        ctrl_l_1_3 = Label(control_1, text="Value_1: ").grid(row=4, column=0, sticky="wn", padx=5)
        ctrl_l_1_4 = Label(control_1, text="Value_2: ").grid(row=5, column=0, sticky="wn", padx=5)
        ctrl_l_1_5 = Label(control_1, text="Value_3: ").grid(row=6, column=0, sticky="wn", padx=5)
        ctrl_l_1_6 = Label(control_1, text="Value_4: ").grid(row=7, column=0, sticky="wn", padx=5)
        ctrl_l_1_7 = Label(control_1, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #control 2 menu label
        tabControl = ttk.Notebook(control_2)
        ctrl_l_2_1 = Label(control_2, text="Control Setting ").grid(row=2, column=0, sticky="wn", padx=5)
        ctrl_l_2_2 = Label(control_2, text="Value_0: ").grid(row=3, column=0, sticky="wn", padx=5)
        ctrl_l_2_3 = Label(control_2, text="Value_1: ").grid(row=4, column=0, sticky="wn", padx=5)
        ctrl_l_2_4 = Label(control_2, text="Value_2: ").grid(row=5, column=0, sticky="wn", padx=5)
        ctrl_l_2_5 = Label(control_2, text="Value_3: ").grid(row=6, column=0, sticky="wn", padx=5)
        ctrl_l_2_6 = Label(control_2, text="Value_4: ").grid(row=7, column=0, sticky="wn", padx=5)
        ctrl_l_2_7 = Label(control_2, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #control 3 menu label
        tabControl = ttk.Notebook(control_3)
        ctrl_l_3_1 = Label(control_3, text="Control Setting ").grid(row=2, column=0, sticky="wn", padx=5)
        ctrl_l_3_2 = Label(control_3, text="Value_0: ").grid(row=3, column=0, sticky="wn", padx=5)
        ctrl_l_3_3 = Label(control_3, text="Value_1: ").grid(row=4, column=0, sticky="wn", padx=5)
        ctrl_l_3_4 = Label(control_3, text="Value_2: ").grid(row=5, column=0, sticky="wn", padx=5)
        cntrl_l_3_5 = Label(control_3, text="Value_3 ").grid(row=6, column=0, sticky="wn", padx=5)
        ctrl_l_3_6 = Label(control_3, text="Value_4: ").grid(row=7, column=0, sticky="wn", padx=5)
        ctrl_l_3_7 = Label(control_3, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #control 4 menu label
        tabControl = ttk.Notebook(control_4)
        ctrl_l_4_1 = Label(control_4, text="Control Setting ").grid(row=2, column=0, sticky="wn", padx=5)
        ctrl_l_4_2 = Label(control_4, text="Value_0: ").grid(row=3, column=0, sticky="wn", padx=5)
        ctrl_l_4_3 = Label(control_4, text="Value_1: ").grid(row=4, column=0, sticky="wn", padx=5)
        ctrl_l_4_4 = Label(control_4, text="Value_2: ").grid(row=5, column=0, sticky="wn", padx=5)
        ctrl_l_4_5 = Label(control_4, text="Value_3: ").grid(row=6, column=0, sticky="wn", padx=5)
        ctrl_l_4_6 = Label(control_4, text="Value_4: ").grid(row=7, column=0, sticky="wn", padx=5)
        ctrl_l_4_7 = Label(control_4, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)
        
        #control tab 1 entry box
        ctrl_1_0 = Entry(control_1, width=20)
        ctrl_1_1 = Entry(control_1, width=20)
        ctrl_1_2 = Entry(control_1, width=20)
        ctrl_1_3 = Entry(control_1, width=20)
        ctrl_1_4 = Entry(control_1, width=20)
        ctrl_1_5 = Entry(control_1, width=20)

        #control tab 2 entry box
        ctrl_2_0 = Entry(control_2, width=20)
        ctrl_2_1 = Entry(control_2, width=20)
        ctrl_2_2 = Entry(control_2, width=20)
        ctrl_2_3 = Entry(control_2, width=20)
        ctrl_2_4 = Entry(control_2, width=20)
        ctrl_2_5 = Entry(control_2, width=20)

        #control tab 3 entry box
        ctrl_3_0 = Entry(control_3, width=20)
        ctrl_3_1 = Entry(control_3, width=20)
        ctrl_3_2 = Entry(control_3, width=20)
        ctrl_3_3 = Entry(control_3, width=20)
        ctrl_3_4 = Entry(control_3, width=20)
        ctrl_3_5 = Entry(control_3, width=20)

        #control tab 4 entry box
        ctrl_4_0 = Entry(control_4, width=20)
        ctrl_4_1 = Entry(control_4, width=20)
        ctrl_4_2 = Entry(control_4, width=20)
        ctrl_4_3 = Entry(control_4, width=20)
        ctrl_4_4 = Entry(control_4, width=20)
        ctrl_4_5 = Entry(control_4, width=20)

        #get control 1, 2, 3, and 4 entries from entry box
        def get_entry(TAB_NUM):
                #control tab 1
                global ctrl_100 # Value_0
                global ctrl_101 # Value_1
                global ctrl_102 # Value_2
                global ctrl_103 # Value_3
                global ctrl_104 # Value_4
                global ctrl_105 # Value_5

                #control tab 2
                global ctrl_200 # Value_0
                global ctrl_201 # Value_1
                global ctrl_202 # Value_2
                global ctrl_203 # Value_3
                global ctrl_204 # Value_4
                global ctrl_205 # Value_5

                #control tab 3
                global ctrl_300 # Value_0
                global ctrl_301 # Value_1
                global ctrl_302 # Value_2
                global ctrl_303 # Value_3
                global ctrl_304 # Value_4
                global ctrl_305 # Value_5

                #control tab 4
                global ctrl_400 # Value_0
                global ctrl_401 # Value_1
                global ctrl_402 # Value_2
                global ctrl_403 # Value_3
                global ctrl_404 # Value_4
                global ctrl_405 # Value_5

                #control tab 1 get Values 0, 1, 2, 3, 4, 5
                ctrl_100 = ctrl_1_0.get()
                ctrl_101 = ctrl_1_1.get()
                ctrl_102 = ctrl_1_2.get()
                ctrl_103 = ctrl_1_3.get()
                ctrl_104 = ctrl_1_4.get()
                ctrl_105 = ctrl_1_5.get()

                #test - getting values from TCP settings entry boxes and display them into entry boxes below:
                entry100.delete(0, END)
                entry100.insert(END, ctrl_1_0.get())
                entry101.delete(0, END)
                entry101.insert(END, ctrl_1_1.get())
                entry102.delete(0, END)
                entry102.insert(END, ctrl_1_2.get())
                entry103.delete(0, END)
                entry103.insert(END, ctrl_1_3.get())
                entry104.delete(0, END)
                entry104.insert(END, ctrl_1_4.get())
                entry105.delete(0, END)
                entry105.insert(END, ctrl_1_5.get())
                entry105.insert(END, COUNT)
                
                #tab 2 get Serial/CAN Settings
                ctrl_200 = ctrl_2_0.get()
                ctrl_201 = ctrl_2_1.get()
                ctrl_202 = ctrl_2_2.get()
                ctrl_203 = ctrl_2_3.get()
                ctrl_204 = ctrl_2_4.get()
                ctrl_205 = ctrl_2_5.get()

                #tab 3 get Bluetooth settings
                ctrl_300 = ctrl_3_0.get()
                ctrl_301 = ctrl_3_1.get()
                ctrl_302 = ctrl_3_2.get()
                ctrl_303 = ctrl_3_3.get()
                ctrl_304 = ctrl_3_4.get()
                ctrl_305 = ctrl_3_5.get()

                #tab 4 get Wifi settings
                ctrl_400 = ctrl_4_0.get()
                ctrl_401 = ctrl_4_1.get()
                ctrl_402 = ctrl_4_2.get()
                ctrl_403 = ctrl_4_3.get()
                ctrl_404 = ctrl_4_4.get()
                ctrl_405 = ctrl_4_5.get()

                #test - getting values from  Serial/CAN settings entry boxes and display them into entry boxes below:
                entry107.delete(0, END)
                entry107.insert(END, ctrl_2_0.get())
                entry108.delete(0, END)
                entry108.insert(END, ctrl_2_1.get())
                entry109.delete(0, END)
                entry109.insert(END, ctrl_2_2.get())
                entry110.delete(0, END)
                entry110.insert(END, ctrl_2_3.get())
                entry111.delete(0, END)
                entry112.insert(END, ctrl_2_4.get())
                entry113.delete(0, END)
                entry114.insert(END, ctrl_2_0.get())

                print("Tab_NUMBER: ", TAB_NUM)
                print("C0: ", ctrl_100)
                print("C1: ", ctrl_101)
                print("C2: ", ctrl_102)
                print("C3: ", ctrl_103)
                print("C4: ", ctrl_104)
                print("C5: ", ctrl_105)

        #up counter
        def count_up():
                COUNT = 0
                global OUTPUT
                COUNT = COUNT + 1
                OUTPUT = COUNT
                ctrl_1_0.delete(0, END)
                ctrl_1_0.insert(END, COUNT)

        #down counter
        def count_down():
                COUNT = 0
                global OUTPUT
                COUNT = COUNT - 1
                OUTPUT = COUNT
                ctrl_1_0.delete(0, END)
                ctrl_1_0.insert(END, COUNT)


        #c_1_0.delete(0, END)
        #c_1_0.insert(END, output)

        #control tab 1, 2, 3, and 4 main window channel label
        channel1_select = "1"
        channel2_select = "2"
        channel3_select = "3"
        channel4_select = "4"
        ctrl_label_1_1 = Label(control_1, text="Channel: {}".format(channel1_select)).grid(row=0, column=0, sticky="wn", padx=5)
        ctrl_label_1_2 = Label(control_2, text="Channel: {}".format(channel2_select)).grid(row=0, column=0, sticky="wn", padx=5)
        ctrl_label_1_3 = Label(control_3, text="Channel: {}".format(channel3_select)).grid(row=0, column=0, sticky="wn", padx=5)
        ctrl__label_1_4 = Label(control_4, text="Channel: {}".format(channel4_select)).grid(row=0, column=0, sticky="wn", padx=5)

        #control tab 1 buttons
        ctrl_1_btn_1 = Button(control_1, text="Up", command=count_up).grid(row=9, column=1, sticky="wne", pady=5)
        ctrl_1_btn_2 = Button(control_1, text="Down", command=count_down).grid(row=10, column=1, sticky="wne", pady=5)
        ctrl_1_btn_3 = Button(control_1, text="Setting_3").grid(row=11, column=1, sticky="wne")
        ctrl_1_btn_4 = Button(control_1, text="Setting_4").grid(row=12, column=1, sticky="wne")
        ctrl_1_btn_5 = Button(control_1, text="Left").grid(row=9, column=2, sticky="wne", padx=5, pady=5)
        ctrl_1_btn_6 = Button(control_1, text="Right").grid(row=9, column=3, sticky="wne", padx=5, pady=5)

        #control tab 2 buttons
        ctrl_2_btn_1 = Button(control_2, text="+", command=count_up).grid(row=9, column=1, sticky="wne")
        ctrl_2_btn_2 = Button(control_2, text="-", command=count_down).grid(row=10, column=1, sticky="wne")
        ctrl_2_btn_3 = Button(control_2, text="Setting_3").grid(row=11, column=1, sticky="wne")
        ctrl_2_btn_4 = Button(control_2, text="Setting_4").grid(row=12, column=1, sticky="wne")
        def kill_set():
                troubleshooter.destroy()

        def submit():
                message1 = "Submitted"
                print("Message1: ", message1)
                troubleshooter.destroy()

        #control tab 1 buttons
        ctrl_1_btn_5 = Button(control_1, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        ctrl_1_btn_6 = Button(control_1, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #control tab 2 buttons
        ctrl_5_btn_5 = Button(control_2, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        ctrl_btn_6 = Button(control_2, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #control tab 1 entry boxes on screen
        ctrl_1_0.grid(row=3, column=1, sticky="wne")
        ctrl_1_1.grid(row=4, column=1, sticky="wne")
        ctrl_1_2.grid(row=5, column=1, sticky="wne")
        ctrl_1_3.grid(row=6, column=1, sticky="wne")
        ctrl_1_4.grid(row=7, column=1, sticky="wne")
        ctrl_2_5.grid(row=8, column=1, sticky="wne")

        #control tab 2 show entry boxes on screen
        ctrl_2_0.grid(row=3, column=1, sticky="wne")
        ctrl_2_1.grid(row=4, column=1, sticky="wne")
        ctrl_2_2.grid(row=5, column=1, sticky="wne")
        ctrl_2_3.grid(row=6, column=1, sticky="wne")
        ctrl_2_4.grid(row=7, column=1, sticky="wne")
        ctrl_2_5.grid(row=8, column=1, sticky="wne")
        troubleshooter.mainloop()


#tab 1 main window entry box
#window = Frame(window, relief=RAISED, bd=2)
entry100 = Entry(window, width=10)
entry101 = Entry(window, width=100)
entry102 = Entry(window, width=10)
entry103 = Entry(window, width=10)
entry104 = Entry(window, width=10)
entry105 = Entry(window, width=10)
entry106 = Entry(window, width=10) 
entry107 = Entry(window, width=10) 
entry108 = Entry(window, width=10) 
entry109 = Entry(window, width=10)
entry110 = Entry(window, width=10)
entry111 = Entry(window, width=10)
entry112 = Entry(window, width=10)
entry113 = Entry(window, width=10)
entry114 = Entry(window, width=10)
entry115 = Entry(window, width=10)

#tab 1 main window buttons
btn_file1 = Button(window, text="Import video", command=file1).grid(row=2, column=0, sticky="ew", padx=5)
btn_100 = Button(window, text="Button_00", command=button_0).grid(row=3, column=0, sticky="ew", padx=5)
btn_101 = Button(window, text="Button_01", command=button_1).grid(row=4, column=0, sticky="ew", padx=5)
btn_102 = Button(window, text="Button_02", command=button_2).grid(row=5, column=0, sticky="ew", padx=5)
btn_103 = Button(window, text="Button_03", command=button_3).grid(row=6, column=0, sticky="ew", padx=5)
btn_104 = Button(window, text="Button_04", command=button_4).grid(row=7, column=0, sticky="ew", padx=5)
btn_105 = Button(window, text="Button_05", command=button_5).grid(row=8, column=0, sticky="ew", padx=5)
btn_106 = Button(window, text="Button_06", command=button_5).grid(row=9, column=0, sticky="ew", padx=5)
btn_107 = Button(window, text="Button_07", command=button_0).grid(row=10, column=0, sticky="ew", padx=5)
btn_108 = Button(window, text="Button_08", command=button_1).grid(row=11, column=0, sticky="ew", padx=5)
btn_109 = Button(window, text="Button_09", command=button_2).grid(row=12, column=0, sticky="ew", padx=5)
btn_110 = Button(window, text="Button_10", command=button_3).grid(row=13, column=0, sticky="ew", padx=5)
btn_111 = Button(window, text="Button_11", command=button_4).grid(row=14, column=0, sticky="ew", padx=5)
btn_112 = Button(window, text="Button_12", command=button_5).grid(row=15, column=0, sticky="ew", padx=5)
btn_113 = Button(window, text="Button_13", command=button_5).grid(row=16, column=0, sticky="ew", padx=5)
btn_114 = Button(window, text="Button_14", command=button_5).grid(row=17, column=0, sticky="ew", padx=5)
btn_stop = Button(window, text="Stop", command=stop).grid(row=23, column=0, sticky="ew", padx=5)

#tab 2 main window buttons
btn_200 = Button(window_1, text="Troubleshooter", command=troubleshoot_wizard).grid(row=5, column=0, sticky="ew", padx=5)

#tab 1 main window settings button
btn_set_100 = Button(window, text="+", command=lambda:settings_menu(0)).grid(row=3, column=3, sticky="ew", padx=5)
btn_set_101 = Button(window, text="+", command=lambda:settings_menu(1)).grid(row=4, column=3, sticky="ew", padx=5)
btn_set_102 = Button(window, text="+", command=lambda:settings_menu(2)).grid(row=5, column=3, sticky="ew", padx=5)
btn_set_103 = Button(window, text="+", command=lambda:settings_menu(3)).grid(row=6, column=3, sticky="ew", padx=5)
btn_set_104 = Button(window, text="+", command=lambda:settings_menu(4)).grid(row=7, column=3, sticky="ew", padx=5)
btn_105 = Button(window, text="+",command=lambda:settings_menu(5) ).grid(row=8, column=3, sticky="ew", padx=5)
btn_set_106 = Button(window, text="+", command=lambda:settings_menu(6)).grid(row=9, column=3, sticky="ew", padx=5)
btn_set_107 = Button(window, text="+", command=lambda:settings_menu(7)).grid(row=10, column=3, sticky="ew", padx=5)
btn_set_108 = Button(window, text="+", command=lambda:settings_menu(8)).grid(row=11, column=3, sticky="ew", padx=5)
btn_set_109 = Button(window, text="+", command=lambda:settings_menu(9)).grid(row=12, column=3, sticky="ew", padx=5)
btn_set_110 = Button(window, text="+", command=lambda:settings_menu(10)).grid(row=13, column=3, sticky="ew", padx=5)
btn_set_111 = Button(window, text="+", command=lambda:settings_menu(11)).grid(row=14, column=3, sticky="ew", padx=5)
btn_set_112 = Button(window, text="+", command=lambda:settings_menu(12)).grid(row=15, column=3, sticky="ew", padx=5)
btn_set_113 = Button(window, text="+", command=lambda:settings_menu(13)).grid(row=16, column=3, sticky="ew", padx=5)
btn_set_114 = Button(window, text="+", command=lambda:settings_menu(14)).grid(row=17, column=3, sticky="ew", padx=5)
btn_set_date = Button(window, text = "Select Date", command = set_date).grid(row=18, column=0, sticky="ew", padx=5) # tab 1 main window
btn_file0 = Button(window, text="Import file", command=file0).grid(row=19, column=0, sticky="ew", padx=5) # tab 1 main window
btn_add_camera = Button(window, text="Add Camera", command=add_camera).grid(row=20, column=0, sticky="ew", padx=5) # tab 1 main window
btn_clear = Button(window, text="Clear", command=clear).grid(row=21, column=0, sticky="ew", padx=5) # tab 1 main window
btn_exit = Button(window, text="Exit", command=exit).grid(row=24, column=0, sticky="ew", padx=5) #tab 1 main window

#tab 1 main window labels
l1 = Label(window, text="Debugger1 Status:").grid(row=0, column=0, sticky="wne", padx=5) #tab 1 main window
l100 = Label(window, text="00: ").grid(row=3, column=1, sticky="wn", padx=5)
l101 = Label(window, text="01: ").grid(row=4, column=1, sticky="wn", padx=5)
l102 = Label(window, text="02: ").grid(row=5, column=1, sticky="wn", padx=5)
l103 = Label(window, text="03: ").grid(row=6, column=1, sticky="wn", padx=5)
l104 = Label(window, text="04: ").grid(row=7, column=1, sticky="wn", padx=5)
l105 = Label(window, text="05: ").grid(row=8, column=1, sticky="wn", padx=5)
l106 = Label(window, text="06: ").grid(row=9, column=1, sticky="wn", padx=5)
l107 = Label(window, text="07: ").grid(row=10, column=1, sticky="wn", padx=5)
l108 = Label(window, text="08: ").grid(row=11, column=1, sticky="wn", padx=5)
l109 = Label(window, text="09: ").grid(row=12, column=1, sticky="wn", padx=5)
l110 = Label(window, text="10: ").grid(row=13, column=1, sticky="wn", padx=5)
l111 = Label(window, text="11: ").grid(row=14, column=1, sticky="wn", padx=5)
l112 = Label(window, text="12: ").grid(row=15, column=1, sticky="wn", padx=5)
l113 = Label(window, text="13: ").grid(row=16, column=1, sticky="wn", padx=5)
l114 = Label(window, text="14: ").grid(row=17, column=1, sticky="wn", padx=5)

#tab 2 main window label
l200 = Label(window_1, text="Diagnostics: ").grid(row=3, column=0, sticky="wn", padx=5)

#tab 1 show main window entry box
entry100.grid(row=3, column=2, sticky="wne", padx=5)
entry101.grid(row=4, column=2, sticky="wne", padx=5)
entry102.grid(row=5, column=2, sticky="wne", padx=5)
entry103.grid(row=6, column=2, sticky="wne", padx=5)
entry104.grid(row=7, column=2, sticky="wne", padx=5)
entry105.grid(row=8, column=2, sticky="wne", padx=5)
entry106.grid(row=9, column=2, sticky="wne", padx=5)
entry107.grid(row=10, column=2, sticky="wne", padx=5)
entry108.grid(row=11, column=2, sticky="wne", padx=5)
entry109.grid(row=12, column=2, sticky="wne", padx=5)
entry110.grid(row=13, column=2, sticky="wne", padx=5)
entry111.grid(row=14, column=2, sticky="wne", padx=5)
entry112.grid(row=15, column=2, sticky="wne", padx=5)
entry113.grid(row=16, column=2, sticky="wne", padx=5)
entry114.grid(row=17, column=2, sticky="wne", padx=5)
entry115.grid(row=18, column=2, sticky="wne", padx=5)

#create main window
window_tabs.mainloop()

