#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        c = ""
        if i % 3 == 0 and i % 5 == 0:
            c += "FizzBuzz"
        elif i % 3 == 0:
            c += "Fizz"
        elif i % 5 == 0:
            c += "Buzz"
        else:
            c += str(i)
        print("{} ".format(c), end='')
