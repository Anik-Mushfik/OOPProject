import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

headers = ["District", "Year", "Month", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
           "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "Janina"]

df = pd.read_excel("C:\Musfique's Folder\Python\OOPProject\Data Set\Copy of Daily  Max  Temp Till Jun_2014.xls", names = headers)

df1 = df.copy()

df1.head(10)
"""Replacing the 1234s with month names"""

replace_values = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
                6:"June", 7:"July", 8:"August", 9:"September", 10:"October",
                11:"November", 12:"December"}

df1["Month"] = df1["Month"].replace(replace_values)

"""Deleted the first 7 rows as they don't have any valuable data."""

df1.drop(df1.head(7).index, inplace= True)
df1.drop('Janina', axis=1, inplace=True)

df1.shape

df1.head(10)

"""Locating a district and making a separate dataset of it"""


def creat_df(month_index, year, district):
    dist = df1.loc[df1["District"] == f"{district}"]
    
    """## Dealing With Nul Values"""

# replacing "****" with NaN
    dist.replace("****", np.nan, inplace = True)

    dist_year = dist.loc[dist["Year"] == year].reset_index(drop = True)

    dist_year['Tempareture of the month'] = dist_year.iloc[:, 3:34].mean(axis=1)

    """## Making Datasets for each months"""

    final_df = pd.DataFrame(dist_year.iloc[month_index])
    final_df = final_df.reset_index()
    final_df.rename(columns = {'index' : "Day"}, inplace = True)
    final_df.rename(columns = {month_index : 'Tempareture'}, inplace = True)
    final_df.drop(final_df.head(3).index, inplace=True)
    final_df = final_df.reset_index(drop = True)


    return final_df


print(creat_df(1, 1948, 'Bogra'))