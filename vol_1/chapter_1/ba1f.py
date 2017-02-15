"""
Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of 'G' and 'C' in Genome. Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCCCATGGGCATCGGCCATACGCC")) are:

0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

Minimum Skew Problem

Find a position in a genome minimizing the skew.

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
"""

from utilities import read_lines_from_dataset

from common import compute_frequencies, number_to_pattern, pattern_to_number


def find_minimum_skew(genome: str):
    skew_list = [0]

    current_skew = 0

    for letter in genome:
        if letter == 'C':
            current_skew -= 1
        elif letter == 'G':
            current_skew += 1

        skew_list.append(current_skew)

    minimum_skew = min(skew_list)

    indices_and_skews = enumerate(skew_list)
    positions_with_min_skew = map(lambda x: x[0], filter(lambda x: x[1] == minimum_skew, indices_and_skews))

    return list(positions_with_min_skew)


if __name__ == '__main__':
    lines = read_lines_from_dataset('1f')

    genome = lines[0]

    result = find_minimum_skew(genome)

    result_string = ' '.join(map(lambda x: str(x), result))

    print(result_string)
