import matplotlib.pyplot as plt

def graphSnowfall(t):
    #read data from the text file and each line is converted to an integer
    with open(t, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file]

    #make a dictionary to store the counts of each 10 cm range
    range_counts = {}

    #loop through the snowfall data and update the dictionary
    for snowfall in snowfall_data:
        range_lower = (snowfall // 10) * 10
        range_counts[range_lower] = range_counts.get(range_lower, 0) + 1

    #extract data to plot
    ranges = list(range(0, max(snowfall_data) + 10, 10))
    counts = [range_counts.get(r, 0) for r in ranges]

    #plot data
    plt.bar(ranges[:-1], counts, width=10, align='edge')
    plt.xlabel('Snowfall Range (cms)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')
    plt.show()

#below is a function that showcases the result of this code logic:
graphSnowfall('snowfall_data.txt')
