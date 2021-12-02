with open('inputs/day02.txt', 'r') as readings:
    commands = [line.split(" ") for line in readings.readlines()]

horizontal_pos = 0
depth = 0

# part one
for dir, speed in commands:
    if dir == 'forward':
        horizontal_pos = horizontal_pos + int(speed)
    elif dir == 'up':
        depth = depth - int(speed)
    elif dir == 'down':
        depth = depth + int(speed)

print(horizontal_pos * depth)

# part two
aim = 0
horizontal_pos = 0
depth = 0
for dir, speed in commands:
    if dir == 'forward':
        horizontal_pos = horizontal_pos + int(speed)
        depth = depth + aim*int(speed)
    elif dir == 'up':
        aim = aim - int(speed)
    elif dir == 'down':
        aim = aim + int(speed)

print(horizontal_pos * depth)
