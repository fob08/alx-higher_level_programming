#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    number = 0
    dico = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dico.keys():
            return 0
        elif dico[i] >= dico[j]:
            number += dico[i]
        else:
            number -= dico[i]
    number += dico[roman_string[-1]]
    return number
