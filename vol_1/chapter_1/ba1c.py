"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, we denote
its complementary nucleotide as p. The reverse complement of a DNA string Pattern = p1…pn is the string
Pattern = pn … p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.

For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC".

Reverse Complement Problem

Find the reverse complement of a DNA string.

Given: A DNA string Pattern.

Return: Pattern, the reverse complement of Pattern.
"""

from utilities import read_lines_from_dataset

COMPLEMENT_MAPPINGS = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}


def find_reverse_complement(pattern):
    complement = list(map(lambda letter: COMPLEMENT_MAPPINGS[letter], pattern))

    reverse_complement = ''.join(reversed(complement))

    return reverse_complement


if __name__ == '__main__':
    lines = read_lines_from_dataset('1c')

    pattern = lines[0]

    print(find_reverse_complement(pattern))
