"""
We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern') ≤ d. Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.

Approximate Pattern Matching Problem

Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
"""

from utilities import convert_result_list_to_string, read_lines_from_dataset

from vol_1.chapter_1.ba1g import calculate_hamming_distance


def approximate_pattern_match(pattern: str, text: str, allowed_mismatches: int) -> [int]:
    pattern_length = len(pattern)

    matches = []

    for index in range(0, (len(text) - pattern_length) + 1):
        substring = text[index:index + len(pattern)]
        if calculate_hamming_distance(pattern, substring) <= allowed_mismatches:
            matches.append(index)

    return matches


if __name__ == '__main__':
    lines = read_lines_from_dataset('1h')

    pattern = lines[0]
    text = lines[1]
    allowed_mismatches = int(lines[2])

    result = approximate_pattern_match(pattern, text, allowed_mismatches)

    print(convert_result_list_to_string(result))
