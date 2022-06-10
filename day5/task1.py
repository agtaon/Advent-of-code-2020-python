# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:29:49 2022

@author: agfrxa
"""


maximum_prod = 0
with open(r'C:\Users\agfrxa\Python\advent of code 2020\day5\input.txt') as f:
    boarding_passes = f.readlines()

    for boarding_pass in boarding_passes:
        seat_range = [0, 127]
        col_range = [0, 7]
        for char in boarding_pass:
            if char == 'F':
                seat_range[1] -= (seat_range[1] - seat_range[0] + 1) / 2

            if char == 'B':
                seat_range[0] += (seat_range[1] - seat_range[0] + 1) / 2

            if char == 'L':
                col_range[1] -= (col_range[1] - col_range[0] + 1) / 2

            if char == 'R':
                col_range[0] += (col_range[1] - col_range[0] + 1) / 2

        if seat_range[0] * 8 + col_range[0] > maximum_prod:
            maximum_prod = seat_range[0] * 8 + col_range[0]
            print(maximum_prod)

print(maximum_prod)