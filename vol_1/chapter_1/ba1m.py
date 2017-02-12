"""
Implement NumberToPattern

Convert an integer to its corresponding DNA string.

Given: Integers index and k.

Return: NumberToPattern(index, k).
"""

import math

NUMBER_TO_LETTER = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def number_to_pattern(number, k):
    pattern = ''

    for index in range(0, k):
        index_multiplier = math.pow(4, k - (index + 1))

        current_number = int(number / index_multiplier)
        current_letter = NUMBER_TO_LETTER[current_number]

        number -= current_number * index_multiplier

        pattern += current_letter

    return pattern


if __name__ == '__main__':
    print(number_to_pattern(7992, 9))
