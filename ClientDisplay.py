
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.animation as animation
from matplotlib import style

from socket import *
from threading import Thread
# In order to terminate the program
import sys
import csv
import tkinter as tk
from tkinter import ttk



LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi = 100)
a = f.add_subplot(111)


xList = []
yList = []

def animate(i):
    print("Animate")
    pullData = open("DataStore.txt", "r").read()
    dataList = pullData.split('\n')
    
    for eachLine in dataList:
        if len(eachLine) > 1:
            x,y = eachLine.split(',')
            xList.append(int(x))
            yList.append(float(y))
    a.set_title("Temperture over Time")      
    a.plot(xList, yList)
   
class EnvironmentMonitor(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Environment Monitor Client")
        self.geometry("1200x800")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # holds the amount of frames for each graph
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree) :

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
       
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class InputPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter IP", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        eIp = tk.Entry(self)
        eIp.pack()
        label2 = tk.Label(self, text="Enter Port", font=LARGE_FONT)
        label2.pack(pady=10, padx=10)
        ePort = tk.Entry(self)
        ePort.insert(4, "1234")
        ePort.pack()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
         # add button to page
        button1 = ttk.Button(self, text="Outside Tempreture", command=lambda: controller.show_frame(PageOne) )

        button1.pack()
         # add button to page
        button2 = ttk.Button(self, text="Kitchen Tempreture", command=lambda: controller.show_frame(PageTwo))

        button2.pack()
         # add button to page
        button3  = ttk.Button(self, text="Living Room Tempreture", command=lambda: controller.show_frame(PageThree))

        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Outside", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

         # add button to page
        button1 = ttk.Button(self, text="Visit Home Page", command=lambda: controller.show_frame(StartPage))

        button1.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kitchen", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
         # add button to page
        button1 = ttk.Button(self, text="Visit Home Page", command=lambda: controller.show_frame(StartPage))

        button1.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Living Room", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # add button to page
        button1 = ttk.Button(self, text="Visit Home Page", command=lambda: controller.show_frame(StartPage))

        button1.pack()

        # add graph to page
        canvas = FigureCanvasTkAgg(f, self)

        canvas.draw()
       
        canvas.get_tk_widget().pack(fill=tk.X, side=tk.LEFT, expand = True) 




if __name__ == "__main__":
     
    
     app = EnvironmentMonitor()

     ani = animation.FuncAnimation(f,animate, interval=1000)
     app.mainloop()
  
    

