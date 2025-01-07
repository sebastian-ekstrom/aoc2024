import sys
from collections import defaultdict

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    numbers = [int(line.strip()) for line in file]

results = defaultdict(int)
for number in numbers:
    prices = [number % 10]
    for i in range(2000):
        number = (number ^ (number * 64)) % 16777216
        number = (number ^ (number // 32)) % 16777216
        number = (number ^ (number * 2048)) % 16777216
        prices.append(number % 10)

    single_results = {}
    for i in range(len(prices) - 4):
        d1 = prices[i+1] - prices[i]
        d2 = prices[i+2] - prices[i+1]
        d3 = prices[i+3] - prices[i+2]
        d4 = prices[i+4] - prices[i+3]
        if (d1, d2, d3, d4) not in single_results:
            single_results[(d1, d2, d3, d4)] = prices[i+4]
    for changes, price in single_results.items():
        results[changes] += price

print(max(results.values()))
if debug:
    max_value = max(results.values())
    for changes, total in results.items():
        if total == max_value:
            print(changes)
            break

