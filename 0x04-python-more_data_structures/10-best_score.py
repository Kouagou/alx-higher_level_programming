#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        key = list(a_dictionary.keys())[0]
        for k, v in a_dictionary.items():
            if a_dictionary[key] < v:
                key = k
        return key
    return 'None'
