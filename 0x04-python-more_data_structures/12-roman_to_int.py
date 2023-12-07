#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or None:
        return 0
    else:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                          'C': 100, 'D': 500, 'M': 1000}
        numerals = []
        for i in roman_string:
            for k, v in roman_numerals.items():
                if i is k:
                    numerals.append(v)

        number = 0
        for j in range(len(numerals)):
            if (j + 1) < len(numerals):
                if numerals[j] < numerals[j + 1]:
                    number -= numerals[j]
                else:
                    number += numerals[j]
            else:
                number += numerals[j]
        return number
