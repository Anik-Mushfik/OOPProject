import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

headers = ["District", "Year", "Month", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
           "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "Janina"]


df = pd.read_csv("C:\Musfique's Folder\Python\OOPProject\Data Set\Daily Total Rainfall Till_Jun 2014-csv.csv", names = headers)
df1 = df.copy()


"""Replacing the 1234s with month names"""

replace_values = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
                6:"June", 7:"July", 8:"August", 9:"September", 10:"October",
                11:"November", 12:"December", '1':"January", '2':"February", '3':"March", '4':"April", '5':"May",
                '6':"June", '7':"July", '8':"August", '9':"September", '10':"October",
                '11':"November", '12':"December"}

df1['Month'] = df1['Month'].replace(replace_values)


df1.drop('Janina', axis=1, inplace=True)

df1.shape

df1.drop(df1.head(1).index, inplace= True)


def creat_rainfall_df(month_index, year, district):
    dist = df1.loc[df1["District"] == f"{district}"]

    """## Dealing With Nul Values"""

    # replacing "****" with NaN
    dist.replace("****", np.nan, inplace=True)
    dist.replace("***", np.nan, inplace=True)
    dist.replace("*** *", np.nan, inplace=True)
    dist.replace("**", np.nan, inplace=True)

    dist_year = dist[dist["Year"] == str(year)].reset_index(drop=True)

    """## Making Datasets for each months"""

    final_df = pd.DataFrame(dist_year.iloc[month_index])
    final_df = final_df.reset_index()
    final_df.rename(columns={'index': "Day"}, inplace=True)
    final_df.rename(columns={month_index: 'Rainfall'}, inplace=True)
    final_df.drop(final_df.head(3).index, inplace=True)
    final_df = final_df.reset_index(drop=True)

    return final_df

