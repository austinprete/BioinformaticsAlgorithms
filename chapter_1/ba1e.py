"""
Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome if there is an interval
of Genome of length L in which Pattern appears at least t times. For example, TGCATGCA forms a (25,3)-clump in the
following Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttacgatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.

Clump Finding Problem

Find patterns forming clumps in a string.

Given: A string Genome, and integers k, L, and t.

Return: All distinct k-mers forming (L, t)-clumps in Genome.
"""

from utilities import read_lines_from_dataset

from common import compute_frequencies, number_to_pattern, pattern_to_number


def slow_find_clumps(genome, k, L, t):
    """
    Note: this version is too slow to run on a non-trivial dataset
    """
    clumped_patterns = set()

    for index in range((len(genome) - L) + 1):
        substring = genome[index:index + L]

        frequency_array = compute_frequencies(substring, k)

        for index in range(len(frequency_array)):
            if frequency_array[index] >= t:
                clumped_patterns.add(number_to_pattern(index, k))

    return clumped_patterns


def find_clumps(genome, k, L, t):
    clumped_patterns = set()

    text = genome[:L]

    frequency_array = compute_frequencies(text, k)

    for index in range(len(frequency_array)):
        if frequency_array[index] >= t:
            clumped_patterns.add(number_to_pattern(index, k))

    for index in range(1, (len(genome) - L) + 1):
        first_pattern = genome[index - 1:(index + k) - 1]

        pattern_index = pattern_to_number(first_pattern)
        frequency_array[pattern_index] -= 1

        last_pattern = genome[(index + L) - k:index + L]

        pattern_index = pattern_to_number(last_pattern)
        frequency_array[pattern_index] += 1

        if frequency_array[pattern_index] >= t:
            clumped_patterns.add(last_pattern)

    return clumped_patterns


if __name__ == '__main__':
    lines = read_lines_from_dataset('1e')

    genome = lines[0]
    k, L, t = map(lambda x: int(x), lines[1].split(' '))

    result = find_clumps(genome, k, L, t)

    print(' '.join(result))
