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
banner_speed = 0
BANNER = 0
RED = 255  # 0 - 255
BLUE = 255 # 0 - 255
GREEN = 255 # 0 - 255
x,y,w,h = 0,640,560,100
width = 1280
height = 720
button1 = False
button5 = False
forward = False
back = False
button2 = False
count = 0

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
                        count = count + 1
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
                entry102.insert(END, banner_speed)
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
	

def button_1():
	global button1
	button1 = not button1
	print('Pause again: ', button1)
	#btn_set1()
	

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
        global back
        back = not back
        print('Back: ', back)
        entry102.delete(0, END)
        entry102.insert(END, back)
        

def button_4():
	global forward
	forward = not forward
	print('Forward: ', forward)
	

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
	

#settings tab
def communication_wizard(object):
        Tabs = Tk()
        Tabs.geometry("400x400")
        Tabs.title("Connection Wizard")
        tabControl = ttk.Notebook(Tabs)

        tab_1 = ttk.Frame(tabControl)
        tab_2 = ttk.Frame(tabControl)
        tab_3 = ttk.Frame(tabControl)
        tab_4 = ttk.Frame(tabControl)

        tabControl.add(tab_1, text ='TCP')
        tabControl.add(tab_2, text ='Serial')
        tabControl.add(tab_3, text ='Bluetooth')
        tabControl.add(tab_4, text ='Wifi')
        tabControl.pack(expand = 8, fill ="both")

        tabControl = ttk.Notebook(tab_1)
        l1 = Label(tab_1, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        l1 = Label(tab_1, text="IP address: ").grid(row=3, column=0, sticky="wn", padx=5)
        l2 = Label(tab_1, text="Subnet mask: ").grid(row=4, column=0, sticky="wn", padx=5)
        l3 = Label(tab_1, text="Default gateway: ").grid(row=5, column=0, sticky="wn", padx=5)
        l4 = Label(tab_1, text="Prefered DNS server: ").grid(row=6, column=0, sticky="wn", padx=5)
        l5 = Label(tab_1, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        l6 = Label(tab_1, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        tabControl = ttk.Notebook(tab_2)
        l1 = Label(tab_2, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        l1 = Label(tab_2, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        l2 = Label(tab_2, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        l3 = Label(tab_2, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        l4 = Label(tab_2, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        l5 = Label(tab_2, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        l6 = Label(tab_2, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        tabControl = ttk.Notebook(tab_3)
        l1 = Label(tab_3, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        l1 = Label(tab_3, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        l2 = Label(tab_3, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        l3 = Label(tab_3, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        l4 = Label(tab_3, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        l5 = Label(tab_3, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        l6 = Label(tab_3, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)

        tabControl = ttk.Notebook(tab_4)
        l1 = Label(tab_4, text="Settings ").grid(row=0, column=0, sticky="wn", padx=5)
        l1 = Label(tab_4, text="COM: ").grid(row=3, column=0, sticky="wn", padx=5)
        l2 = Label(tab_4, text="Speed (baud): ").grid(row=4, column=0, sticky="wn", padx=5)
        l3 = Label(tab_4, text="Data bits: ").grid(row=5, column=0, sticky="wn", padx=5)
        l4 = Label(tab_4, text="Stop bit: ").grid(row=6, column=0, sticky="wn", padx=5)
        l5 = Label(tab_4, text="Port: ").grid(row=7, column=0, sticky="wn", padx=5)
        l6 = Label(tab_4, text="N/A: ").grid(row=8, column=0, sticky="wn", padx=5)
        
        #creat entry boxes
        e_1_0 = Entry(tab_1, width=20)
        e_1_1 = Entry(tab_1, width=20)
        e_1_2 = Entry(tab_1, width=20)
        e_1_3 = Entry(tab_1, width=20)
        e_1_4 = Entry(tab_1, width=20)
        e_1_5 = Entry(tab_1, width=20)

        e_2_0 = Entry(tab_2, width=20)
        e_2_1 = Entry(tab_2, width=20)
        e_2_2 = Entry(tab_2, width=20)
        e_2_3 = Entry(tab_2, width=20)
        e_2_4 = Entry(tab_2, width=20)
        e_2_5 = Entry(tab_2, width=20)

        e_3_0 = Entry(tab_3, width=20)
        e_3_1 = Entry(tab_3, width=20)
        e_3_2 = Entry(tab_3, width=20)
        e_3_3 = Entry(tab_3, width=20)
        e_3_4 = Entry(tab_3, width=20)
        e_3_5 = Entry(tab_3, width=20)

        e_4_0 = Entry(tab_4, width=20)
        e_4_1 = Entry(tab_4, width=20)
        e_4_2 = Entry(tab_4, width=20)
        e_4_3 = Entry(tab_4, width=20)
        e_4_4 = Entry(tab_4, width=20)
        e_4_5 = Entry(tab_4, width=20)


        def get_entry(TAB_NUM):
                global e100
                global e101
                global e102
                global e103
                global e104
                global e105

                global e200
                global e201
                global e202
                global e203
                global e204
                global e205

                global e300
                global e301
                global e302
                global e303
                global e304
                global e305

                global e400
                global e401
                global e402
                global e403
                global e404
                global e405

                #TCP settings
                e100 = e_1_0.get()
                e101 = e_1_1.get()
                e102 = e_1_2.get()
                e103 = e_1_3.get()
                e104 = e_1_4.get()
                e105 = e_1_5.get()

                entry100.delete(0, END)
                entry100.insert(END, e_1_0.get())
                entry101.delete(0, END)
                entry101.insert(END, e_1_1.get())
                entry102.delete(0, END)
                entry102.insert(END, e_1_2.get())
                entry103.delete(0, END)
                entry103.insert(END, e_1_3.get())
                entry104.delete(0, END)
                entry104.insert(END, e_1_4.get())
                entry105.delete(0, END)
                entry105.insert(END, e_1_5.get())
                
                #Serial/CAN Settings
                e200 = e_2_0.get()
                e201 = e_2_1.get()
                e202 = e_2_2.get()
                e203 = e_2_3.get()
                e204 = e_2_4.get()
                e205 = e_2_5.get()


                #Bluetooth Settings
                e300 = e_3_0.get()
                e301 = e_3_1.get()
                e302 = e_3_2.get()
                e303 = e_3_3.get()
                e304 = e_3_4.get()
                e305 = e_3_5.get()

                #Wifi Settings
                e400 = e_4_0.get()
                e401 = e_4_1.get()
                e402 = e_4_2.get()
                e403 = e_4_3.get()
                e404 = e_4_4.get()
                e405 = e_4_5.get()

                #Example insert data from menu tab2 into main window entry box
                entry107.delete(0, END)
                entry107.insert(END, e_2_0.get())
                entry108.delete(0, END)
                entry108.insert(END, e_2_1.get())
                entry109.delete(0, END)
                entry109.insert(END, e_2_2.get())
                entry110.delete(0, END)
                entry110.insert(END, e_2_3.get())
                entry111.delete(0, END)
                entry112.insert(END, e_2_4.get())
                entry113.delete(0, END)
                entry114.insert(END, e_2_0.get())

                print("Tab_NUMBER: ", TAB_NUM)
                print("E0: ", e100)
                print("E1: ", e101)
                print("E2: ", e102)
                print("E3: ", e103)
                print("E4: ", e104)
                print("E5: ", e105)

        #create channel labels
        e_label1 = Label(tab_1, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        e_label2 = Label(tab_2, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        e_label3 = Label(tab_3, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)
        e_label4 = Label(tab_4, text="Channel: {}".format(button_select)).grid(row=0, column=0, sticky="wn", padx=5)

        #create buttons
        Button(tab_1, text="+").grid(row=9, column=1, sticky="wne")
        Button(tab_1, text="-").grid(row=10, column=1, sticky="wne")
        Button(tab_1, text="Setting_3").grid(row=11, column=1, sticky="wne")
        Button(tab_1, text="Settings_4").grid(row=12, column=1, sticky="wne")

        Button(tab_2, text="+").grid(row=9, column=1, sticky="wne")
        Button(tab_2, text="-").grid(row=10, column=1, sticky="wne")
        Button(tab_2, text="Setting_3").grid(row=11, column=1, sticky="wne")
        Button(tab_2, text="Settings_4").grid(row=12, column=1, sticky="wne")
        def kill_set():
                Tabs.destroy()

        def submit():
                message1 = "Submitted"
                print("Message1: ", message1)
                get_entry(button_select)
                Tabs.destroy()


        Button(tab_1, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        Button(tab_1, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")
        
        Button(tab_2, text="Submit", command=submit).grid(row=13, column=1, sticky="wne")
        Button(tab_2, text="Exit", command=kill_set).grid(row=14, column=1, sticky="wne")

        #show entry boxes on screen
        e_1_0.grid(row=3, column=1, sticky="wne")
        e_1_1.grid(row=4, column=1, sticky="wne")
        e_1_2.grid(row=5, column=1, sticky="wne")
        e_1_3.grid(row=6, column=1, sticky="wne")
        e_1_4.grid(row=7, column=1, sticky="wne")
        e_2_5.grid(row=8, column=1, sticky="wne")

        e_2_0.grid(row=3, column=1, sticky="wne")
        e_2_1.grid(row=4, column=1, sticky="wne")
        e_2_2.grid(row=5, column=1, sticky="wne")
        e_2_3.grid(row=6, column=1, sticky="wne")
        e_2_4.grid(row=7, column=1, sticky="wne")
        e_2_5.grid(row=8, column=1, sticky="wne")
        Tabs.mainloop()

def settings_menu(object):
        global button1
        global button_select
        button_select = object
        button1 = not button1
        print('Pause again: ', button1)
        communication_wizard(object)
                
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


#main screen
window_tabs = Tk()
window_tabs.geometry("800x800")
window_tabs.title("Debugger1")
tabControl = ttk.Notebook(window_tabs)

window = ttk.Frame(tabControl)
window_1 = ttk.Frame(tabControl)

tabControl.add(window, text ='Sensor')
tabControl.add(window_1, text ='Diagnostics')
tabControl.pack(expand = 1, fill ="both")

#entry box
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

#buttons
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


#settings button
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

#labels
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


#show entry box
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

#create window
window_tabs.mainloop()

