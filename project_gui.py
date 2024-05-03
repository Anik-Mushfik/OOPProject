import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkinter import *
from data_visualization import *






# Creating the window
root = Tk()
root.title("Water Modeling System")
root.geometry("960x540")
# root.resizable(height=False,width=False) 
root.state("zoom") 


# Making the borders and the title label
title_label=Label(text= "Water Model ", bg="orchid" ,fg="pink" , font=("comicsansms",40,"bold", "italic"), borderwidth=3,relief=SUNKEN ) 
title_label.pack(side=TOP,fill="x") 
title_label=Label( bg="orchid1" ,fg="pink" , font=("comicsansms",24,"bold"), borderwidth=3,relief=SUNKEN ) 
title_label.pack(side=BOTTOM,fill="x") 
title_label=Label(bg="orchid2" ,fg="pink" , font=("comicsansms",24,"bold"), borderwidth=3,relief=SUNKEN ) 
title_label.pack(side=LEFT,fill="y") 
title_label=Label( bg="orchid3" ,fg="pink" , font=("comicsansms",24,"bold"), borderwidth=3,relief=SUNKEN ) 
title_label.pack(side=RIGHT,fill="y") 


# Making the sidebad
sidebar_frame = Frame(root, bg='orchid3')
sidebar_frame.pack(fill='y', side='left')

side_label = Label(sidebar_frame, text="Choose Your\nOptions", bg='orchid4', font='Calicri 24 bold', foreground="white")
side_label.pack()

temp_button = Button(sidebar_frame, text='Min Temperature', font='Aial 24 bold', bg='lightyellow2', fg='black',borderwidth=8)
temp_button.pack(pady=40)

temp_button = Button(sidebar_frame, text='Min Temperature', font='Aial 24 bold', bg='lightyellow2', fg='black',borderwidth=8)
temp_button.pack(pady=40)

temp_button = Button(sidebar_frame, text='Humidity', font='Aial 24 bold', bg='lightyellow2', fg='black',borderwidth=8)
temp_button.pack(pady=40, fill='x')

temp_button = Button(sidebar_frame, text='Sunshine', font='Aial 24 bold', bg='lightyellow2', fg='black',borderwidth=8)
temp_button.pack(pady=40, fill='x')

temp_button = Button(sidebar_frame, text='Rainfall', font='Aial 24 bold', bg='lightyellow2', fg='black', borderwidth=8)
temp_button.pack(pady=40, fill='x')







# Drop down box of months
options_month = ['January', 'Februray', 'March', 'April', 'May', 'June', 'July', 
           'August', 'September', 'October', 'November', 'December']
clicked_month = StringVar()
clicked_month.set("Month")

drop_month = OptionMenu(root, clicked_month, *options_month)
drop_month.config(font="Arial 24 bold", relief=SUNKEN)
drop_month.place(relx =1, x =-300, y = 200, anchor =S)


# Drop down box of years
options_year = [i for i in range(1948, 2016)]
clicked_year = StringVar()
clicked_year.set("Year")

drop_year = OptionMenu(root, clicked_year, *options_year)
drop_year.config(font="Arial 24 bold", relief=SUNKEN)
drop_year.place(relx =1, x =-800, y = 200, anchor =S)


# drop down box of districs
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
drop_district.place(relx =1, x =-1300, y = 200, anchor =S)





def plotting():
       fig1, ax1 = plt.subplots()
       ax1.plot(february['Day'], february['Tempareture'])
       ax1.set_title("Tempareture of Bogra in 1948")
       ax1.set_xticks(['5', '10','15', '20','25','30'])
       ax1.set_xlabel('Day')
       ax1.set_ylabel('Tempareture')


       canvas = FigureCanvasTkAgg(fig1, root)
       canvas.draw()
       canvas.get_tk_widget().place(relx =1, x =-900, y = 900, anchor =S)





bt_1 = Button(master=root, text="Create The Graph", font="Times 30 bold", command=plotting)
bt_1.place(relx =1, x =-790, y = 350, anchor =S)


root.mainloop()