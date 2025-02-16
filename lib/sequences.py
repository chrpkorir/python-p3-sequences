#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        return"Invalid"
    elif length == 1:
        return [0]
    elif length == 2:
        return [0, 1]
    
    series = [0, 1]
    while len(series) < length:
        series.append(series[-1] + series[-2])

        print(series)

print(print_fibonacci(9))
