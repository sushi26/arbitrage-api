from typing import Tuple, List, Dict
import csv

def calculate_rates(rates_array: List[List[float]], conversion_rates_EUR: Dict[float], index: Dict[str]):
    for i in range(170):
        for j in range(170):
            rates_array[i][j] = conversion_rates_EUR[index[i]]/conversion_rates_EUR[index[j]]

def bellman_ford(rates_array: List[List[float]], conversion_rates_EUR: Dict[float], index: Dict[str]):
    pass


if __name__ == "__main__":
    rates_array = [[0] * 170] * 170
    conversion_rates_EUR = dict()
    index = dict()
    with open("data.txt", 'r') as file:
        csvreader = csv.reader(file)
        for i, row in enumerate(csvreader):
            if (i == 0) :
                continue
            conversion_rates_EUR[row[0]] = float(row[1])
            index[i-1] = row[0]
    calculate_rates(rates_array, conversion_rates_EUR, index)
    print(type(conversion_rates_EUR))