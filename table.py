#Billy Boone
#The file djia.csv contains all closing stock prices in the history of the Dow Jones Industrial Average,
# in the comma-separated value format. Compose a data type Entry that can hold one entry/row from the table, 
#with values for date, opening price, daily high, daily low, and closing price. 
#Then, compose a data type Table that reads the file to build an array of Entry objects and supports methods 
#for computing averages over various periods of time. 
# Finally, create interesting Table clients to produce plots of the data.The user can specify the time period of data to view.
#For example, plot the average of the daily highs and lows over a user-specified time period.

import csv
from entry import Entry
from datetime import datetime

class Table:
    def __init__(self, filename):
        self._entries = []
        self._load_data(filename)

    def _load_data(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) # skip header row
            for row in reader:
                self._entries.append(Entry(row[0], row[1], row[2], row[3], row[4]))
    
    def entries(self):  #get list of entries
        return self._entries
    
    def get_avg_price(self, start_date, end_date, field=None):
        start = datetime.strptime(start_date, '%d-%b-%y')
        end = datetime.strptime(end_date, '%d-%b-%y')
        
        yearly_data = {}
        for entry in self._entries:
            entry_year = entry.date().year
            if start.year <= entry_year <= end.year:
                if entry_year not in yearly_data:
                    yearly_data[entry_year] = {'open': entry.open(), 'high': entry.high(), 
                                               'low': entry.low(), 'close': entry.close()}
                else:
                    yearly_data[entry_year]['high'] = max(yearly_data[entry_year]['high'], entry.high())
                    yearly_data[entry_year]['low'] = min(yearly_data[entry_year]['low'], entry.low())
                    yearly_data[entry_year]['close'] = entry.close()

        return yearly_data


    


   

