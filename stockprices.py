#Billy Boone
#The file djia.csv contains all closing stock prices in the history of the Dow Jones Industrial Average,
# in the comma-separated value format. Compose a data type Entry that can hold one entry/row from the table, 
#with values for date, opening price, daily high, daily low, and closing price. 
#Then, compose a data type Table that reads the file to build an array of Entry objects and supports methods 
#for computing averages over various periods of time. 
# Finally, create interesting Table clients to produce plots of the data.The user can specify the time period of data to view.
#For example, plot the average of the daily highs and lows over a user-specified time period.
"""
To run this program input the following in the command line:

python stockprices.py djia.csv startdate(01-Jan-01) enddate(31-Dec-01) optional:field(open,close,high,low)

"""

import sys
import stddraw
import stdstats
from table import Table

def main():
    # Parse command line arguments for file name and date range
    file = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    field = sys.argv[4] if len(sys.argv) > 4 else None

    # Create a table object and calculate average prices
    table = Table(file)
    if field:
    # If a specific field is given, get only that average
        averages = table.get_avg_price(start_date, end_date, field)
    else:
    # If no field is specified, get all averages
        averages = table.get_avg_price(start_date, end_date)

    # Check if avg_price_data is a dictionary and then proceed
    if isinstance(averages, dict):
    # Print the averages
        for key, value in averages.items():
            print(f"{key}: {value:.2f}")
    # ... (rest of the code for drawing the bar chart)
    else:
        print(averages)  # In case avg_price_data is not a dictionary 

    #draw chart
    stddraw.setCanvasSize(600, 300)
    stddraw.setXscale(0, 5)  # Set a scale with enough space for 4 bars
    stddraw.setYscale(0, max(averages.values()) * 1.2)  # Scale y-axis for max value

    # Define colors for each bar
    colors = {"average_open": stddraw.RED, "average_close": stddraw.BLUE,
              "average_high": stddraw.GREEN, "average_low": stddraw.YELLOW}

    # Bar width
    bar_width = 0.5

    # Draw the bars for each average price
    for idx, (key, value) in enumerate(averages.items()):
        stddraw.setPenColor(colors[key])
        x = idx + 1  # x-coordinate for the bar
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width, value)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.text(x, value / 2, f"{value:.2f}")

    # Display the drawn canvas
    stddraw.show()

if __name__ == "__main__":
    main()