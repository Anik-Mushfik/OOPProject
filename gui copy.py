import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import pandas as pd
import customtkinter as ct
from data_visualization2 import creat_df

class WaterModelApp(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Water Modeling System")
        self.geometry("1920x1080")
        self.resizable(height=True, width=True)
        self.state("zoomed")
        self.create_widgets()

    def create_widgets(self):
        # Making the borders and the title label
        self.title_label = ct.CTkLabel(self, text="Water Model ", font=("comicsansms", 40, "bold", "italic"), border_width=3, relief="sunken")
        self.title_label.pack(side="top", fill="x")

        # Making the sidebar
        self.sidebar_frame = ct.CTkFrame(self, bg='orchid3')
        self.sidebar_frame.pack(fill='y', side='left')

        self.side_label = ct.CTkLabel(self.sidebar_frame, text="Choose Your\nOptions", bg='orchid4', font=('Calicri', 24, 'bold'), fg_color="white")
        self.side_label.pack()

        # Dark mode button
        self.switch = ct.CTkSwitch(self.sidebar_frame, text="Dark Mode", command=self.change_mode)
        self.switch.pack(side="bottom")

        # Drop down box of months
        self.options_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.clicked_month = ct.StringVar()
        self.clicked_month.set("Month")
        self.drop_month = ct.CTkOptionMenu(self, variable=self.clicked_month, values=self.options_month, font=("Arial", 24, "bold"), border_width=2, relief="sunken")
        self.drop_month.place(relx=1, x=-300, y=200, anchor="s")

        # Drop down box of years
        self.options_year = [i for i in range(1948, 2016)]
        self.clicked_year = ct.IntVar()
        self.clicked_year.set("Year")
        self.drop_year = ct.CTkOptionMenu(self, variable=self.clicked_year, values=self.options_year, font=("Arial", 24, "bold"), border_width=2, relief="sunken")
        self.drop_year.place(relx=1, x=-800, y=200, anchor="s")

        # Drop down box of districts
        self.options_district = ['Bogra', 'Comilla', "Cox's Bazar", 'Dinajpur', 'Faridpur', 'Jessore', 'Khulna', 'Mymensingh', 'Satkhira', 'Srimangal', 'Barisal', 'Chittagong', 'M.court', 'Dhaka', 'Sylhet', 'Rangamati', 'Rangpur', 'Ishurdi', 'Chandpur', 'Rajshahi', 'Bhola', 'Hatiya', 'Sandwip', 'Feni', 'Patuakhali', 'Khepupara', 'Madaripur', 'Sitakunda', 'Teknaf', 'Kutubdia', 'Tangail', 'Chuadanga', 'Mongla', 'Sydpur', 'Ambagan(Ctg)']
        self.clicked_district = ct.StringVar()
        self.clicked_district.set("District")
        self.drop_district = ct.CTkOptionMenu(self, variable=self.clicked_district, values=self.options_district, font=("Arial", 24, "bold"), border_width=2, relief="sunken")
        self.drop_district.place(relx=1, x=-1300, y=200, anchor="s")

        # Button to trigger plotting
        self.plot_button = ct.CTkButton(self, text="Create The Graph", font=("Times", 30, "bold"), command=self.plot_selected)
        self.plot_button.place(relx=1, x=-790, y=350, anchor="s")

    def change_mode(self):
        if self.switch.get():
            ct.set_appearance_mode("dark")
        else:
            ct.set_appearance_mode("light")

    def plot_selected(self):
        month = self.clicked_month.get()
        month_index = self.options_month.index(month)
        year = self.clicked_year.get()
        district = self.clicked_district.get()

        df = creat_df(month_index, year, district)
        self.plotting(month, year, district, df)

    def plotting(self, month, year, district, df):
        fig, ax = plt.subplots()
        ax.plot(df['Day'], df['Tempareture'])
        ax.set_title(f"Tempareture of {district} in {month} of {year}")
        ax.set_xlabel('Day')
        ax.set_ylabel('Tempareture')

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().place(relx=1, x=-900, y=900, anchor="s")

if __name__ == "__main__":
    app = WaterModelApp()
    app.mainloop()