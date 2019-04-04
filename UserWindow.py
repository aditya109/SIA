import tkinter as tk
from tkinter import ttk as ttk
import urllib
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use ("TkAgg")
from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.figure import figure
# Font Family

TITLE_LARGE = ("Verdana", 35)
TEXT_SMALL = ("Verdana", 18, 'bold')

def animate(i):
        dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
        data = urllib.request.urlopen(dataLink)
        data = data.readall().decode("utf-8")
        data = json.loads(data)


        data = data["btc_usd"]
        data = pd.DataFrame(data)

        buys = data[(data['type']=="bid")]
        buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
        buyDates = (buys["datestamp"]).tolist()


        sells = data[(data['type']=="ask")]
        sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        sellDates = (sells["datestamp"]).tolist()

        a.clear()

        a.plot_date(buyDates, buys["price"], "#00A3E0", label="buys")
        a.plot_date(sellDates, sells["price"], "#183A54", label="sells")

        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
             ncol=2, borderaxespad=0)

        title = "BTC-e BTCUSD Prices\nLast Price: "+str(data["price"][1999])
        a.set_title(title)
class Test(tk.Tk) :

        def __init__(self, *args, **kwargs) :

                tk.Tk.__init__(self, *args, **kwargs)

                container = tk.Frame(self)

                container.pack(side = "top", fill = "both", expand =  True)

                container.grid_rowconfigure(0, weight = 1)
                container.grid_columnconfigure(0, weight = 1)

                self.frames = {}

                frame = UserWindow(container, self)

                self.frames[UserWindow] = frame

                frame.grid(row = 0, column = 0, sticky = "nsew")

                self.show_frame(UserWindow)

                # Title bar ICON
                tk.Tk.iconbitmap(self, default="C:/Users/Aditya/Desktop/Projects/Stock Investment Automation/assets/favicon.ico")
                # Title bar TITLE
                tk.Tk.wm_title(self, "Stock Investment Automation")


        def show_frame(self, cont) :

                frame = self.frames[cont]
                frame.tkraise()

class UserWindow(tk.Frame) :

##        def __init__(self, parent, controller) :

        ##                tk.Frame.__init__(self, parent, bg = '#403C3C')
        ##
        ##                title_label = ttk.Label(self, text = "STOCK INVESMENT AUTOMATION", font = TITLE_LARGE, foreground = '#0ed145', background = '#403C3C')
        ##                title_label.pack(pady = 240 , padx = 10)
        ##
        ##                # Designing Login Button
        ##                
        ##                login_Button = tk.Button(self, text = "LOGIN", background = '#ea3946', foreground = '#ffffff', relief='flat', width = 10, font = TEXT_SMALL)
        ##                login_Button.pack(pady=10, padx =10)
        ##                login_Button = tk.Button(self, text = "SIGN UP", background = '#ea3946', foreground = '#ffffff', relief='flat', width = 10, font = TEXT_SMALL)
        ##                login_Button.pack(pady=10, padx =10)

        # Creating Matplotlib Plots

        def __init__(self, parent, controller) :
                tk.Frame.__init__(self, parent)
                label = tk.label(self, text = "Graph Page", font = LARGE_FONT)
                label.pack(pady=10, padx=10)

                f = Figure(figsize = (5,5), dpi = 100)
                a = f.add_subplot(111)

                
        



app = Test()
app.geometry("1600x900")
app.mainloop()
