import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import customtkinter as ct
from customtkinter import *
from matplotlib.figure import Figure

from max_temp_analysis import *
from min_temp_analysis import *
from humidity_analysis import *
from rainfall_analysis import *

ct.set_appearance_mode("light")

# Define the plotting function
def temp_plotting(month, year, district, df_max, df_min):


    fig1, ax1 = plt.subplots()
    ax1.plot(df_max['Day'], df_max['Tempareture'], label = "Max Tempareture")
    ax1.plot(df_min['Day'], df_min['Tempareture'], label = "Min Tempareture")
    ax1.set_title(f"Tempareture of {district} in {month} of {year}")
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Tempareture')
    ax1.legend()
    
    canvas = FigureCanvasTkAgg(fig1, root)
    # canvas.legend()
    canvas.draw()
    canvas.get_tk_widget().place(relx=1, x=-330, y=900, anchor=S)
    

def humidity_plotting(month, year, district, df):


    fig1, ax1 = plt.subplots()
    ax1.plot(df['Day'], df['Humidity'])
    ax1.set_title(f"Humidity of {district} in {month} of {year}")
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Humidity')

    
    canvas = FigureCanvasTkAgg(fig1, root)
    # canvas.legend()
    canvas.draw()
    canvas.get_tk_widget().place(relx=1, x=-950, y=900, anchor=S)


def rainfall_plotting(month, year, district, df):

    fig1, ax1 = plt.subplots()
    ax1.scatter(df['Day'], df['Rainfall'])
    ax1.set_title(f"Rainfall of {district} in {month} of {year}")
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Rainfall')

    
    canvas = FigureCanvasTkAgg(fig1, root)
    # canvas.legend()
    canvas.draw()
    canvas.get_tk_widget().place(relx=1, x=-1590, y=900, anchor=S)


# Creating the window
root = CTk()
root.title("Water Modeling System")
root.geometry("1920x1080")
root.resizable(height=True, width=True)
root.state("zoomed")

# Making the borders and the title label
title_label = Label(text="Bangladesh Weather History Analyzer", bg="orchid", fg="pink", font=("comicsansms", 40, "bold", "italic"),
                    borderwidth=3, relief=SUNKEN)
title_label.pack(side=TOP, fill="x")
title_label = Label(bg="orchid1", fg="pink", font=("comicsansms", 24, "bold"), borderwidth=3, relief=SUNKEN)
title_label.pack(side=BOTTOM, fill="x")
title_label = Label(bg="orchid2", fg="pink", font=("comicsansms", 24, "bold"), borderwidth=3, relief=SUNKEN)
title_label.pack(side=LEFT, fill="y")
title_label = Label(bg="orchid3", fg="pink", font=("comicsansms", 24, "bold"), borderwidth=3, relief=SUNKEN)
title_label.pack(side=RIGHT, fill="y")


# Dark mode button
def changeMode():
    val = switch.get()
    if val:
        ct.set_appearance_mode("dark")
    else:
        ct.set_appearance_mode("light")

switch = CTkSwitch(root, text="Dark Mode",
                   onvalue=1,
                   offvalue=0,
                   command=changeMode)
switch.pack(side="bottom")

# Drop down box of months
options_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                 'August', 'September', 'October', 'November', 'December']
clicked_month = StringVar()
clicked_month.set("Month")
drop_month = OptionMenu(root, clicked_month, *options_month)
drop_month.config(font="Arial 24 bold", relief=SUNKEN)
drop_month.place(relx=1, x=-300, y=200, anchor=S)

# Drop down box of years
options_year = [i for i in range(1948, 2016)]
clicked_year = StringVar()
clicked_year.set("Year")
drop_year = OptionMenu(root, clicked_year, *options_year)
drop_year.config(font="Arial 24 bold", relief=SUNKEN)
drop_year.place(relx=1, x=-800, y=200, anchor=S)

# drop down box of districts
options_district = ['Bogra', 'Comilla', "Cox's Bazar", 'Dinajpur', 'Faridpur',
                    'Jessore', 'Khulna', 'Mymensingh', 'Satkhira', 'Srimangal',
                    'Barisal', 'Chittagong', 'M.court', 'Dhaka', 'Sylhet', 'Rangamati',
                    'Rangpur', 'Ishurdi', 'Chandpur', 'Rajshahi', 'Bhola', 'Hatiya',
                    'Sandwip', 'Feni', 'Patuakhali', 'Khepupara', 'Madaripur',
                    'Sitakunda', 'Teknaf', 'Kutubdia', 'Tangail', 'Chuadanga',
                    'Mongla', 'Sydpur', 'Ambagan(Ctg)']
clicked_district = StringVar()
clicked_district.set("District")
drop_district = OptionMenu(root, clicked_district, *options_district)
drop_district.config(font="Arial 24 bold", relief=SUNKEN)
drop_district.place(relx=1, x=-1300, y=200, anchor=S)

# Function to call plotting with selected options
def plot_selected():
    month = clicked_month.get()
    month_index = options_month.index(month)
    year = int(clicked_year.get())
    district = clicked_district.get()


    df_max = creat_max_df(month_index, year, district)
    df_min = creat_min_df(month_index, year, district)

    df_humidity = creat_humidity_df(month_index, year, district)

    df_rainfall = creat_rainfall_df(month_index, year, district)

    # Here, you should fetch data based on selected options and pass it to the plotting function
    temp_plotting(month, year, district, df_max, df_min)
    humidity_plotting(month, year, district, df_humidity)
    rainfall_plotting(month, year, district, df_rainfall)
    

# Button to trigger plotting
bt_1 = Button(master=root, text="Create The Graph", font="Times 30 bold", command=plot_selected)
bt_1.place(relx=1, x=-790, y=350, anchor=S)





root.mainloop()