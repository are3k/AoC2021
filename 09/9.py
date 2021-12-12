import numpy as np
 
def part_one(input):
  riskLevel = 0
  lowPoints = []
  for i in range(100):
    for j in range(100):
      if i == 0 and j == 0:
        if int(input[i][j]) < min(int(input[i][j + 1]), int(input[i + 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
      elif i == 0 and j == 99:
        if int(input[i][j]) < min(int(input[i][j - 1]), int(input[i + 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
      elif i == 99 and j == 0:
        if int(input[i][j]) < min(int(input[i][j + 1]), int(input[i - 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
      elif i == 99 and j == 99:
        if int(input[i][j]) < min(int(input[i][j - 1]), int(input[i - 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
      elif i == 0:
        if int(input[i][j]) < min(int(input[i][j + 1]), int(input[i][j - 1]), int(input[i + 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
      elif i == 99:
        if int(input[i][j]) < min(int(input[i][j + 1]), int(input[i][j - 1]), int(input[i - 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
      elif j == 0:
        if int(input[i][j]) < min(int(input[i][j + 1]), int(input[i - 1][j]), int(input[i + 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
      elif j == 99:
        if int(input[i][j]) < min(int(input[i][j - 1]), int(input[i + 1][j]), int(input[i - 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
      else:
        if int(input[i][j]) < min(int(input[i][j + 1]), int(input[i][j - 1]), int(input[i + 1][j]), int(input[i - 1][j])):
          riskLevel += int(input[i][j]) + 1
          lowPoints.append([i, j])
  return riskLevel, lowPoints

class Basin:
  
  def __init__(self, heightmap, initialLowPoint) -> None:
      self.heightmap = heightmap
      self.foundPoints = np.empty((0, 3), dtype = int)
      self.foundPoints = np.vstack((self.foundPoints, np.array([initialLowPoint[0], initialLowPoint[1], 0])))
      self.lp = initialLowPoint
  
  def basinSize(self):
    hm = self.heightmap
    lp = self.lp
    while 0 in self.foundPoints[:,2].tolist():
      self.foundPoints = self.foundPoints[self.foundPoints[:,0].argsort()]
      for point in np.where(self.foundPoints[:,2] == 0):
        self.foundPoints = self.findAdjacent(self.foundPoints[point[0]])
        self.foundPoints[point[0]] = np.array([self.foundPoints[point[0]][0], self.foundPoints[point[0]][1], 1])
    return(len(self.foundPoints))

  
  def findAdjacent(self, lp):
    fp = self.foundPoints
    hm = self.heightmap
    if lp[0] < 99:
      if int(hm[lp[0] + 1][lp[1]]) < 9 and [lp[0] + 1, lp[1]] not in fp[...,0:2].tolist():
        fp = np.vstack((fp, np.array([lp[0] + 1, lp[1], 0])))
    if lp[0] > 0:
      if int(hm[lp[0] - 1][lp[1]]) < 9 and [lp[0] - 1, lp[1]] not in fp[...,0:2].tolist():
        fp = np.vstack((fp, np.array([lp[0] - 1, lp[1], 0])))
    if lp[1] < 99:
      if int(hm[lp[0]][lp[1] + 1]) < 9 and [lp[0], lp[1] + 1] not in fp[...,0:2].tolist():
          fp = np.vstack((fp, np.array([lp[0], lp[1] + 1, 0])))
    if lp[1] > 0:
      if int(hm[lp[0]][lp[1] - 1]) < 9 and [lp[0], lp[1] - 1] not in fp[...,0:2].tolist():
        fp = np.vstack((fp, np.array([lp[0], lp[1] - 1, 0])))
    return fp



def part_two(lowPoints, heightmap):
  basinSizes = []
  for lp in lowPoints:
    basin = Basin(heightmap, lp)
    basinSizes.append(basin.basinSize())
  basinSizes.sort(reverse=True)
  return np.product([basinSizes[0:3]])

heightmap = np.empty((100,100), dtype=int)
with open('input') as file:
  input = [
    line.strip() for line in file.readlines()
  ]
  file.close()
  heightmap = np.array(input)
  riskLevel, lowPoints = part_one(heightmap)

print(
    f"""Day 9:
    first solution: {riskLevel}
    second solution: {part_two(lowPoints, heightmap)}"""
 )
