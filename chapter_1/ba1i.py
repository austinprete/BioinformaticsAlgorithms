"""
We defined a mismatch in “Compute the Hamming Distance Between Two Strings”. We now generalize
“Find the Most Frequent Words in a String” to incorporate mismatches as well.

Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of
occurrences of Pattern in Text with at most d mismatches. For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4
because AAAAA appears four times in this string with at most one mismatch: AACAA, ATAAA, AAACA, and AAAGA.
Note that two of these occurrences overlap.

A most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Countd(Text, Pattern)
among all k-mers. Note that Pattern does not need to actually appear as a substring of Text; for example, AAAAA is the
most frequent 5-mer with 1 mismatch in AACAAGCTGATAAACATTTAAAGAG, even though AAAAA does not appear exactly in this
string. Keep this in mind while solving the following problem.

Frequent Words with Mismatches Problem

Find the most frequent k-mers with mismatches in a string.

Given: A string Text as well as integers k and d.

Return: All most frequent k-mers with up to d mismatches in Text.
"""
import sys

from common import calculate_hamming_distance, find_neighbors
from utilities import read_lines_from_dataset


def approximate_pattern_count(pattern: str, text: str, allowed_mismatches: int) -> int:
    pattern_length = len(pattern)

    count = 0

    for index in range(0, (len(text) - pattern_length) + 1):
        substring = text[index:index + len(pattern)]
        if calculate_hamming_distance(pattern, substring) <= allowed_mismatches:
            count += 1

    return count


def find_frequent_words_with_mismatches(text, k, d):
    pattern_set = set()

    for index in range(len(text) - k + 1):
        substring = text[index:index + k]

        if substring in pattern_set:
            continue
        else:
            neighbors = find_neighbors(substring, d)
            for neighbor in neighbors:
                pattern_set.add(neighbor)

    frequent_words = set()
    highest_count = 0

    for pattern in pattern_set:
        pattern_count = approximate_pattern_count(pattern, text, d)

        if pattern_count > highest_count:
            frequent_words.clear()
            frequent_words.add(pattern)
            highest_count = pattern_count
        elif pattern_count == highest_count:
            frequent_words.add(pattern)

    return frequent_words


if __name__ == '__main__':
    lines = read_lines_from_dataset('1i')

    text = lines[0]
    integer_inputs = list(map(lambda x: int(x), lines[1].split(' ')))
    k = integer_inputs[0]
    d = integer_inputs[1]

    result = find_frequent_words_with_mismatches(text, k, d)

    for word in result:
        print("%s " % word, end='')
