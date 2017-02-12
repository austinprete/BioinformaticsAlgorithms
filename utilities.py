def read_lines_from_dataset(problem_number):
    f = open("resources/rosalind_ba%s.txt" % problem_number)
    lines = f.readlines()

    lines = list(map(lambda x: x.strip(), lines))

    return lines