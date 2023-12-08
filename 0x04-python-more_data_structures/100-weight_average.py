#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        num = 0
        denom = 0
        for (x, y) in my_list:
            num += x * y
            denom += y
        return num / denom
    else:
        return 0
