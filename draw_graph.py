import pandas
import numpy
import matplotlib.pyplot as plt
import math
import dataframe_image as dfi
import matplotlib.image as mpimg


def drawGraph(dataframe):
    print(dataframe.columns)
    print("Entered drawgraph")
    lived_days_col = dataframe["lived_days"]
    lived_years_col = dataframe["lived_years"].astype(int)
    value_counts = lived_years_col.value_counts()

    weights = []
    for i in range(len(lived_years_col)):
        year = lived_years_col[i]
        # Using the frequency of a year as the weight
        weights.append(value_counts[year])
    weights = numpy.array(weights)
    # Getting weighted values
    weighted_values = weights * lived_days_col

    # Calculating the statistics
    mean = lived_days_col.mean()
    weighted_mean = weighted_values.sum() / weights.sum()
    median = lived_days_col.median()
    mode = lived_years_col.mode() * 365
    max = lived_days_col.max()
    min = lived_days_col.min()
    std = lived_days_col.std()

    # Calculating the statistics - years
    mean_years = lived_years_col.mean()
    weighted_mean_years = lived_years_col.sum() / weights.sum()
    median_years = lived_years_col.median()
    mode_years = lived_years_col.mode()
    max_years = lived_years_col.max()
    min_years = lived_years_col.min()
    std_years = lived_years_col.std()

    # Tabularizing by appending everything to a dictionary
    data = {
        "Statistic": ["Mean Age", "Weighted Mean Age", "Median Age", "Mode Age", "Maximum Age", "Minimum Age", "Standard Deviation"],
        "Age (Days)": [mean, weighted_mean, median, list(mode), max, min, std],
        "Age (Years)": [mean_years, weighted_mean_years, median_years, [x for x in list(mode_years)], max_years, min_years, std_years]
    }

    def addlabels(x,y):
        # for i in range(len(x)):
        #     plt.text(i,round(y[i],2), round(y[i],2))
        for i in range(len(x)):
            plt.text(i, round(y[i]//2,1), round(y[i],1), ha = 'center')
    # Creating dataframe from the dictionary
    dataframe_stats = pandas.DataFrame.from_dict(data)
    dataframe_stats.style.hide(axis="index")

    dfi.export(
    dataframe_stats,
    "stats.png"  
    )
    # Displaying the image using matplotlib
    img = mpimg.imread('stats.png')
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.show()

    x_axis = ["Mean", "Weighted Mean", "Median", "Maximum", "Minimum"]
    x_axis_positions = range(len(x_axis))
    y_axis = [mean, weighted_mean, median, max, min]
    plt.figure(figsize=(6, 5))
    plt.bar(x_axis_positions, y_axis, 0.7, color=['#7d8291', '#b8c0d9', '#68718c', '#4e515c', '#687396'])
    addlabels(x_axis_positions, y_axis)
    plt.ylabel("Age (in Days)")
    plt.title("Statistics of Presidential Ages")

    plt.axhline(y = mean + std, color = 'r', linestyle = '--', label='Standard Deviation')
    plt.axhline(y = mean, color = 'gray', linestyle = '-.', label='Mean')
    plt.axhline(y = mean - std, color = 'r', linestyle = '--')

    plt.legend(labels=['Standard Deviation', 'Mean'])

    plt.xticks(x_axis_positions, x_axis)
    plt.show()

    # Plotting frequency distribution using matplotlib
    # x_axis_positions = [i for i in range(len(value_counts))]
    # plt.figure(figsize=(15, 4))
    # plt.bar(x_axis_positions, value_counts)
    # plt.xlabel("Age (years)")
    # plt.ylabel("Number of Presidents")
    # plt.title("Frequency of Presidential Ages")

    # plt.xticks(x_axis_positions, value_counts.keys())
    # plt.yticks(range(value_counts.max() + 1))
    # plt.show()

    # binning
    print(dataframe)

    temp = dataframe["lived_years"].astype(int).value_counts()
    print("TEMP",temp)
    dataframe['age_range'] = pandas.cut(dataframe['lived_years'].astype(int), [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100], labels=['45-50', '51-55', '56-60', '61-65', '66-70', '71-75', '76-80', '81-85', '86-90', '91-95', '96-100'])
    age_range_col = dataframe["age_range"].value_counts().sort_index().rename_axis('range').reset_index(name='counts')
    print(age_range_col['range'])

    x_axis = list(age_range_col['range'])
    y_axis = list(age_range_col['counts'])
    plt.figure(figsize=(15, 4))
    # plt.ayhline(y = mean, color = 'gray', linestyle = '-.', label='Mean')
    plt.plot(x_axis, y_axis, color='red', marker='o')
    plt.title('AGE RANGE', fontsize=14)
    plt.xlabel('AGE RANGE', fontsize=14)
    plt.ylabel('COUNT', fontsize=14)
    plt.grid(True)
    plt.show()

    print("Exit ProcessData")
    return 0