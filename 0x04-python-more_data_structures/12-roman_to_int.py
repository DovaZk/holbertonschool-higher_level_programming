#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    l = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if type(roman_string) is not str or roman_string is None:
        return num

    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            num += l[roman_string[i]]
        elif l[roman_string[i]] >= l[roman_string[i + 1]]:
            num += l[roman_string[i]]
        else:
            num -= l[roman_string[i]]

    return num
