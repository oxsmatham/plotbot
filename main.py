# imports
from tkinter import *
from tkinter import ttk, filedialog
import tkintertable
from tkintertable import TableCanvas, TableModel
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
import matplotlib.patches as ptc

#--------------------------------------------------

app = Tk()

# app config
app_width = app.winfo_screenwidth()
app_height = app.winfo_screenheight()
app_x = 0
app_y = 0

app.geometry("%dx%d+%d+%d" % (app_width, app_height, app_x, app_y))
#app.resizable(False,False)
app.title("plotbot")

# grid layout for app
app.columnconfigure((0,1),weight = 1, uniform = "a")

app.rowconfigure(0, weight = 3, uniform = "a")
app.rowconfigure(1, weight = 21, uniform = "a")
app.rowconfigure(2, weight = 1, uniform = "a")
app.rowconfigure(3, weight = 1, uniform = "a")
app.rowconfigure(4, weight = 4, uniform = "a")

# Frame 1 (row 0, column 0)
f1 = Frame(app, bg = "red")
f1.grid(row = 0, column = 0, sticky = "nsew")

# Frame 2 (row 1, column 0)
f2 = Frame(app, bg = "yellow")
f2.grid(row = 1, column = 0, sticky = "nsew")

# Frame 3 (row 2, column 0)
f3 = Frame(app, bg = "blue")
f3.grid(row = 2, column = 0, sticky = "nsew")

# Frame 4 (row 3, column 0)
f4 = Frame(app, bg = "green")
f4.grid(row = 3, column = 0, sticky = "nsew")

# Frame 5 (row 4, column 0)
f5 = Frame(app, bg = "orange")
f5.grid(row = 4, column = 0, sticky = "nsew")


# Frame 6 (row 0, column 1)
f6 = Frame(app, bg = "pink")
f6.grid(row = 0, column = 1, sticky = "nsew")

# Frame 7 (row 1, column 1)
f7 = Frame(app, bg = "magenta")
f7.grid(row = 1, column = 1, sticky = "nsew")

# Frame 8 (row 2-4, column 1)
f8 = Frame(app, bg = "black")
f8.grid(row = 2, column = 1, rowspan = 3, sticky = "nsew")

app.mainloop()