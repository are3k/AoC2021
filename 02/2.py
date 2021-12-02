import re

depth = 0
position = 0
aim = 0

# Part two (was also part One, just needed small change)
with open('input.txt') as file:
  while (line := file.readline().rstrip()):
    commandParts = re.split(' +', line)
    if commandParts[0] == "forward":
        position += int(commandParts[1])
        depth = depth + (aim * int(commandParts[1]))
    elif commandParts[0] == "down": aim += int(commandParts[1])
    elif commandParts[0] == "up": aim -= int(commandParts[1])
    else: print('Some error with this line ' + line)
  print('Depth after all commands : ' + str(depth))
  print('Position after all commands: ' + str(position) )
  print('Solution: ' + str(position * depth))
  