from typing import List


def read_lines_from_dataset(problem_number: str) -> List[str]:
    f = open("resources/rosalind_ba%s.txt" % problem_number)
    lines = f.readlines()

    lines = list(map(lambda x: x.strip(), lines))

    return lines


def convert_result_list_to_string(result_list: list) -> str:
    result_string_list = map(lambda x: str(x), result_list)

    return ' '.join(result_string_list)
