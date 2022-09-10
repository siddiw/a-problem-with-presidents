"""
The file contains the function that processes the input data
"""
import numpy
import pandas
from datetime import datetime
import dataframe_image as dfi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def processData():
    #The function processes data and creates the required tables.

    # Import the CSV into dataframe df
    df = pandas.read_csv('input.csv', sep = ',',header = 0)
    df = df[:-1]

    # REQ001 - Parse Year of Birth from "BIRTH DATE" column
    df["year_of_birth"] = pandas.DatetimeIndex(df["BIRTH DATE"]).year.astype(int)

    # Change all unknown locations of death to "ALIVE"
    df["LOCATION OF DEATH"].fillna('ALIVE', inplace=True)

    # Creating variable "latest_living_date" to calculate lived_dates, lived_months and lived_years.
    # This is a one step of Data Cleaning - to handle missing values (NaN in our case). Technically, 
    # these are not "missing", just empty due to the nature of the column.
    today_date = datetime.now().strftime("%b %d, %Y")
    df["latest_living_date"] = df["DEATH DATE"]
    df["latest_living_date"].fillna(today_date, inplace=True)

    # REQ002 , REQ003, REQ004 - Calculating lived_years, lived_months and lived_days
    count_dates = pandas.DatetimeIndex(df["latest_living_date"]) - pandas.DatetimeIndex(df["BIRTH DATE"])
    df["lived_years"] = count_dates / numpy.timedelta64(1, "Y")
    df["lived_months"] = count_dates / numpy.timedelta64(1, "M")
    df["lived_days"] = (count_dates/ numpy.timedelta64(1, "D"))

    # Since calculations are now done, replace NaN death date values with "Living".
    # Update DEATH DATE column empty values with "ALIVE" since we have calculated the required variables.
    df["DEATH DATE"].fillna('ALIVE', inplace=True)

    # Function to return style to highlight living presidents in tables.
    def highlight_living(data):
        living_highlight = ['background-color: green'] * len(data)
        death_highlight = ['background-color: transparent'] * len(data)
    
        return living_highlight if data['DEATH DATE'] == 'ALIVE' else death_highlight

    # REQ005 - Output top 10 Presidents from longest lived to shortest lived.
    # Taking top 10 values after sorting data by days lived in dsecending order.
    oldest_top_10_df = df.sort_values("lived_days", ascending=False).head(10)
    # Converting lived years to integer
    oldest_top_10_df["lived_years"] = oldest_top_10_df["lived_years"].astype(int)
    # Changing lived_years column name to AGE
    oldest_top_10_df.rename(columns={"lived_years": "AGE"}, inplace=True)

    oldest_top_10 = oldest_top_10_df.style
    # Hide index
    oldest_top_10.hide(axis="index")
    # Hide extra columns unnecessary to the table
    oldest_top_10.hide_columns(["lived_days", "lived_months", "latest_living_date", "year_of_birth"])
    # Highlight living presidents in the table
    oldest_top_10.apply(highlight_living, axis=1)
    # Set title of the table
    oldest_top_10.set_caption("Top 10 Presidents of the United States from longest lived to shortest lived")
    # Show the table
    # Converting styled table to image
    dfi.export(oldest_top_10, "oldest_top_10.png")
    # Displaying the image using matplotlib
    img = mpimg.imread('oldest_top_10.png')
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.show()

    # REQ006 - Output top 10 Presidents from shortest lived to longest lived.
    # Performing similar steps as above, except taking top 10 values after sorting data by days lived in ascending order.
    youngest_top_10_df = df.sort_values("lived_days", ascending=True).head(10)
    youngest_top_10_df["lived_years"] = youngest_top_10_df["lived_years"].astype(int)
    youngest_top_10_df.rename(columns={"lived_years": "AGE"}, inplace=True)

    youngest_top_10 = youngest_top_10_df.style
    youngest_top_10.hide(axis="index")
    youngest_top_10.hide_columns(["lived_days", "lived_months", "latest_living_date", "year_of_birth"])
    youngest_top_10.apply(highlight_living, axis=1)
    youngest_top_10.set_caption("Top 10 Presidents of the United States from shortest lived to longest lived")
    dfi.export(youngest_top_10, "youngest_top_10.png")
    img = mpimg.imread('youngest_top_10.png')
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.show()

    print("Exit ProcessData")

    return df
