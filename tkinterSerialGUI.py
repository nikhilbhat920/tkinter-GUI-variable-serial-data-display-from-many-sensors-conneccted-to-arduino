from time import sleep

#from tkinter import * var1 = tk.StringVar()  var2 = tk.StringVar() #import threading

import tkinter as tk  


import serial
ser = serial.Serial('COM10',baudrate=9600,timeout=1)  #

def readSensor():
        mcD=ser.readline()
        data0=str(mcD)
        
        data0=data0[2:-1]
        u=data0.split(" ")
        print(u)
        if(len(u)>1):
                if(int(u[1])== 7):
                    lbl["text"] = u[0]
                
                if(int(u[1])== 8):
                    labl["text"] = u[0]
        window.after(527, readSensor)
        

window = tk.Tk()
window.title("serial GUI")
lbl = tk.Label(window, text="intitializing.........",font="arial 30",bg="pink")
labl = tk.Label(window, text="intitializing........",font="arial 30",bg="yellow")
lbl.pack()
labl.pack()
labl.after(1000, readSensor)


window.mainloop()
