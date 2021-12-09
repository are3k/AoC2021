import numpy as np

def lanternfish_part_two(fishArray):
  ageCounter = np.empty(9, dtype=int)
  for i in range (0, 9):
    count = np.count_nonzero(fishArray == i)
    ageCounter[i] = count
  for day in range(0, 256):
    newAges = np.empty(9, dtype=int)
    for i in range(0,9):
      if i  == 0:
        newAges[6] = ageCounter[i]
        newAges[8] = ageCounter[i]
      elif i == 7:
        newAges[6] = newAges[6] + ageCounter[i]
      else:
        newAges[i-1] = ageCounter[i]
    np.copyto(ageCounter, newAges)
  return np.sum(ageCounter)

def lanternfish_part_one(fishList):
  for days in range(0, 80):
    newborn = []
    for i in range(0, len(fishList)):
      if fishList[i] > 0:
        fishList[i] -= 1
      elif fishList[i] == 0:
        fishList[i]=6
        newborn.append(8)
    fishList = fishList + newborn
  return len(fishList)

fishList = []
with open('input') as file:
  input =[
    line.strip() for line in file.readlines()
  ]
  file.close()
  for fish in input[0].split(','):
    fishList.append(int(fish))
  fishArray = np.array(fishList)


print(
    f"""Day 6:
    first solution: {lanternfish_part_one(fishList)}
    second solution: {lanternfish_part_two(fishArray)}"""
 )
