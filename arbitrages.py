from typing import Tuple, List, Dict
from math import log
import csv

def calculate_rates(rates_array, conversion_rates_EUR, index):
    for source_curr in range(170):
        for dest_curr in range(170):
            rates_array[source_curr][dest_curr] = conversion_rates_EUR[index[source_curr]]/conversion_rates_EUR[index[dest_curr]]

def negate_logarithm_convertor(rates_array):
    return [[-log(edge) for edge in row] for row in rates_array]

def find_arbitrage(rates_array, conversion_rates_EUR, index):
    #Finds arbitrages via Bellman-Ford algorithm
    rates_array = negate_logarithm_convertor(rates_array)

    source = 0
    n = len(rates_array)

    min_dist = [float('inf')] * n

    pre = [-1] * n
    
    min_dist[source] = source

    output = []

    # 'Relax edges |V-1| times'
    for _ in range(n-1):
        for source_curr in range(n):
            for dest_curr in range(n):
                if min_dist[dest_curr] > min_dist[source_curr] + rates_array[source_curr][dest_curr]:
                    min_dist[dest_curr] = min_dist[source_curr] + rates_array[source_curr][dest_curr]
                    pre[dest_curr] = source_curr

    # if we can still relax edges, then we have a negative cycle
    for source_curr in range(n):
        for dest_curr in range(n):
            if min_dist[dest_curr] > min_dist[source_curr] + rates_array[source_curr][dest_curr]:
                # negative cycle exists, and use the predecessor chain to print the cycle
                print_cycle = [dest_curr, source_curr]
                # Start from the source and go backwards until you see the source vertex again or any vertex that already exists in print_cycle array
                while pre[source_curr] not in  print_cycle:
                    print_cycle.append(pre[source_curr])
                    source_curr = pre[source_curr]
                print_cycle.append(pre[source_curr])
                output.append([index[i] for i in print_cycle[::-1]])

    return output


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

    arbitrages = find_arbitrage(rates_array,conversion_rates_EUR,index)

    sourceFile = open('arbitrage.txt', 'w')
    print("arbitrages", file=sourceFile)
    for arbitrage in arbitrages:
        for currency in arbitrage:
            print(currency, end = " ", file = sourceFile)
        print(file = sourceFile)
    sourceFile.close()