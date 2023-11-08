#This module is used to define the functions used in the main program

import math

def calculate_std_dev(data):
    # Check if the data list has at least two elements, as standard deviation requires more than one data point.
    if len(data) < 2:
        return None  # Return None if there's not enough data for standard deviation.

    std_dev = math.sqrt(sum((x - sum(data) / len(data))**2 for x in data) / (len(data) - 1))
    return std_dev

def calculate_avg(data):
    # Check if the data list has at least one element, as average requires at least one data point.
    if len(data) < 1:
        return None  # Return None if there's not enough data for average.

    avg = sum(data) / len(data)
    return avg
