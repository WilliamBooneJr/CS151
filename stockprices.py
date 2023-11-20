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

python stockprices.py djia.csv startdate(01-Jan-01) enddate(31-Dec-01)

For each year, a candlestick is drawn.
The color of the candlestick is red if the close price is lower than the 
open price (indicating a price decrease) and green otherwise (indicating a price increase).
The line (wick) represents the high and low prices.
The rectangle (body) represents the open and close prices.

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
    yearly_data = table.get_avg_price(start_date, end_date)

    # Prepare the canvas for drawing
    num_years = len(yearly_data)
    stddraw.setCanvasSize(800, 400)
    stddraw.setXscale(0, num_years + 1)
    max_price = max(max(year['high'] for year in yearly_data.values()), 1) #find the max of the max high prices
    stddraw.setYscale(0, max_price * 1.2) #set the y scale to 20% more than the max high price

    # Draw the candlesticks for each year
    for idx, (year, data) in enumerate(yearly_data.items()): #iterate over each index and key-value pair in yearly_data
        x = idx + 1 #position the candlestick
        open_price = data['open']
        close_price = data['close']
        high_price = data['high']
        low_price = data['low']

        color = stddraw.RED if close_price < open_price else stddraw.GREEN #set the color of the candlestick
        stddraw.setPenColor(color)

        # Draw the line for high and low prices
        stddraw.line(x, low_price, x, high_price)

        # Draw the rectangle for open and close prices
        rect_height = abs(close_price - open_price)
        rect_y = close_price if close_price < open_price else open_price
        stddraw.filledRectangle(x - 0.1, rect_y, 0.2, rect_height)

    # Display the drawn canvas
    stddraw.show()

if __name__ == "__main__":
    main()