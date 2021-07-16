#Date: 6/20/2021
#Author: Robert Lyttle

##import libraries
import numpy as np
import os
import sys
import datetime
import time
import glob
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter.filedialog import askopenfilename, asksaveasfilename
import datetime
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
        def __init__(self, x,VIDEO_DATE, FILE):
                self.x = x
                self.VIDEO_DATE = VIDEO_DATE
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
                entry.delete(0, END)
                entry.insert(END, BANNER[0])
                entry5.delete(0, END)
                entry5.insert(END, BANNER[3])
                entry6.delete(0, END)
                entry6.insert(END, banner_speed)
                entry7.delete(0, END)
                entry7.insert(END, BANNER[5])
                entry8.delete(0, END)
                entry8.insert(END, BANNER[10])
                entry9.delete(0, END)
                entry9.insert(END, BANNER[11])
                entry10.delete(0, END)
                entry10.insert(END, BANNER[6])
                entry11.delete(0, END)
                entry11.insert(END, BANNER[12])

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
	entry12.delete(0, END)
	entry12.insert(END, FILE)
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
	entry1.delete(0, END)
	entry1.insert(END, FILE2)
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
        def run():
                Debugger1.command_1()
                entry1.delete(0, END)
                entry1.insert(END, count)
                print("Button_4")
                

        thread1 = threading.Thread(target=run)
        thread1.start()
        print(button2)

def button_3():
        global back
        back = not back
        print('Back: ', back)
        entry.delete(0, END)
        entry.insert(END, back)
        

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
        entry.delete(0, END)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
        entry8.delete(0, END)
        entry9.delete(0, END)
        entry10.delete(0, END)
        entry11.delete(0, END)
        entry12.delete(0, END)
        entry13.delete(0, END)
        entry14.delete(0, END)

        

def add_camera():
	global camera
	camera = entry1.get()
	print('Camera: ',camera)
	entry1.delete(0, END)
	

def stop():
	stop = True
	entry2.delete(0, END)
	entry3.delete(0, END)
	entry4.delete(0, END)
	entry5.delete(0, END)
	entry6.delete(0, END)
	entry7.delete(0, END)
	entry8.delete(0, END)
	entry9.delete(0, END)
	entry10.delete(0, END)
	entry11.delete(0, END)
	print(stop)
	

def exit():
	global stop
	stop = True
	entry1.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)
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
        tabControl.pack(expand = 1, fill ="both")

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
                global e0
                global e1
                global e2
                global e3
                global e4
                global e5
                entry_box = 0
                if TAB_NUM <= 7:
                        entry_box = 1
                        e0 = e_1_0.get()
                        e1 = e_1_1.get()
                        e2 = e_1_2.get()
                        e3 = e_1_3.get()
                        e4 = e_1_4.get()
                        e5 = e_1_5.get()


                        entry.delete(0, END)
                        entry.insert(END, e0)
                        entry1.delete(0, END)
                        entry1.insert(END, e1)
                        entry2.delete(0, END)
                        entry2.insert(END, e2)
                        entry3.delete(0, END)
                        entry3.insert(END, e3)
                        entry4.delete(0, END)
                        entry4.insert(END, e4)
                        entry5.delete(0, END)
                        entry5.insert(END, e5)
                

                elif TAB_NUM >= 8:
                        entry_box = 2
                        e0 = e_2_0.get()
                        e1 = e_2_1.get()
                        e2 = e_2_2.get()
                        e3 = e_2_3.get()
                        e4 = e_2_4.get()
                        e5 = e_2_5.get()

                        entry7.delete(0, END)
                        entry7.insert(END, e0)
                        entry8.delete(0, END)
                        entry8.insert(END, e1)
                        entry9.delete(0, END)
                        entry9.insert(END, e2)
                        entry10.delete(0, END)
                        entry10.insert(END, e3)
                        entry11.delete(0, END)
                        entry12.insert(END, e4)
                        entry13.delete(0, END)
                        entry14.insert(END, e5)


                print("Tab_NUMBER: ", TAB_NUM)
                print("Entry box number: ", entry_box)
                print("E0: ", e0)
                print("E1: ", e1)
                print("E2: ", e2)
                print("E3: ", e3)
                print("E4: ", e4)
                print("E5: ", e5)



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
		global VIDEO_DATE
		VIDEO_DATE  = '0{}/0{}/{}'.format(day, month, year)
		entry.delete(0, END)
		entry.insert(END, VIDEO_DATE)
		print('Date: ', VIDEO_DATE)
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
entry = Entry(window, width=10)
entry1 = Entry(window, width=100)
entry2 = Entry(window, width=10)
entry3 = Entry(window, width=10)
entry4 = Entry(window, width=10)
entry5 = Entry(window, width=10)
entry6 = Entry(window, width=10) 
entry7 = Entry(window, width=10) 
entry8 = Entry(window, width=10) 
entry9 = Entry(window, width=10)
entry10 = Entry(window, width=10)
entry11 = Entry(window, width=10)
entry12 = Entry(window, width=10)
entry13 = Entry(window, width=10)
entry14 = Entry(window, width=10)
entry15 = Entry(window, width=10)

#buttons
btn_file1 = Button(window, text="Import video", command=file1).grid(row=2, column=0, sticky="ew", padx=5)
btn_1 = Button(window, text="Button_00", command=button_0).grid(row=3, column=0, sticky="ew", padx=5)
btn_2 = Button(window, text="Button_01", command=button_1).grid(row=4, column=0, sticky="ew", padx=5)
btn_3 = Button(window, text="Button_02", command=button_2).grid(row=5, column=0, sticky="ew", padx=5)
btn_4 = Button(window, text="Button_03", command=button_3).grid(row=6, column=0, sticky="ew", padx=5)
btn_5 = Button(window, text="Button_04", command=button_4).grid(row=7, column=0, sticky="ew", padx=5)
btn_6 = Button(window, text="Button_05", command=button_5).grid(row=8, column=0, sticky="ew", padx=5)
btn_7 = Button(window, text="Button_06", command=button_5).grid(row=9, column=0, sticky="ew", padx=5)
btn_8 = Button(window, text="Button_07", command=button_0).grid(row=10, column=0, sticky="ew", padx=5)
btn_9 = Button(window, text="Button_08", command=button_1).grid(row=11, column=0, sticky="ew", padx=5)
btn_10 = Button(window, text="Button_09", command=button_2).grid(row=12, column=0, sticky="ew", padx=5)
btn_11 = Button(window, text="Button_10", command=button_3).grid(row=13, column=0, sticky="ew", padx=5)
btn_12 = Button(window, text="Button_11", command=button_4).grid(row=14, column=0, sticky="ew", padx=5)
btn_13 = Button(window, text="Button_12", command=button_5).grid(row=15, column=0, sticky="ew", padx=5)
btn_14 = Button(window, text="Button_13", command=button_5).grid(row=16, column=0, sticky="ew", padx=5)
btn_14 = Button(window, text="Button_14", command=button_5).grid(row=17, column=0, sticky="ew", padx=5)
btn_stop = Button(window, text="Stop", command=stop).grid(row=23, column=0, sticky="ew", padx=5)


#settings button
btn_set_1 = Button(window, text="+", command=lambda:settings_menu(0)).grid(row=3, column=3, sticky="ew", padx=5)
btn_set_2 = Button(window, text="+", command=lambda:settings_menu(1)).grid(row=4, column=3, sticky="ew", padx=5)
btn_set_3 = Button(window, text="+", command=lambda:settings_menu(2)).grid(row=5, column=3, sticky="ew", padx=5)
btn_set_4 = Button(window, text="+", command=lambda:settings_menu(3)).grid(row=6, column=3, sticky="ew", padx=5)
btn_set_5 = Button(window, text="+", command=lambda:settings_menu(4)).grid(row=7, column=3, sticky="ew", padx=5)
btn_6 = Button(window, text="+",command=lambda:settings_menu(5) ).grid(row=8, column=3, sticky="ew", padx=5)
btn_set_7 = Button(window, text="+", command=lambda:settings_menu(6)).grid(row=9, column=3, sticky="ew", padx=5)
btn_set_8= Button(window, text="+", command=lambda:settings_menu(7)).grid(row=10, column=3, sticky="ew", padx=5)
btn_set_9 = Button(window, text="+", command=lambda:settings_menu(8)).grid(row=11, column=3, sticky="ew", padx=5)
btn_set_10 = Button(window, text="+", command=lambda:settings_menu(9)).grid(row=12, column=3, sticky="ew", padx=5)
btn_set_11 = Button(window, text="+", command=lambda:settings_menu(10)).grid(row=13, column=3, sticky="ew", padx=5)
btn_set_12 = Button(window, text="+", command=lambda:settings_menu(11)).grid(row=14, column=3, sticky="ew", padx=5)
btn_set_13 = Button(window, text="+", command=lambda:settings_menu(12)).grid(row=15, column=3, sticky="ew", padx=5)
btn_set_14 = Button(window, text="+", command=lambda:settings_menu(13)).grid(row=16, column=3, sticky="ew", padx=5)
btn_set_15 = Button(window, text="+", command=lambda:settings_menu(14)).grid(row=17, column=3, sticky="ew", padx=5)
btn_set_date = Button(window, text = "Select Date", command = set_date).grid(row=18, column=0, sticky="ew", padx=5) #.pack(pady = 20)
btn_file0 = Button(window, text="Import file", command=file0).grid(row=19, column=0, sticky="ew", padx=5)
btn_add_camera = Button(window, text="Add Camera", command=add_camera).grid(row=20, column=0, sticky="ew", padx=5)
btn_clear = Button(window, text="Clear", command=clear).grid(row=21, column=0, sticky="ew", padx=5)
btn_exit = Button(window, text="Exit", command=exit).grid(row=24, column=0, sticky="ew", padx=5)

#labels
l1 = Label(window, text="Debugger1 Status:").grid(row=0, column=0, sticky="wne", padx=5)
l1 = Label(window, text="00: ").grid(row=3, column=1, sticky="wn", padx=5)
l1 = Label(window, text="01: ").grid(row=4, column=1, sticky="wn", padx=5)
l1 = Label(window, text="02: ").grid(row=5, column=1, sticky="wn", padx=5)
l1 = Label(window, text="03: ").grid(row=6, column=1, sticky="wn", padx=5)
l1 = Label(window, text="04: ").grid(row=7, column=1, sticky="wn", padx=5)
l1 = Label(window, text="05: ").grid(row=8, column=1, sticky="wn", padx=5)
l1 = Label(window, text="06: ").grid(row=9, column=1, sticky="wn", padx=5)
l1 = Label(window, text="07: ").grid(row=10, column=1, sticky="wn", padx=5)
l1 = Label(window, text="08: ").grid(row=11, column=1, sticky="wn", padx=5)
l1 = Label(window, text="09: ").grid(row=12, column=1, sticky="wn", padx=5)
l1 = Label(window, text="10: ").grid(row=13, column=1, sticky="wn", padx=5)
l1 = Label(window, text="11: ").grid(row=14, column=1, sticky="wn", padx=5)
l1 = Label(window, text="12: ").grid(row=15, column=1, sticky="wn", padx=5)
l1 = Label(window, text="13: ").grid(row=16, column=1, sticky="wn", padx=5)
l1 = Label(window, text="14: ").grid(row=17, column=1, sticky="wn", padx=5)


#show entry box
entry.grid(row=3, column=2, sticky="wne", padx=5)
entry1.grid(row=4, column=2, sticky="wne", padx=5)
entry2.grid(row=5, column=2, sticky="wne", padx=5)
entry3.grid(row=6, column=2, sticky="wne", padx=5)
entry4.grid(row=7, column=2, sticky="wne", padx=5)
entry5.grid(row=8, column=2, sticky="wne", padx=5)
entry6.grid(row=9, column=2, sticky="wne", padx=5)
entry7.grid(row=10, column=2, sticky="wne", padx=5)
entry8.grid(row=11, column=2, sticky="wne", padx=5)
entry9.grid(row=12, column=2, sticky="wne", padx=5)
entry10.grid(row=13, column=2, sticky="wne", padx=5)
entry11.grid(row=14, column=2, sticky="wne", padx=5)
entry12.grid(row=15, column=2, sticky="wne", padx=5)
entry13.grid(row=16, column=2, sticky="wne", padx=5)
entry14.grid(row=17, column=2, sticky="wne", padx=5)
entry15.grid(row=18, column=2, sticky="wne", padx=5)

#create window
window_tabs.mainloop()

