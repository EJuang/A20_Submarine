from parse_course_file import parse_course_file

def calculate_position(filePath):
    instruction_sets = parse_course_file(filePath)
    return process_course(instruction_sets)

def process_course(instruction_sets):
    horizontal_distance = int(0)
    depth = int(0)
    for instruction_set in instruction_sets:
        instruction_value = parse_course_instruction_value(instruction_set)
        if instruction_set[0] == 'forward':
            horizontal_distance += int(instruction_value)
        elif instruction_set[0] == 'down':
            depth += int(instruction_value)
        elif instruction_set[0] == 'up':
            depth -= int(instruction_value)
        else:
            raise ValueError('Must provide a valid course instruction type')
    
    return (horizontal_distance, depth, horizontal_distance * depth)

def parse_course_instruction_value(instruction_set):
    try:
        instruction_value = int(instruction_set[1])
    except ValueError:
        raise ValueError('Must provide a valid numerical input for course instruction')
    except IndexError:
        raise ValueError('Must provide a numerical input for course instruction')
    
    if instruction_value <= 0:
        raise ValueError('Must provide a positive value for course instruction')
    
    return instruction_value