from calculate_submarine_distance import calculate_position

distances = calculate_position('./InputFiles/submarine_kata_input.txt')
print('Horizontal Distance: ' + str(distances[0]))
print('Depth: ' + str(distances[1]))
print('Multiplied Distance: ' + str(distances[2]))