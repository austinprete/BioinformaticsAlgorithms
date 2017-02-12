"""
Implement PatternToNumber

Convert a DNA string to a number.

Given: A DNA string Pattern.

Return: PatternToNumber(Pattern).
"""

import math

LETTER_TO_NUMBER = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def pattern_to_number(pattern):
    pattern_length = len(pattern)

    number = 0

    for index in range(0, pattern_length):
        current_letter = pattern[index]

        number += math.pow(4, pattern_length - (index + 1)) * LETTER_TO_NUMBER[current_letter]

    return int(number)


if __name__ == '__main__':
    print(pattern_to_number('TATATCAGACCGAGGACTTTAAGACTA'))
