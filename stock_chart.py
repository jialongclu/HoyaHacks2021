import matplotlib.pyplot as plt 
plt.style.use('seaborn-whitegrid')
#import numpy as np 

def stock_chart(data, dates, y_min, y_range, company):
    """A function to generate a 5 day stock chart of a specific company given the date and price data"""
    # create the plot using data and set it to a certain colour
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

    # fills in the area under the graph red or green to indicate if the stock did better (green) or worse (red)
    for i in range(len(positions) - 1):
        if data[i] >= data[i+1]:
            plt.fill_between([positions[i], positions[i+1]], [data[i], data[i+1]], 0, facecolor="red", alpha=0.2)
        else:
            plt.fill_between([positions[i], positions[i+1]], [data[i], data[i+1]], 0, facecolor="green", alpha=0.2)

    # use to display plot while debugging
    #plt.show()

    # save the graph as a png with the format startdate_company_stock_chart.png
    plt.savefig("static/stock_charts/" + start_date + "_" + company + "_stock_chart.png")


def main():
    data = [33, 25, 88, 50, 30]
    dates = ['Jan 1', 'Jan 2', 'Jan 3', 'Jan 4', 'Jan 5']
    stock_chart(data, dates, 0, 100, "apple")

if __name__ == '__main__':
    main()