"""
The file contains the function that draws the required plots
"""
import numpy
import pandas
import dataframe_image as dfi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# The function draws the required plots
def drawGraph(df):
    # Taking required columns into variables so that lists can be worked on
    lived_years_column = df["lived_years"].astype(int)
    value_counts = lived_years_column.value_counts()
    lived_days_column = df["lived_days"]

    weights = []
    for i in range(len(lived_years_column)):
        year = lived_years_column[i]
        # Using the frequency of a year as the weight
        weights.append(value_counts[year])
    weights = numpy.array(weights)
    # Getting weighted values
    weighted_values = weights * lived_days_column

    # REQ007 - REQ013 - Calculating the statistics (in years)
    mean_years = lived_years_column.mean()
    weighted_mean_years = lived_years_column.sum() / weights.sum()
    median_years = lived_years_column.median()
    mode_years = lived_years_column.mode()
    max_years = lived_years_column.max()
    min_years = lived_years_column.min()
    std_years = lived_years_column.std()

    # REQ007 - REQ013 - Calculating the statistics (in days)
    mean_days = lived_days_column.mean()
    weighted_mean_days = weighted_values.sum() / weights.sum()
    median_days = lived_days_column.median()
    mode_days = lived_years_column.mode() * 365
    max_days = lived_days_column.max()
    min_days = lived_days_column.min()
    std_days = lived_days_column.std()

    # REQ14 - Tabularizing and output the statistics in well-formatted table
    data = {
        "Statistic": ["Mean Age", "Weighted Mean Age", "Median Age", "Mode Age", "Maximum Age", "Minimum Age", "Standard Deviation"],
        "Age (Days)": [mean_days, weighted_mean_days, median_days, list(mode_days), max_days, min_days, std_days],
        "Age (Years)": [mean_years, weighted_mean_years, median_years, [x for x in list(mode_years)], max_years, min_years, std_years]
    }

    def add_labels_to_bar_graph(x,y):
        for i in range(len(x)):
            plt.text(i, round(y[i]//2,1), round(y[i],1), ha = 'center')

    df_stats = pandas.DataFrame.from_dict(data)
    df_stats.style.hide(axis="index")
    dfi.export(df_stats, "stats.png")
    # Displaying the image using matplotlib
    img = mpimg.imread('stats.png')
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.show()

    # REQ015 - PLOT 1 [ Statistics ]
    x_axis = ["Mean", "Weighted Mean", "Median", "Maximum", "Minimum"]
    x_axis_positions = range(len(x_axis))
    y_axis = [mean_days, weighted_mean_days, median_days, max_days, min_days]
    plt.figure(figsize=(6, 5))
    plt.bar(x_axis_positions, y_axis, 0.7, color=['#7d8291', '#b8c0d9', '#68718c', '#4e515c', '#687396'])
    add_labels_to_bar_graph(x_axis_positions, y_axis)
    plt.ylabel("Age (in Days)")
    plt.title("Statistics of Presidential Ages")

    plt.axhline(y = mean_days + std_days, color = 'r', linestyle = '--', label='Standard Deviation')
    plt.axhline(y = mean_days, color = 'gray', linestyle = '-.', label='Mean')
    plt.axhline(y = mean_days - std_days, color = 'r', linestyle = '--')

    plt.legend(labels=['Standard Deviation', 'Mean'])

    plt.xticks(x_axis_positions, x_axis)
    plt.show()

    # REQ016 - PLOT 2 [ Age Ranges ]
    def add_labels_to_line_graph(x, y):
        for x,y in zip(x,y):
            label = y
            plt.annotate(label, # this is the text
                        (x,y), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(3,7), # distance from text to points (x,y)
                        ha='center') 

    df['age_range'] = pandas.cut(df['lived_years'].astype(int), [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100], 
                        labels=['45-50', '51-55', '56-60', '61-65', '66-70', '71-75', '76-80', '81-85', '86-90', '91-95', '96-100'])
    
    age_range_column = df["age_range"].value_counts().sort_index().rename_axis('range').reset_index(name='counts')
    print(age_range_column['range'])

    x_axis = list(age_range_column['range'])
    y_axis = list(age_range_column['counts'])
    plt.figure(figsize=(15, 4))
    plt.plot(x_axis, y_axis, color='red', marker='o')
    add_labels_to_line_graph(x_axis, y_axis)
    plt.title('Frequency Distribution of Presidential Ages', fontsize=14)
    plt.xlabel('Age Range', fontsize=10)
    plt.ylabel('No. of Presidents', fontsize=10)
    plt.grid(True)
    plt.show()

    print("Exit ProcessData")
    return 0