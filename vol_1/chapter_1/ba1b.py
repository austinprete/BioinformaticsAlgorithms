from functools import reduce

from utilities import read_lines_from_dataset

from vol_1.chapter_1.ba1a import pattern_count


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


if __name__ == '__main__':

    lines = read_lines_from_dataset('1b')

    text = lines[0]
    k = int(lines[1])

    result = frequent_words(text, k)

    print(' '.join(result))
