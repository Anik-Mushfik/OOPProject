import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkinter import *
from data_visualization2 import *
import customtkinter as ct
from customtkinter import *

# Define the plotting function
def plotting(month, year, district, df):

    # Assuming 'february' DataFrame is defined somewhere else based on user's selection
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(df['Day'], df['Tempareture'])
    ax1.set_title(f"Tempareture of {district} in {month} of {year}")
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Tempareture')
    
    canvas = FigureCanvasTkAgg(fig1, root)
    canvas.draw()
    canvas.get_tk_widget().place(relx=1, x=-900, y=900, anchor=S)
    

# Creating the window
root = CTk()
root.title("Water Modeling System")
root.geometry("1920x1080")
root.resizable(height=True, width=True)
root.state("zoomed")

# Making the borders and the title label
title_label = Label(text="Water Model ", bg="orchid", fg="pink", font=("comicsansms", 40, "bold", "italic"),
                    borderwidth=3, relief=SUNKEN)
title_label.pack(side=TOP, fill="x")
title_label = Label(bg="orchid1", fg="pink", font=("comicsansms", 24, "bold"), borderwidth=3, relief=SUNKEN)
title_label.pack(side=BOTTOM, fill="x")
title_label = Label(bg="orchid2", fg="pink", font=("comicsansms", 24, "bold"), borderwidth=3, relief=SUNKEN)
title_label.pack(side=LEFT, fill="y")
title_label = Label(bg="orchid3", fg="pink", font=("comicsansms", 24, "bold"), borderwidth=3, relief=SUNKEN)
title_label.pack(side=RIGHT, fill="y")

# Making the sidebar
sidebar_frame = Frame(root, bg='orchid3')
sidebar_frame.pack(fill='y', side='left')

side_label = Label(sidebar_frame, text="Choose Your\nOptions", bg='orchid4', font='Calicri 24 bold',
                   foreground="white")
side_label.pack()

# Dark mode button
def changeMode():
    val = switch.get()
    if val:
        ct.set_appearance_mode("dark")
    else:
        ct.set_appearance_mode("light")

switch = CTkSwitch(sidebar_frame, text="Dark Mode",
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


    df = creat_df(month_index, year, district)
    
    # Here, you should fetch data based on selected options and pass it to the plotting function
    plotting(month, year, district, df)

# Button to trigger plotting
bt_1 = Button(master=root, text="Create The Graph", font="Times 30 bold", command=plot_selected)
bt_1.place(relx=1, x=-790, y=350, anchor=S)





root.mainloop()