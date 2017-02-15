"""
We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two mismatches. The number of mismatches between strings p and q is called the Hamming distance between these strings and is denoted HammingDistance(p, q).

Hamming Distance Problem

Compute the Hamming distance between two DNA strings.

Given: Two DNA strings.

Return: An integer value representing the Hamming distance.
"""

from utilities import read_lines_from_dataset


def calculate_hamming_distance(dna_string_1: str, dna_string_2: str) -> int:
    non_matching_letters = filter(lambda letter_pair: letter_pair[0] != letter_pair[1], zip(dna_string_1, dna_string_2))

    non_matching_letters_list = list(non_matching_letters)

    hamming_distance = len(non_matching_letters_list)

    return hamming_distance


if __name__ == '__main__':
    lines = read_lines_from_dataset('1g')

    dna_string_1 = lines[0]
    dna_string_2 = lines[1]

    result = calculate_hamming_distance(dna_string_1, dna_string_2)

    print(result)
