"""
We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".

Frequent Words Problem

Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).
"""

from utilities import read_lines_from_dataset

from common import (compute_frequencies, pattern_count, number_to_pattern)


def frequent_words(text, k):
    frequent_patterns = set()
    count_list = []

    for index in range(0, (len(text) - k) + 1):
        pattern = text[index:index + k]
        count_list.append(pattern_count(text, pattern))

    max_count = max(count_list)

    for index in range(0, (len(text) - k) + 1):

        if count_list[index] == max_count:
            frequent_patterns.add(text[index:index + k])

    return frequent_patterns


def faster_frequent_words(text, k):
    frequency_array = compute_frequencies(text, k)

    max_count = max(frequency_array)

    frequent_patterns = set()

    for index in range(len(frequency_array)):
        if frequency_array[index] == max_count:
            pattern = number_to_pattern(index, k)

            frequent_patterns.add(pattern)

    return frequent_patterns


if __name__ == '__main__':
    lines = read_lines_from_dataset('1b')

    text = lines[0]
    k = int(lines[1])

    result = frequent_words(text, k)

    print(' '.join(result))

    print('\nUsing Faster Frequent Words:\n')

    result = faster_frequent_words(text, k)

    print(' '.join(result))
