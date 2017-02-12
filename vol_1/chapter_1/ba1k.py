import math

from utilities import read_lines_from_dataset

from vol_1.chapter_1.ba1l import pattern_to_number


def computing_frequencies(text, k):
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

    result = computing_frequencies(text, k)

    str_result = map(lambda x: str(x), result)

    print(' '.join(str_result))
