from utilities import read_lines_from_dataset


def pattern_count(text, pattern):
    pattern_length = len(pattern)
    count = 0

    for index in range(0, (len(text) - pattern_length) + 1):
        if text[index:index + len(pattern)] == pattern:
            count += 1

    return count


if __name__ == '__main__':
    lines = read_lines_from_dataset('1a')

    text = lines[0]
    pattern = lines[1]

    result = pattern_count(text, pattern)

    print(result)
