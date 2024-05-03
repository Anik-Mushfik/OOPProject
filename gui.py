import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkinter import *
from data_visualization import *
import customtkinter as ct
from customtkinter import *

ct.set_appearance_mode("light")
ct.set_default_color_theme("dark-blue")



class WaterModelingSystem:
    def __init__(self):
        self.root = CTk()
        self.root.title("Water Modeling System")
        self.root.geometry("1920x1080")
        self.root.resizable(height=True,width=True)
        self.root.state("zoomed")
        self.create_labels()
        self.create_sidebar()
        self.create_dropdowns()
        self.create_plot_button()

    def create_labels(self):
        self.title_label=Label(text= "Water Model ", bg="orchid" ,fg="pink" , font=("comicsansms",40,"bold", "italic"), borderwidth=3,relief=SUNKEN ) 
        self.title_label.pack(side=TOP,fill="x") 
        self.title_label=Label( bg="orchid1" ,fg="pink" , font=("comicsansms",24,"bold"), borderwidth=3,relief=SUNKEN ) 
        self.title_label.pack(side=BOTTOM,fill="x") 
        self.title_label=Label(bg="orchid2" ,fg="pink" , font=("comicsansms",24,"bold"), borderwidth=3,relief=SUNKEN ) 
        self.title_label.pack(side=LEFT,fill="y") 
        self.title_label=Label( bg="orchid3" ,fg="pink" , font=("comicsansms",24,"bold"), borderwidth=3,relief=SUNKEN ) 
        self.title_label.pack(side=RIGHT,fill="y") 

    def create_sidebar(self):
        self.sidebar_frame = Frame(self.root, bg='orchid3')
        self.sidebar_frame.pack(fill='y', side='left')
        self.side_label = Label(self.sidebar_frame, text="Choose Your\nOptions", bg='orchid4', font='Calicri 24 bold', foreground="white")
        self.side_label.pack()
        self.temp_button = Button(self.sidebar_frame, text='Min Temperature', font='Aial 24 bold', bg='lightyellow2', fg='black',borderwidth=8)
        self.temp_button.pack(pady=40)
        self.temp_button = Button(self.sidebar_frame, text='Humidity', font='Aial 24 bold', bg='lightyellow2', fg='black',borderwidth=8)
        self.temp_button.pack(pady=40, fill='x')
        self.temp_button = Button(self.sidebar_frame, text='Sunshine', font='Aial 24 bold', bg='lightyellow2', fg='black',borderwidth=8)
        self.temp_button.pack(pady=40, fill='x')
        self.temp_button = Button(self.sidebar_frame, text='Rainfall', font='Aial 24 bold', bg='lightyellow2', fg='black', borderwidth=8)
        self.temp_button.pack(pady=40, fill='x')
        self.switch = CTkSwitch(self.sidebar_frame, text="Dark Mode", onvalue=1, offvalue=0, command=self.changeMode)
        self.switch.pack(side= "bottom")

    def changeMode(self):
        val = self.switch.get()
        if val:
            ct.set_appearance_mode("dark")
        else:
            ct.set_appearance_mode("light")

    def create_dropdowns(self):
        options_month = ['January', 'Februray', 'March', 'April', 'May', 'June', 'July', 
           'August', 'September', 'October', 'November', 'December']
        self.clicked_month = StringVar()
        self.clicked_month.set("Month")
        self.drop_month = OptionMenu(self.root, self.clicked_month, *options_month)
        self.drop_month.config(font="Arial 24 bold", relief=SUNKEN)
        self.drop_month.place(relx =1, x =-300, y = 200, anchor =S)
        options_year = [i for i in range(1948, 2016)]
        self.clicked_year = StringVar()
        self.clicked_year.set("Year")
        self.drop_year = OptionMenu(self.root, self.clicked_year, *options_year)
        self.drop_year.config(font="Arial 24 bold", relief=SUNKEN)
        self.drop_year.place(relx =1, x =-800, y = 200, anchor =S)
        options_district = []
        self.clicked_district = StringVar()
        self.clicked_district.set("District")
        self.drop_district = OptionMenu(self.root, self.clicked_district, *options_district)
        self.drop_district.config(font="Arial 24 bold", relief=SUNKEN)
        self.drop_district.place(relx =1, x =-1300, y = 200, anchor =S)

    def create_plot_button(self):
        self.bt_1 = Button(master=self.root, text="Create The Graph", font="Times 30 bold", command=self.plotting)
        self.bt_1.place(relx =1, x =-790, y = 350, anchor =S)

    def plotting(self):
        fig1, ax1 = plt.subplots()
        ax1.plot(february['Day'], february['Tempareture'])
        ax1.set_title("Tempareture of Bogra in 1948")
        ax1.set_xticks(['5', '10','15', '20','25','30'])
        ax1.set_xlabel('Day')
        ax1.set_ylabel('Tempareture')
        canvas = FigureCanvasTkAgg(fig1, self.root)
        canvas.draw()
        canvas.get_tk_widget().place(relx =1, x =-900, y = 900, anchor =S)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WaterModelingSystem()
    app.run()
