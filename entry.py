#Billy Boone
#The file djia.csv contains all closing stock prices in the history of the Dow Jones Industrial Average,
# in the comma-separated value format. Compose a data type Entry that can hold one entry/row from the table, 
#with values for date, opening price, daily high, daily low, and closing price. 
#Then, compose a data type Table that reads the file to build an array of Entry objects and supports methods 
#for computing averages over various periods of time. 
# Finally, create interesting Table clients to produce plots of the data.The user can specify the time period of data to view.
#For example, plot the average of the daily highs and lows over a user-specified time period.

from datetime import datetime


class Entry:
    def __init__(self, date, open, high, low, close):
        self._date = datetime.strptime(date, '%d-%b-%y')
        self._open = float(open)
        self._high = float(high)
        self._low = float(low)
        self._close = float(close)

    def date(self):
        return self._date
    
    def open(self):
        return self._open
    
    def high(self):
        return self._high
    
    def low(self):
        return self._low
    
    def close(self):
        return self._close
    
    def __str__(self):
        return f"{self._date}, {self._open}, {self._high}, {self._low}, {self._close}"
