"""
Given an integer k, we define the frequency array of a string Text as an array of length 4k, where the i-th element of
the array holds the number of times that the i-th k-mer (in the lexicographic order) appears in Text (see Figure 1.

Computing a Frequency Array

Generate the frequency array of a DNA string.

Given: A DNA string Text and an integer k.

Return: The frequency array of k-mers in Text.
"""

import math

from utilities import read_lines_from_dataset

from common import pattern_to_number


def compute_frequencies(text, k):
    frequency_array = []

    for index in range(int(math.pow(4, k))):
        frequency_array.append(0)

    for index in range((len(text) - k) + 1):
        pattern = text[index:index + k]

        pattern_index = pattern_to_number(pattern)
        frequency_array[pattern_index] += 1

    return frequency_array


if __name__ == '__main__':
    lines = read_lines_from_dataset('1k')

    text = lines[0]
    k = int(lines[1])

    result = compute_frequencies(text, k)

    str_result = map(lambda x: str(x), result)

    print(' '.join(str_result))
