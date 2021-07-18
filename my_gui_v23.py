#Date: 6/20/2021
#Author: Robert Lyttle
#variable naming convension (window_name_{window number}_widget ID: (Button or Entry)_{row position}).format(a, b)
#for example:
#comm_1_label_0_0 = Label(comm_tab_1, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
#
#window_number: 1
#window_name: comm
#screen position: row = 0
#screen position: column: 0

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
                mw_1_entry_3_2.delete(0, END)
                mw_1_entry_3_2.insert(END, BANNER[0])
                mw_1_entry_4_2.delete(0, END)
                mw_1_entry_4_2.insert(END, BANNER[3])
                mw_1_entry_5_2.delete(0, END)
                mw_1_entry_5_2.insert(END, BANNER_SPEED)
                mw_1_entry_6_2.delete(0, END)
                mw_1_entry_6_2.insert(END, BANNER[5])
                mw_1_entry_7_2.delete(0, END)
                mw_1_entry_7_2.insert(END, BANNER[10])
                mw_1_entry_8_2.delete(0, END)
                mw_1_entry_8_2.insert(END, BANNER[11])
                mw_1_entry_9_2.delete(0, END)
                mw_1_entry_9_2.insert(END, BANNER[6])
                mw_1_entry_10_2.delete(0, END)
                mw_1_entry_10_2.insert(END, BANNER[12])

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
	mw_1_entry_4_2.delete(0, END)
	mw_1_entry_4_2.insert(END, FILE)
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
	mw_1_entry_5_2.delete(0, END)
	mw_1_entry_5_2.insert(END, FILE2)
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
                mw_1_entry_4_2.delete(0, END)
                mw_1_entry_4_2.insert(END, count0)
                print("Button_4")
                
        thread1 = threading.Thread(target=run)
        thread1.start()
        print(button2)

def button_3():
        global BACK
        BACK = not BACK
        print('Back: ', BACK)
        mw_1_entry_4_2.delete(0, END)
        mw_1_entry_4_2.insert(END, BACK)
        
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
        mw_1_entry_3_2.delete(0, END)
        mw_1_entry_4_2.delete(0, END)
        mw_1_entry_5_2.delete(0, END)
        mw_1_entry_6_2.delete(0, END)
        mw_1_entry_7_2.delete(0, END)
        mw_1_entry_8_2.delete(0, END)
        mw_1_entry_9_2.delete(0, END)
        mw_1_entry_10_2.delete(0, END)
        mw_1_entry_11_2.delete(0, END)
        mw_1_entry_12_2.delete(0, END)
        mw_1_entry_13_2.delete(0, END)
        mw_1_entry_14_2.delete(0, END)
        mw_1_entry_15_2.delete(0, END)
        mw_1_entry_16_2.delete(0, END)
        mw_1_entry_17_2.delete(0, END)

def add_camera():
	global camera
	camera = mw_1_entry_4_2.get()
	print('Camera: ',camera)
	mw_1_entry_4_2.delete(0, END)
	
def stop():
	stop = True
	mw_1_entry_3_2.delete(0, END)
	mw_1_entry_4_2.delete(0, END)
	mw_1_entry_5_2.delete(0, END)
	mw_1_entry_6_2.delete(0, END)
	mw_1_entry_7_2.delete(0, END)
	mw_1_entry_8_2.delete(0, END)
	mw_1_entry_9_2.delete(0, END)
	mw_1_entry_10_2.delete(0, END)
	mw_1_entry_11_2.delete(0, END)
	mw_1_entry_12_2.delete(0, END)
	print(stop)

def exit():
        global stop
        stop = True
        mw_1_entry_3_2.delete(0, END)
        mw_1_entry_4_2.delete(0, END)
        mw_1_entry_5_2.delete(0, END)
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
        comm_1_label_0_0 = Label(comm_tab_1, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        comm_1_label_3_0 = Label(comm_tab_1, text="IP address: ").grid(row=3, column=0, sticky="wn", padx=5)
        comm_1_label_4_0 = Label(comm_tab_1, text="Subnet mask: ").grid(row=4, column=0, sticky="wn", padx=5)
        comm_1_label_5_0 = Label(comm_tab_1, text="Default gateway: ").grid(row=5, column=0, sticky="wn", padx=5)
        comm_1_label_6_0 = Label(comm_tab_1, text="Prefered DNS server: ").grid(row=6, column=0, sticky="wn", padx=5)
        comm_1_label_7_0 = Label(comm_tab_1, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        comm_1_label_8_0 = Label(comm_tab_1, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #tab 2 Serial/CAN settings menu label
        tabControl = ttk.Notebook(comm_tab_2)
        comm_2_label_0_0 = Label(comm_tab_2, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        comm_2_label_3_0 = Label(comm_tab_2, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        comm_2_label_4_0 = Label(comm_tab_2, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        comm_2_label_5_0 = Label(comm_tab_2, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        comm_2_label_6_0 = Label(comm_tab_2, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        comm_2_label_7_0 = Label(comm_tab_2, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        comm_2_label_8_0 = Label(comm_tab_2, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #tab 3 Bluetooth settings menu label
        tabControl = ttk.Notebook(comm_tab_3)
        comm_3_label_0_0 = Label(comm_tab_3, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        comm_3_label_3_0 = Label(comm_tab_3, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        comm_3_label_4_0 = Label(comm_tab_3, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        comm_3_label_5_0 = Label(comm_tab_3, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        comm_3_label_6_0 = Label(comm_tab_3, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        comm_3_label_7_0 = Label(comm_tab_3, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        comm_3_label_8_0 = Label(comm_tab_3, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #tab 4 Wifi settings menu label
        tabControl = ttk.Notebook(comm_tab_4)
        comm_4_label_0_0 = Label(comm_tab_4, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        comm_4_label_3_0 = Label(comm_tab_4, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        comm_4_label_4_0 = Label(comm_tab_4, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        comm_4_label_5_0 = Label(comm_tab_4, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        comm_4_label_6_0 = Label(comm_tab_4, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        comm_4_label_7_0 = Label(comm_tab_4, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        comm_4_label_8_0 = Label(comm_tab_4, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)
        
        #tab 1 TCP settings menu entry box
        comm_1_entry_3_1 = Entry(comm_tab_1, width=20)
        comm_1_entry_4_1 = Entry(comm_tab_1, width=20)
        comm_1_entry_5_1 = Entry(comm_tab_1, width=20)
        comm_1_entry_6_1 = Entry(comm_tab_1, width=20)
        comm_1_entry_7_1 = Entry(comm_tab_1, width=20)
        comm_1_entry_8_1 = Entry(comm_tab_1, width=20)

        #tab 2 Serial/CAN settings menu entry box
        comm_2_entry_3_1 = Entry(comm_tab_2, width=20)
        comm_2_entry_4_1 = Entry(comm_tab_2, width=20)
        comm_2_entry_5_1 = Entry(comm_tab_2, width=20)
        comm_2_entry_6_1 = Entry(comm_tab_2, width=20)
        comm_2_entry_7_1 = Entry(comm_tab_2, width=20)
        comm_2_entry_8_1 = Entry(comm_tab_2, width=20)

        #tab 3 Buetooth settings menu entry box
        comm_3_entry_3_1 = Entry(comm_tab_3, width=20)
        comm_3_entry_4_1 = Entry(comm_tab_3, width=20)
        comm_3_entry_5_1 = Entry(comm_tab_3, width=20)
        comm_3_entry_6_1 = Entry(comm_tab_3, width=20)
        comm_3_entry_7_1 = Entry(comm_tab_3, width=20)
        comm_3_entry_8_1 = Entry(comm_tab_3, width=20)

        #tab 3 Wifi settings menu entry box
        comm_4_entry_3_1 = Entry(comm_tab_4, width=20)
        comm_4_entry_4_1 = Entry(comm_tab_4, width=20)
        comm_4_entry_5_1 = Entry(comm_tab_4, width=20)
        comm_4_entry_6_1 = Entry(comm_tab_4, width=20)
        comm_4_entry_7_1 = Entry(comm_tab_4, width=20)
        comm_4_entry_8_1 = Entry(comm_tab_4, width=20)

        #get TCP, Serial/CAN, Bluetooth, and Wifi settings menu entries
        def get_entry(TAB_NUM):
                global comm_1_output_1 # TCP
                global comm_1_output_2 # TCP
                global comm_1_output_3 # TCP
                global comm_1_output_4 # TCP
                global comm_1_output_5 # TCP
                global comm_1_output_6 # TCP

                global comm_2_output_1 # Serial/CAN
                global comm_2_output_2 # Serial/CAN
                global comm_2_output_3 # Serial/CAN
                global comm_2_output_4 # Serial/CAN
                global comm_2_output_5 # Serial/CAN
                global comm_2_output_6 # Serial/CAN

                global comm_3_output_1 # Bluetooth
                global comm_3_output_2 # Bluetooth
                global comm_3_output_3 # Bluetooth
                global comm_3_output_4 # Bluetooth
                global comm_3_output_5 # Bluetooth
                global comm_3_output_6 # Bluetooth

                global comm_4_output_1 # Wifi
                global comm_4_output_2 # Wifi
                global comm_4_output_3 # Wifi
                global comm_4_output_4 # wifi
                global comm_4_output_5 # wifi
                global comm_4_output_6 # wifi

                #tab 1 get TCP settings
                comm_1_output_1 = comm_1_entry_3_1.get()
                comm_1_output_2 = comm_1_entry_4_1.get()
                comm_1_output_3 = comm_1_entry_5_1.get()
                comm_1_output_4 = comm_1_entry_3_1.get()
                comm_1_output_5 = comm_1_entry_4_1.get()
                comm_1_output_6 = comm_1_entry_5_1.get()
                
                #tab 2 get Serial/CAN Settings
                comm_2_output_1 = comm_2_entry_3_1.get()
                comm_2_output_2 = comm_2_entry_4_1.get()
                comm_2_output_3 = comm_2_entry_5_1.get()
                comm_2_output_4 = comm_2_entry_6_1.get()
                comm_2_output_5 = comm_2_entry_7_1.get()
                comm_2_output_6 = comm_2_entry_8_1.get()

                #tab 3 get Bluetooth settings
                comm_3_output_1 = comm_3_entry_3_1.get()
                comm_3_output_2 = comm_3_entry_4_1.get()
                comm_3_output_3 = comm_3_entry_5_1.get()
                comm_3_output_4 = comm_3_entry_6_1.get()
                comm_3_output_5 = comm_3_entry_7_1.get()
                comm_3_output_6 = comm_3_entry_8_1.get()

                #tab 4 get Wifi settings
                comm_4_output_1 = comm_4_entry_3_1.get()
                comm_4_output_2 = comm_4_entry_4_1.get()
                comm_4_output_3 = comm_4_entry_5_1.get()
                comm_4_output_4 = comm_4_entry_6_1.get()
                comm_4_output_5 = comm_4_entry_7_1.get()
                comm_4_output_6 = comm_4_entry_8_1.get()

                print("Tab_NUMBER: ", TAB_NUM)
                print("COM1_1: ", comm_1_output_1)
                print("COM1_2: ", comm_1_output_2)
                print("COM1_3: ", comm_1_output_3)
                print("COM1_4: ", comm_1_output_4)
                print("COM1_5: ", comm_1_output_5)
                print("COM1_6: ", comm_1_output_6)

                print("Tab_NUMBER: ", TAB_NUM)
                print("COM2_1: ", comm_2_output_1)
                print("COM2_2: ", comm_2_output_2)
                print("COM2_3: ", comm_2_output_3)
                print("COM2_4: ", comm_2_output_4)
                print("COM2_5: ", comm_2_output_5)
                print("COM2_6: ", comm_2_output_6)

                print("Tab_NUMBER: ", TAB_NUM)
                print("COM3_1: ", comm_3_output_1)
                print("COM3_2: ", comm_3_output_2)
                print("COM3_3: ", comm_3_output_3)
                print("COM3_4: ", comm_3_output_4)
                print("COM3_5: ", comm_3_output_5)
                print("COM3_6: ", comm_3_output_6)

                print("Tab_NUMBER: ", TAB_NUM)
                print("COM4_1: ", comm_4_output_1)
                print("COM4_2: ", comm_4_output_2)
                print("COM4_3: ", comm_4_output_3)
                print("COM4_4: ", comm_4_output_4)
                print("COM4_5: ", comm_4_output_5)
                print("COM4_6: ", comm_4_output_6)

        #tab 1, 2, 3, and 4 settings window menu labels
        comm_1_label_1_0 = Label(comm_tab_1, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        comm_1_label_2_0 = Label(comm_tab_2, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        comm_1_label_3_0 = Label(comm_tab_3, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        comm_1_label_4_0 = Label(comm_tab_4, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)

        #tab 1 settings menu buttons
        comm_1_btn_9_1 = Button(comm_tab_1, text="+").grid(row=9, column=1, sticky="wne")
        comm_1_btn_10_1 = Button(comm_tab_1, text="-").grid(row=10, column=1, sticky="wne")
        comm_1_btn_11_1 = Button(comm_tab_1, text="Setting_3").grid(row=11, column=1, sticky="wne")
        comm_1_btn_12_1 = Button(comm_tab_1, text="Setting_4").grid(row=12, column=1, sticky="wne")

        #tab 2 settings menu buttons
        comm_2_btn_9_1 = Button(comm_tab_2, text="+").grid(row=9, column=1, sticky="wne")
        comm_2_btn_10_1 = Button(comm_tab_2, text="-").grid(row=10, column=1, sticky="wne")
        comm_2_btn_11_1 = Button(comm_tab_2, text="Setting_3").grid(row=11, column=1, sticky="wne")
        comm_2_btn_12_1 = Button(comm_tab_2, text="Setting_4").grid(row=12, column=1, sticky="wne")
        def kill_set():
                Tabs.destroy()

        def submit():
                message1 = "Submitted"
                print("Message1: ", message1)
                get_entry(button_select)
                Tabs.destroy()

        #tab 1 settings menu buttons
        comm_1_btn_13_1 = Button(comm_tab_1, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        comm_1_btn_14_1 = Button(comm_tab_1, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #tab 2 settings menu buttons
        comm_2_btn_13_1 = Button(comm_tab_2, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        comm_2_btn_14_1 = Button(comm_tab_2, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #tab 1 settings menu window show entry boxes on screen
        comm_1_entry_3_1.grid(row=3, column=1, sticky="wne")
        comm_1_entry_4_1.grid(row=4, column=1, sticky="wne")
        comm_1_entry_5_1.grid(row=5, column=1, sticky="wne")
        comm_1_entry_6_1.grid(row=6, column=1, sticky="wne")
        comm_1_entry_7_1.grid(row=7, column=1, sticky="wne")
        comm_1_entry_8_1.grid(row=8, column=1, sticky="wne")

        #tab 2 settings menu window show entry boxes on screen
        comm_2_entry_3_1.grid(row=3, column=1, sticky="wne")
        comm_2_entry_4_1.grid(row=4, column=1, sticky="wne")
        comm_2_entry_5_1.grid(row=5, column=1, sticky="wne")
        comm_2_entry_6_1.grid(row=6, column=1, sticky="wne")
        comm_2_entry_7_1.grid(row=7, column=1, sticky="wne")
        comm_2_entry_8_1.grid(row=8, column=1, sticky="wne")

        #test - getting values from TCP settings entry boxes and display them into entry boxes below:
        #mw_1_entry_3_2.delete(0, END)
        #mw_1_entry_3_2.insert(END, comm_1_output_1)


        #test - getting values from  Serial/CAN settings entry boxes and display them into entry boxes below:
        #mw_1_entry_3_2.delete(0, END)
        #mw_1_entry_3_2.insert(END, comm_2_output_1)


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
		mw_1_entry_3_2.delete(0, END)
		mw_1_entry_3_2.insert(END, DATE)
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
        ctrl_1_label_2_0 = Label(control_1, text="Input Control").grid(row=2, column=0, sticky="wn", padx=5)
        ctrl_1_label_2_0 = Label(control_1, text="Value_0: ").grid(row=3, column=0, sticky="wn", padx=5)
        ctrl_1_label_4_0 = Label(control_1, text="Value_1: ").grid(row=4, column=0, sticky="wn", padx=5)
        ctrl_1_label_5_0 = Label(control_1, text="Value_2: ").grid(row=5, column=0, sticky="wn", padx=5)
        ctrl_1_label_6_0 = Label(control_1, text="Value_3: ").grid(row=6, column=0, sticky="wn", padx=5)
        ctrl_1_label_7_0 = Label(control_1, text="Value_4: ").grid(row=7, column=0, sticky="wn", padx=5)
        ctrl_1_label_8_0 = Label(control_1, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #control 2 menu label
        tabControl = ttk.Notebook(control_2)
        ctrl_2_label_2_0 = Label(control_2, text="Control Setting ").grid(row=2, column=0, sticky="wn", padx=5)
        ctrl_2_label_3_0 = Label(control_2, text="Value_0: ").grid(row=3, column=0, sticky="wn", padx=5)
        ctrl_2_label_4_0 = Label(control_2, text="Value_1: ").grid(row=4, column=0, sticky="wn", padx=5)
        ctrl_2_label_5_0 = Label(control_2, text="Value_2: ").grid(row=5, column=0, sticky="wn", padx=5)
        ctrl_2_label_6_0 = Label(control_2, text="Value_3: ").grid(row=6, column=0, sticky="wn", padx=5)
        ctrl_2_label_7_0 = Label(control_2, text="Value_4: ").grid(row=7, column=0, sticky="wn", padx=5)
        ctrl_2_label_8_0 = Label(control_2, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #control 3 menu label
        tabControl = ttk.Notebook(control_3)
        ctrl_3_label_2_0 = Label(control_3, text="Control Setting ").grid(row=2, column=0, sticky="wn", padx=5)
        ctrl_3_label_3_0 = Label(control_3, text="Value_0: ").grid(row=3, column=0, sticky="wn", padx=5)
        ctrl_3_label_4_0 = Label(control_3, text="Value_1: ").grid(row=4, column=0, sticky="wn", padx=5)
        ctrl_3_label_5_0 = Label(control_3, text="Value_2: ").grid(row=5, column=0, sticky="wn", padx=5)
        ctrl_3_label_6_0 = Label(control_3, text="Value_3 ").grid(row=6, column=0, sticky="wn", padx=5)
        ctrl_3_label_7_0 = Label(control_3, text="Value_4: ").grid(row=7, column=0, sticky="wn", padx=5)
        ctrl_3_label_8_0 = Label(control_3, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        #control 4 menu label
        tabControl = ttk.Notebook(control_4)
        ctrl_4_label_2_0 = Label(control_4, text="Control Setting ").grid(row=2, column=0, sticky="wn", padx=5)
        ctrl_4_label_3_0 = Label(control_4, text="Value_0: ").grid(row=3, column=0, sticky="wn", padx=5)
        ctrl_4_label_4_0 = Label(control_4, text="Value_1: ").grid(row=4, column=0, sticky="wn", padx=5)
        ctrl_4_label_5_0 = Label(control_4, text="Value_2: ").grid(row=5, column=0, sticky="wn", padx=5)
        ctrl_4_label_6_0 = Label(control_4, text="Value_3: ").grid(row=6, column=0, sticky="wn", padx=5)
        ctrl_4_label_7_0 = Label(control_4, text="Value_4: ").grid(row=7, column=0, sticky="wn", padx=5)
        ctrl_4_label_8_0 = Label(control_4, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)
        
        #control tab 1 entry box
        ctrl_1_entry_3_1 = Entry(control_1, width=20)
        ctrl_1_entry_4_1 = Entry(control_1, width=20)
        ctrl_1_entry_5_1 = Entry(control_1, width=20)
        ctrl_1_entry_6_1 = Entry(control_1, width=20)
        ctrl_1_entry_7_1 = Entry(control_1, width=20)
        ctrl_1_entry_8_1 = Entry(control_1, width=20)

        #control tab 2 entry box
        ctrl_2_entry_3_1 = Entry(control_2, width=20)
        ctrl_2_entry_4_1 = Entry(control_2, width=20)
        ctrl_2_entry_5_1 = Entry(control_2, width=20)
        ctrl_2_entry_6_1 = Entry(control_2, width=20)
        ctrl_2_entry_7_1 = Entry(control_2, width=20)
        ctrl_2_entry_8_1 = Entry(control_2, width=20)

        #control tab 3 entry box
        ctrl_3_entry_3_1 = Entry(control_3, width=20)
        ctrl_3_entry_4_1 = Entry(control_3, width=20)
        ctrl_3_entry_5_1 = Entry(control_3, width=20)
        ctrl_3_entry_6_1 = Entry(control_3, width=20)
        ctrl_3_entry_7_1 = Entry(control_3, width=20)
        ctrl_3_entry_8_1 = Entry(control_3, width=20)

        #control tab 4 entry box
        ctrl_4_entry_3_1 = Entry(control_4, width=20)
        ctrl_4_entry_4_1 = Entry(control_4, width=20)
        ctrl_4_entry_5_1 = Entry(control_4, width=20)
        ctrl_4_entry_6_1 = Entry(control_4, width=20)
        ctrl_4_entry_7_1 = Entry(control_4, width=20)
        ctrl_4_entry_8_1 = Entry(control_4, width=20)

        #get control 1, 2, 3, and 4 entries from entry box
        def get_entry(TAB_NUM):
                #control tab 1
                global ctrl_1_output_1 # Value_0
                global ctrl_1_output_2 # Value_1
                global ctrl_1_output_3 # Value_2
                global ctrl_1_ourput_3 # Value_3
                global ctrl_1_output_4 # Value_4
                global ctrl_1_output_5 # Value_5
                global ctrl_1_output_6 # Value_6

                #control tab 2
                global ctrl_2_output_1 # Value_0
                global ctrl_2_output_2 # Value_1
                global ctrl_2_output_3 # Value_2
                global ctrl_2_output_4 # Value_3
                global ctrl_2_output_5 # Value_4
                global ctrl_2_output_6 # Value_5

                #control tab 3
                global ctrl_3_output_1 # Value_0
                global ctrl_3_output_2 # Value_1
                global ctrl_3_output_3 # Value_2
                global ctrl_3_output_4 # Value_3
                global ctrl_3_output_5 # Value_4
                global ctrl_3_output_6 # Value_5

                #control tab 4
                global ctrl_4_output_1 # Value_0
                global ctrl_4_output_2 # Value_1
                global ctrl_4_output_3 # Value_2
                global ctrl_4_output_4 # Value_3
                global ctrl_4_output_5 # Value_4
                global ctrl_4_output_6 # Value_5

                #control tab 1 get Values 0, 1, 2, 3, 4, 5
                ctrl_1_output_1 = ctrl_1_entry_3_1.get()
                ctrl_1_output_2 = ctrl_1_entry_4_1.get()
                ctrl_1_output_3 = ctrl_1_entry_5_1.get()
                ctrl_1_output_4 = ctrl_1_entry_6_1.get()
                ctrl_1_output_5 = ctrl_1_entry_7_1.get()
                ctrl_1_output_6 = ctrl_1_entry_8_1.get()

                #test - getting values from TCP settings entry boxes and display them into entry boxes below:
                mw_1_entry_3_2.delete(0, END)
                mw_1_entry_3_2.insert(END, ctrl_1_output_1)
                mw_1_entry_4_2.delete(0, END)
                mw_1_entry_4_2.insert(END, ctrl_1_output_2)
                mw_1_entry_5_2.delete(0, END)
                mw_1_entry_5_2.insert(END, ctrl_1_output_3)
                mw_1_entry_6_2.delete(0, END)
                mw_1_entry_6_2.insert(END, ctrl_1_output_4)
                mw_1_entry_7_2.delete(0, END)
                mw_1_entry_8_2.insert(END, ctrl_1_output_5)
                mw_1_entry_9_2.delete(0, END)
                mw_1_entry_10_2.insert(END, ctrl_1_output_6)
                mw_1_entry_11_2.insert(END, COUNT)
                
                #tab 2 get Serial/CAN Settings
                ctrl_2_output_1 = ctrl_2_entry_3_1.get()
                ctrl_2_output_2 = ctrl_2_entry_4_1.get()
                ctrl_2_output_3 = ctrl_2_entry_5_1.get()
                ctrl_2_output_4 = ctrl_2_entry_6_1.get()
                ctrl_2_output_5 = ctrl_2_entry_7_1.get()
                ctrl_2_output_6 = ctrl_2_entry_8_1.get()

                #tab 3 get Bluetooth settings
                ctrl_3_output_1 = ctrl_3_entry_3_1.get()
                ctrl_3_output_2 = ctrl_3_entry_4_1.get()
                ctrl_3_output_3 = ctrl_3_entry_5_1.get()
                ctrl_3_output_4 = ctrl_3_entry_6_1.get()
                ctrl_3_output_5 = ctrl_3_entry_7_1.get()
                ctrl_3_output_6 = ctrl_3_entry_8_1.get()

                #tab 4 get Wifi settings
                ctrl_4_output_1 = ctrl_4_entry_3_1.get()
                ctrl_4_output_2 = ctrl_4_entry_4_1.get()
                ctrl_4_output_3 = ctrl_4_entry_5_1.get()
                ctrl_4_output_4 = ctrl_4_entry_6_1.get()
                ctrl_4_output_5 = ctrl_4_entry_7_1.get()
                ctrl_4_output_6 = ctrl_4_entry_8_1.get()

                #test - getting values from  Serial/CAN settings entry boxes and display them into entry boxes below:
                mw_1_entry_3_2.delete(0, END)
                mw_1_entry_4_2.insert(END, ctrl_2_entry_3_1.get())
                mw_1_entry_5_2.delete(0, END)
                mw_1_entry_6_2.insert(END, ctrl_2_entry_4_1.get())
                mw_1_entry_7_2.delete(0, END)
                mw_1_entry_8_2.insert(END, ctrl_2_entry_5_1.get())
                mw_1_entry_9_2.delete(0, END)
                mw_1_entry_10_2.insert(END, ctrl_2_entry_6_1.get())
                mw_1_entry_11_2.delete(0, END)
                mw_1_entry_12_2.insert(END, ctrl_2_entry_7_1.get())
                mw_1_entry_13_2.delete(0, END)
                mw_1_entry_14_2.insert(END, ctrl_2_entry_8_1.get())

                print("Tab_NUMBER: ", TAB_NUM)
                print("C0: ", ctrl_1_output_1)
                print("C1: ", ctrl_1_output_2)
                print("C2: ", ctrl_1_output_3)
                print("C3: ", ctrl_1_output_4)
                print("C4: ", ctrl_1_output_5)
                print("C5: ", ctrl_1_output_6)

        #up counter
        def count_up():
                COUNT = 0
                global OUTPUT
                COUNT = COUNT + 1
                OUTPUT = COUNT
                ctrl_1_entry_3_1.delete(0, END)
                ctrl_1_entry_3_1.insert(END, COUNT)

        #down counter
        def count_down():
                COUNT = 0
                global OUTPUT
                COUNT = COUNT - 1
                OUTPUT = COUNT
                ctrl_1_entry_3_1.delete(0, END)
                ctrl_1_entry_3_1.insert(END, COUNT)


        #c_1_0.delete(0, END)
        #c_1_0.insert(END, output)

        #control tab 1, 2, 3, and 4 main window channel label
        channel1_select = "1"
        channel2_select = "2"
        channel3_select = "3"
        channel4_select = "4"
        ctrl_1_label_0_0 = Label(control_1, text="Channel: {}".format(channel1_select)).grid(row=0, column=0, sticky="wn", padx=5)
        ctrl_2_label_0_0 = Label(control_2, text="Channel: {}".format(channel2_select)).grid(row=0, column=0, sticky="wn", padx=5)
        ctrl_3_label_0_0 = Label(control_3, text="Channel: {}".format(channel3_select)).grid(row=0, column=0, sticky="wn", padx=5)
        ctrl_4_label_0_0 = Label(control_4, text="Channel: {}".format(channel4_select)).grid(row=0, column=0, sticky="wn", padx=5)

        #control tab 1 buttons
        ctrl_1_btn_9_1 = Button(control_1, text="Up", command=count_up).grid(row=9, column=1, sticky="wne", pady=5)
        ctrl_1_btn_10_1 = Button(control_1, text="Down", command=count_down).grid(row=10, column=1, sticky="wne", pady=5)
        ctrl_1_btn_11_1 = Button(control_1, text="Setting_3").grid(row=11, column=1, sticky="wne")
        ctrl_1_btn_12_1 = Button(control_1, text="Setting_4").grid(row=12, column=1, sticky="wne")
        ctrl_1_btn_9_2 = Button(control_1, text="Left").grid(row=9, column=2, sticky="wne", padx=5, pady=5)
        ctrl_1_btn_9_3 = Button(control_1, text="Right").grid(row=9, column=3, sticky="wne", padx=5, pady=5)

        #control tab 2 buttons
        ctrl_2_btn_9_1 = Button(control_2, text="+", command=count_up).grid(row=9, column=1, sticky="wne")
        ctrl_2_btn_10_1 = Button(control_2, text="-", command=count_down).grid(row=10, column=1, sticky="wne")
        ctrl_2_btn_11_1 = Button(control_2, text="Setting_3").grid(row=11, column=1, sticky="wne")
        ctrl_2_btn_12_1 = Button(control_2, text="Setting_4").grid(row=12, column=1, sticky="wne")
        def kill_set():
                troubleshooter.destroy()

        def submit():
                message1 = "Submitted"
                print("Message1: ", message1)
                troubleshooter.destroy()

        #control tab 1 buttons
        ctrl_1_btn_13_1 = Button(control_1, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        ctrl_1_btn_14_1 = Button(control_1, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #control tab 2 buttons
        ctrl_2_btn_13_1 = Button(control_2, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        ctrl_2_btn_14_1 = Button(control_2, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #control tab 1 entry boxes on screen
        ctrl_1_entry_3_1.grid(row=3, column=1, sticky="wne")
        ctrl_1_entry_4_1.grid(row=4, column=1, sticky="wne")
        ctrl_1_entry_5_1.grid(row=5, column=1, sticky="wne")
        ctrl_1_entry_6_1.grid(row=6, column=1, sticky="wne")
        ctrl_1_entry_7_1.grid(row=7, column=1, sticky="wne")
        ctrl_2_entry_8_1.grid(row=8, column=1, sticky="wne")

        #control tab 2 show entry boxes on screen
        ctrl_2_entry_3_1.grid(row=3, column=1, sticky="wne")
        ctrl_2_entry_4_1.grid(row=4, column=1, sticky="wne")
        ctrl_2_entry_5_1.grid(row=5, column=1, sticky="wne")
        ctrl_2_entry_6_1.grid(row=6, column=1, sticky="wne")
        ctrl_2_entry_7_1.grid(row=7, column=1, sticky="wne")
        ctrl_2_entry_8_1.grid(row=8, column=1, sticky="wne")
        troubleshooter.mainloop()

#main window (mw_{window number}_widget ID (Button or Entry)_{row position}).format(a, b)
#tab 1 main window entry box
#window = Frame(window, relief=RAISED, bd=2)
mw_1_entry_3_2 = Entry(window, width=10)
mw_1_entry_4_2 = Entry(window, width=100)
mw_1_entry_5_2 = Entry(window, width=10)
mw_1_entry_6_2 = Entry(window, width=10)
mw_1_entry_7_2 = Entry(window, width=10)
mw_1_entry_8_2 = Entry(window, width=10)
mw_1_entry_9_2 = Entry(window, width=10) 
mw_1_entry_10_2 = Entry(window, width=10) 
mw_1_entry_11_2 = Entry(window, width=10) 
mw_1_entry_12_2 = Entry(window, width=10)
mw_1_entry_13_2 = Entry(window, width=10)
mw_1_entry_14_2 = Entry(window, width=10)
mw_1_entry_15_2 = Entry(window, width=10)
mw_1_entry_16_2 = Entry(window, width=10)
mw_1_entry_17_2 = Entry(window, width=10)
mw_1_entry_18_2 = Entry(window, width=10)

#tab 1 main window buttons
mw_1_btn_2_0 = Button(window, text="Import video", command=file1).grid(row=2, column=0, sticky="ew", padx=5)
mw_1_btn_3_0 = Button(window, text="Button_00", command=button_0).grid(row=3, column=0, sticky="ew", padx=5)
mw_1_btn_4_0 = Button(window, text="Button_01", command=button_1).grid(row=4, column=0, sticky="ew", padx=5)
mw_1_btn_5_0 = Button(window, text="Button_02", command=button_2).grid(row=5, column=0, sticky="ew", padx=5)
mw_1_btn_6_0 = Button(window, text="Button_03", command=button_3).grid(row=6, column=0, sticky="ew", padx=5)
mw_1_btn_7_0 = Button(window, text="Button_04", command=button_4).grid(row=7, column=0, sticky="ew", padx=5)
mw_1_btn_8_0 = Button(window, text="Button_05", command=button_5).grid(row=8, column=0, sticky="ew", padx=5)
mw_1_btn_9_0 = Button(window, text="Button_06", command=button_5).grid(row=9, column=0, sticky="ew", padx=5)
mw_1_btn_10_0 = Button(window, text="Button_07", command=button_0).grid(row=10, column=0, sticky="ew", padx=5)
mw_1_btn_11_0 = Button(window, text="Button_08", command=button_1).grid(row=11, column=0, sticky="ew", padx=5)
mw_1_btn_12_0 = Button(window, text="Button_09", command=button_2).grid(row=12, column=0, sticky="ew", padx=5)
mw_1_btn_13_0 = Button(window, text="Button_10", command=button_3).grid(row=13, column=0, sticky="ew", padx=5)
mw_1_btn_14_0 = Button(window, text="Button_11", command=button_4).grid(row=14, column=0, sticky="ew", padx=5)
mw_1_btn_15_0 = Button(window, text="Button_12", command=button_5).grid(row=15, column=0, sticky="ew", padx=5)
mw_1_btn_16_0 = Button(window, text="Button_13", command=button_5).grid(row=16, column=0, sticky="ew", padx=5)
mw_1_btn_17_0 = Button(window, text="Button_14", command=button_5).grid(row=17, column=0, sticky="ew", padx=5)
mw_1_btn_stop_23_0 = Button(window, text="Stop", command=stop).grid(row=23, column=0, sticky="ew", padx=5)

#tab 2 main window buttons
mw_2_btn_5_0 = Button(window_1, text="Troubleshooter", command=troubleshoot_wizard).grid(row=5, column=0, sticky="ew", padx=5)

#tab 1 main window settings button
mw_1_btn_3_3 = Button(window, text="+", command=lambda:settings_menu(0)).grid(row=3, column=3, sticky="ew", padx=5)
mw_1_btn_4_3 = Button(window, text="+", command=lambda:settings_menu(1)).grid(row=4, column=3, sticky="ew", padx=5)
mw_1_btn_5_3 = Button(window, text="+", command=lambda:settings_menu(2)).grid(row=5, column=3, sticky="ew", padx=5)
mw_1_btn_6_3 = Button(window, text="+", command=lambda:settings_menu(3)).grid(row=6, column=3, sticky="ew", padx=5)
mw_1_btn_7_3 = Button(window, text="+", command=lambda:settings_menu(4)).grid(row=7, column=3, sticky="ew", padx=5)
mw_1_btn_8_3 = Button(window, text="+",command=lambda:settings_menu(5) ).grid(row=8, column=3, sticky="ew", padx=5)
mw_1_btn_9_3 = Button(window, text="+", command=lambda:settings_menu(6)).grid(row=9, column=3, sticky="ew", padx=5)
mw_1_btn_10_3 = Button(window, text="+", command=lambda:settings_menu(7)).grid(row=10, column=3, sticky="ew", padx=5)
mw_1_btn_11_3 = Button(window, text="+", command=lambda:settings_menu(8)).grid(row=11, column=3, sticky="ew", padx=5)
mw_1_btn_12_3 = Button(window, text="+", command=lambda:settings_menu(9)).grid(row=12, column=3, sticky="ew", padx=5)
mw_1_btn_13_3 = Button(window, text="+", command=lambda:settings_menu(10)).grid(row=13, column=3, sticky="ew", padx=5)
mw_1_btn_14_3 = Button(window, text="+", command=lambda:settings_menu(11)).grid(row=14, column=3, sticky="ew", padx=5)
mw_1_btn_15_3 = Button(window, text="+", command=lambda:settings_menu(12)).grid(row=15, column=3, sticky="ew", padx=5)
mw_1_btn_16_3 = Button(window, text="+", command=lambda:settings_menu(13)).grid(row=16, column=3, sticky="ew", padx=5)
mw_1_btn_17_3 = Button(window, text="+", command=lambda:settings_menu(14)).grid(row=17, column=3, sticky="ew", padx=5)
mw_1_btn_set_date_17_3 = Button(window, text = "Select Date", command = set_date).grid(row=18, column=0, sticky="ew", padx=5) # tab 1 main window
mw_1_btn_Import_file_19_0 = Button(window, text="Expot port file", command=file0).grid(row=19, column=0, sticky="ew", padx=5) # tab 1 main window
mw_1_btn_add_camera_20_0 = Button(window, text="Add Camera", command=add_camera).grid(row=20, column=0, sticky="ew", padx=5) # tab 1 main window
mw_1_btn_clear_21_0 = Button(window, text="Clear", command=clear).grid(row=21, column=0, sticky="ew", padx=5) # tab 1 main window
mw_1_btn_exit_24_0 = Button(window, text="Exit", command=exit).grid(row=24, column=0, sticky="ew", padx=5) #tab 1 main window

#tab 1 main window labels
mw_1_label_0_0 = Label(window, text="Debugger1 Status:").grid(row=0, column=0, sticky="wne", padx=5) #tab 1 main window
mw_1_label_3_1 = Label(window, text="00: ").grid(row=3, column=1, sticky="wn", padx=5)
mw_1_label_4_1 = Label(window, text="01: ").grid(row=4, column=1, sticky="wn", padx=5)
mw_1_label_5_1 = Label(window, text="02: ").grid(row=5, column=1, sticky="wn", padx=5)
mw_1_label_6_1 = Label(window, text="03: ").grid(row=6, column=1, sticky="wn", padx=5)
mw_1_label_7_1 = Label(window, text="04: ").grid(row=7, column=1, sticky="wn", padx=5)
mw_1_label_8_1 = Label(window, text="05: ").grid(row=8, column=1, sticky="wn", padx=5)
mw_1_label_9_1 = Label(window, text="06: ").grid(row=9, column=1, sticky="wn", padx=5)
mw_1_label_10_1 = Label(window, text="07: ").grid(row=10, column=1, sticky="wn", padx=5)
mw_1_label_11_1 = Label(window, text="08: ").grid(row=11, column=1, sticky="wn", padx=5)
mw_1_label_12_1 = Label(window, text="09: ").grid(row=12, column=1, sticky="wn", padx=5)
mw_1_label_13_1 = Label(window, text="10: ").grid(row=13, column=1, sticky="wn", padx=5)
mw_1_label_14_1 = Label(window, text="11: ").grid(row=14, column=1, sticky="wn", padx=5)
mw_1_label_15_1 = Label(window, text="12: ").grid(row=15, column=1, sticky="wn", padx=5)
mw_1_label_16_1 = Label(window, text="13: ").grid(row=16, column=1, sticky="wn", padx=5)
mw_1_label_17_1 = Label(window, text="14: ").grid(row=17, column=1, sticky="wn", padx=5)

#tab 2 main window label
mw_2_label_3_0 = Label(window_1, text="Diagnostics: ").grid(row=3, column=0, sticky="wn", padx=5)

#tab 1 show main window entry box
mw_1_entry_3_2.grid(row=3, column=2, sticky="wne", padx=5)
mw_1_entry_4_2.grid(row=4, column=2, sticky="wne", padx=5)
mw_1_entry_5_2.grid(row=5, column=2, sticky="wne", padx=5)
mw_1_entry_6_2.grid(row=6, column=2, sticky="wne", padx=5)
mw_1_entry_7_2.grid(row=7, column=2, sticky="wne", padx=5)
mw_1_entry_8_2.grid(row=8, column=2, sticky="wne", padx=5)
mw_1_entry_9_2.grid(row=9, column=2, sticky="wne", padx=5)
mw_1_entry_10_2.grid(row=10, column=2, sticky="wne", padx=5)
mw_1_entry_11_2.grid(row=11, column=2, sticky="wne", padx=5)
mw_1_entry_12_2.grid(row=12, column=2, sticky="wne", padx=5)
mw_1_entry_13_2.grid(row=13, column=2, sticky="wne", padx=5)
mw_1_entry_14_2.grid(row=14, column=2, sticky="wne", padx=5)
mw_1_entry_15_2.grid(row=15, column=2, sticky="wne", padx=5)
mw_1_entry_16_2.grid(row=16, column=2, sticky="wne", padx=5)
mw_1_entry_17_2.grid(row=17, column=2, sticky="wne", padx=5)
mw_1_entry_18_2.grid(row=18, column=2, sticky="wne", padx=5)

#create main window
window_tabs.mainloop()

