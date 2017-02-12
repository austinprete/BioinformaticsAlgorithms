"""
In this problem, we ask a simple question: how many times can one string occur as a substring of another? Recall from “Find the Most Frequent Words in a String” that different occurrences of a substring can overlap with each other. For example, ATAATA occurs three times in CGATATATCCATAGCGATATATCCATAG.

Pattern Matching Problem

Find all occurrences of a pattern in a string.

Given: Strings Pattern and Genome.

Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.
"""

from utilities import read_lines_from_dataset


def find_pattern_matches(pattern, genome):
    pattern_length = len(pattern)

    match_indices = []

    for index in range((len(genome) - pattern_length) + 1):
        substring = genome[index:index + pattern_length]

        if substring == pattern:
            match_indices.append(index)

    return match_indices


if __name__ == '__main__':
    lines = read_lines_from_dataset('1d')

    pattern = lines[0]
    genome = lines[1]

    result = find_pattern_matches(pattern, genome)

    result = map(lambda x: str(x), result)

    print(' '.join(result))
