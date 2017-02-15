"""
The d-neighborhood Neighbors(Pattern, d) is the set of all k-mers whose Hamming distance from Pattern does not exceed d.

Generate the d-Neighborhood of a String

Find all the neighbors of a pattern.

Given: A DNA string Pattern and an integer d.

Return: The collection of strings Neighbors(Pattern, d).
"""

from utilities import convert_result_list_to_string, read_lines_from_dataset

from vol_1.chapter_1.ba1g import calculate_hamming_distance

NUCLEOTIDES = ['A', 'C', 'G', 'T']


def find_neighbors(pattern: str, allowed_mismatches: int) -> [str]:
    if allowed_mismatches == 0:
        return [pattern]

    if len(pattern) == 1:
        return NUCLEOTIDES

    neighbors = set()

    first_symbol = pattern[0]

    suffix = pattern[1:]
    suffix_neighbors = find_neighbors(suffix, allowed_mismatches)

    for suffix_neighbor in suffix_neighbors:
        if calculate_hamming_distance(suffix, suffix_neighbor) < allowed_mismatches:
            for nucleotide in NUCLEOTIDES:
                neighbors.add(nucleotide + suffix_neighbor)
        else:
            neighbors.add(first_symbol + suffix_neighbor)

    return list(neighbors)


if __name__ == '__main__':
    lines = read_lines_from_dataset('1n')

    pattern = lines[0]
    allowed_mismatches = int(lines[1])

    result = find_neighbors(pattern, allowed_mismatches)

    print(convert_result_list_to_string(result).replace(' ', '\n'))
