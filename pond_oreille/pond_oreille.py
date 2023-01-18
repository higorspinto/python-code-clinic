import csv
import numpy as np
import argparse
from datetime import datetime
from matplotlib import pyplot as plt

### read data from csv file
def read_files():
    date_time_lst = []
    barometric_pressure_lst = []
    files = [
        "./resources/Environmental_Data_Deep_Moor_2012.txt",
        "./resources/Environmental_Data_Deep_Moor_2013.txt",
        "./resources/Environmental_Data_Deep_Moor_2014.txt",
        "./resources/Environmental_Data_Deep_Moor_2015.txt"
    ]
    for file in files:
        with open(file) as csv_file:
            reader = csv.DictReader(csv_file, delimiter='\t')
            for row in reader:
                date_time_lst.append(datetime.strptime(row["date       time    "], '%Y_%m_%d %H:%M:%S'))
                barometric_pressure_lst.append(float(row["Barometric_Press"]))
    return date_time_lst, barometric_pressure_lst

### loading data into numpy arrays
def read_data(initial_date, final_date):
    date_time_lst, barometric_pressure_lst = read_files()

    date_time = np.array(date_time_lst)
    barometric_pressure = np.array(barometric_pressure_lst)
    slope = None

    if initial_date and final_date:
        start_idx = np.searchsorted(date_time, initial_date)
        end_idx = np.searchsorted(date_time, final_date)

        slope = calculate_slope(date_time, barometric_pressure, start_idx, end_idx)

        date_time = np.array(date_time_lst[start_idx:end_idx])
        barometric_pressure = np.array(barometric_pressure_lst[start_idx:end_idx])        

    return date_time, barometric_pressure, slope

### calculating slop
def calculate_slope(date_time, barometric_pressure, start_idx, end_edx):
    dy = barometric_pressure[end_idx] - barometric_pressure[start_idx]
    dt = date_time[end_idx] - date_time[start_idx]
    slope = dy/dt

### ploting results
def plot(date_time, barometric_pressure):
    plt.title("Pond Oreille Weather") 
    plt.xlabel("Date")
    plt.xticks(rotation=90)
    plt.ylabel("Barometric Pressure") 
    plt.plot(date_time, barometric_pressure, linestyle = 'dotted') 
    plt.show()

### parse cli dates
def parse_arg_dates(args):
    initial_date = args.initial_date
    final_date = args.final_date
    if initial_date is None or final_date is None:
        return None, None
    return datetime.strptime(initial_date, '%Y/%m/%d'), datetime.strptime(final_date, '%Y/%m/%d')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plots Pond Oreille Weather')
    parser.add_argument('--initial_date', type=str, help='Initial date. Format: %Y/%m/%d')
    parser.add_argument('--final_date', type=str, help='Final date. Format: %Y/%m/%d')
    args = parser.parse_args()
    initial_date, final_date = parse_arg_dates(args)

    date_time, barometric_pressure, slope = read_data(initial_date, final_date)
    plot(date_time, barometric_pressure, slope)