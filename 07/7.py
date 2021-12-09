import numpy as np

def computeCost(crabsubArray, position):
  fuel = 0
  for crabsub in crabsubArray:
    fuel += (max(crabsub, position) - min(crabsub, position))
  return fuel

def computeCostTwo(crabsubArray, position):
  fuel = 0
  for crabsub in crabsubArray:
    fuel += (max(crabsub, position) - min(crabsub, position))
    for i in range(0, (max(crabsub, position) - min(crabsub, position))):
      fuel += i
  return fuel


def part_two(input):
  testvalues = []
  for i in range(min(input), max(input)):
    testvalues.append([i, computeCostTwo(input, i)])
  testvalues.append([i, computeCostTwo(input, i)])
  testArray = np.array(testvalues)
  testArray = testArray[testArray[:,1].argsort()]
  return testArray[0][1]
 
def part_one(input):
  testvalues = []
  for i in range(min(input), max(input)):
    testvalues.append([i, computeCost(input, i)])
  testArray = np.array(testvalues)
  testArray = testArray[testArray[:,1].argsort()]
  return testArray[0][1]

crabsubList = []
with open('input') as file:
  input =[
    line.strip() for line in file.readlines()
  ]
  file.close()
  for crabsub in input[0].split(','):
    crabsubList.append(int(crabsub))
  crabsubArray = np.array(crabsubList)


print(
    f"""Day 7:
    first solution: {part_one(crabsubArray)}
    second solution: {part_two(crabsubArray)}"""
 )
