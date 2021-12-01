with open('inputs/day01.txt', 'r') as readings:
    depths = [int(number.strip()) for number in readings.readlines()]

# part one
print(sum([1 for i in range(len(depths)) if depths[i-1] < depths[i]]))

# part two
print(sum([1 for i in range(3, len(depths)+1) if sum(depths[i-3:i]) < sum(depths[i-2:i+1])]))
