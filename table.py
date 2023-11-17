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
        relevant_entries = [e for e in self._entries if start <= e.date() <= end]

        if len(relevant_entries) == 0:
            return "No entries found."
        
        # If a specific field is provided, calculate its average
        if field is not None:
            total = sum(getattr(e, field)() for e in relevant_entries)
            return {f'average_{field}': total / len(relevant_entries)}

         
        # If no specific field is provided, calculate averages for all fields
        fields = ['open', 'close', 'high', 'low']
        averages = {}
        for field in fields:
            total = sum(getattr(e, field)() for e in relevant_entries)
            averages[f'average_{field}'] = total / len(relevant_entries)

        return averages


    


   

