"""Module for defining Vigenere square and access functions"""

from string import ascii_uppercase
from numpy import array

numbers = range(0, 26)
letters = ascii_uppercase
row_list = []

for i in numbers:
    row = [(x + i) % 26 for x in numbers]
    row_list.append(row)

square = array(row_list, int)


def get_letter_from_index(index):
    """Get letter from given index"""
    return letters[index]


def get_index_from_letter(letter):
    """Get index of given letter"""
    return letters.index(letter)
