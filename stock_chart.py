import matplotlib.pyplot as plt 
plt.style.use('seaborn-whitegrid')
#import numpy as np 

def stock_chart(data, dates, y_min, y_range, company):
    """A function to generate a 5 day stock chart of a specific company given the date and price data"""
    # create the plot using data and set it to a certain colour
    # TODO: if trend after tweet is upwards, set to green, else set to red
    # TODO: check with team which linestyle is preferred
    green = '#7cfc00'
    red = '#ff0000'
    lines = plt.plot(data, color="black")#, linestyle='dashdot')

    

    # set the range of the x- and y-axes
    y_max = y_min + y_range
    plt.axis([0, 4, y_min, y_max])

    # label the ticks of the x axis
    positions = (0, 1, 2, 3, 4)
    plt.xticks(positions, dates)

    # label the x- and y-axes
    plt.xlabel('Dates')
    plt.ylabel('Price (USD)')

    # title the graph
    start_date = str(dates[0])
    end_date = str(dates[-1])
    plt.title("Stock Performance of " + company.capitalize() + " from " + start_date + " to " + end_date)

    when_red = [1, 1, 1, 1, 1]
    when_green = [0, 1, 1, 0, 0]
    # for i in range(len(data)):
    #     if i is 0:
    #         continue
    #     elif data[i] <= data[i-1]:
    #         when_green.append(0)
    #         when_red.append(1)
    #     else:
    #         when_green.append(1)
    #         when_red.append(0)    

    for i in range(len(positions) - 1):
        if data[i] >= data[i+1]:
            plt.fill_between([positions[i], positions[i+1]], [data[i], data[i+1]], 0, facecolor="red", alpha=0.2)
            #lines.axvspan(positions[i], positions[i+1], alpha=0.2, color='red')
        else:
            plt.fill_between([positions[i], positions[i+1]], [data[i], data[i+1]], 0, facecolor="green", alpha=0.2)
            #plt.fill_between(positions, data, 0, where= (positions > positions[i]) & (positions < positions[i+1]), facecolor="green", alpha=0.2)
            #lines.axvspan(positions[i], positions[i+1], alpha=0.2, color='green')

    # plt.fill_between(positions, data, 0, where=when_green, facecolor="green", alpha=0.2)
    # plt.fill_between(positions, data, 0, where=when_red, facecolor="red", alpha=0.2)

    print(when_green)
    print(when_red)

    plt.show()

    # save the graph as a png
    # person_startdate_company
    plt.savefig("static/stock_charts/" + start_date + "_" + company + "_stock_chart.png")


def main():
    data = [
        33, 25, 88, 50, 30
    ]
    dates = ['Jan 1', 'Jan 2', 'Jan 3', 'Jan 4', 'Jan 5']
    #stripes(data, dates, 100, 100)
    stock_chart(data, dates, 0, 100, "apple")

if __name__ == '__main__':
    main()