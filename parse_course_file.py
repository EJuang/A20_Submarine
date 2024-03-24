def parse_course_file(filePath):
    instruction_sets = []
    with open(filePath) as file:
        for line in file:
            instruction_sets.append(tuple(line.strip().split(' ')))

    return instruction_sets