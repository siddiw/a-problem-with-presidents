import pandas
import numpy
import matplotlib.pyplot as plt

def drawGraph(dataframe):
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

    # Tabularizing by appending everything to a dictionary
    data = {
        "Statistic": ["Mean Age", "Weighted Mean Age", "Median Age", "Mode Age", "Maximum Age", "Minimum Age", "Standard Deviation"],
        "Age (Days)": [mean, weighted_mean, median, list(mode), max, min, std],
        "Age (Years)": [mean / 365, weighted_mean / 365, median / 365, [x / 365 for x in list(mode)], max / 365, min / 365, std / 365]
    }

    # Creating dataframe from the dictionary
    dataframe_stats = pandas.DataFrame.from_dict(data)
    dataframe_stats.style.hide_index()

    x_axis = ["Mean", "Weighted Mean", "Median", "Maximum", "Minimum"]
    x_axis_positions = range(len(x_axis))
    y_axis = [mean, weighted_mean, median, max, min]
    plt.figure(figsize=(8, 6))
    plt.bar(x_axis_positions, y_axis)
    plt.ylabel("Age (in Days)")
    plt.title("Statistics of Presidential Ages")

    plt.axhline(y = mean + std, color = 'r', linestyle = '--', label='Standard Deviation')
    plt.axhline(y = mean, color = 'gray', linestyle = '-.', label='Mean')
    plt.axhline(y = mean - std, color = 'r', linestyle = '--')

    plt.legend(labels=['Standard Deviation', 'Mean'])

    plt.xticks(x_axis_positions, x_axis)
    plt.show()

    # Plotting frequency distribution using matplotlib
    x_axis_positions = [i for i in range(len(value_counts))]
    plt.figure(figsize=(15, 4))
    plt.bar(x_axis_positions, value_counts)
    plt.xlabel("Age (years)")
    plt.ylabel("Number of Presidents")
    plt.title("Frequency of Presidential Ages")

    plt.xticks(x_axis_positions, value_counts.keys())
    plt.yticks(range(value_counts.max() + 1))
    plt.show()

    print("Exit ProcessData")
    return 0