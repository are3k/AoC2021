import itertools
import numpy as np

def fold(points, f):
  folddirection, foldline =f.split(' ')[-1].split('=')
  foldline = int(foldline)
  if folddirection == 'x':
    for point in points:
      if point[0] > foldline:
        point[0] -= (foldline + 1)
      else:
        point[0] = (foldline - 1) - point[0]
  elif folddirection == 'y':
    for point in points:
      if point[1] > foldline:
        difference = point[1] - foldline
        point[1] = foldline - difference

  points.sort()
  return list(points for points,_ in itertools.groupby(points))

def part_one(points, f):
  folded = fold(points, f)
  return len(folded)

def part_two(points, instructions):
  for instruction in instructions:
    points = fold(points, instruction)
    npPoints = np.array(points)
  printCode = []
  printCodeRow = []
  for col in range(max(npPoints[:,1]) + 1):
    for row in range(max(npPoints[:,0]) + 1):
      printCodeRow.append('.')
    printCode.append(printCodeRow)
  npPrintCode = np.array(printCode)
  for point in npPoints:
    print('point', point)
    npPrintCode[point[1],point[0]] = '#'
  np.savetxt('output', npPrintCode, fmt='%s')
  print(npPrintCode)
  return None

points = []
instructions = []
with open('input') as file:
  while (line := file.readline().rstrip()):
    if line[0] == 'f':
      instructions.append(line)
    else:
      x, y = line.split(',')
      points.append([int(x), int(y)])

print(
    f"""Day 13:
    first solution: {part_one(points.copy(), instructions[0])}
    second solution: {part_two(points.copy(), instructions)}"""
)
