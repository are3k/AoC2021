import numpy as np

class OctySwarm:
  
  def __init__(self, octy) -> None:
      self.flashedCount = 0
      self.octy = octy
      self.fullFlash = False

  def liftEnergyLevel(self):
    for row in range(10):
      for item in range(10):
        self.octy[row][item] += 1

  def flash(self):
    while np.count_nonzero(self.octy == 10) > 0:
      self.flashedCount += np.count_nonzero(self.octy == 10)
      flashed = np.array(np.where(self.octy == 10))
      flashed = np.vstack(flashed)
      self.riseAdjacent(flashed)
    self.octy[self.octy > 9] = 0
    if np.count_nonzero(self.octy == 0) == 100:
      self.fullFlash = True

  def riseAdjacent(self, flashed):
    for i in range(len(flashed[0])):
      x, y = flashed[:,i]
      self.octy[x][y] += 1
    for i in range(len(flashed[0])):
      x, y = flashed[:,i]
      if x > 0 and y > 0 and x < 9 and y < 9:
        if self.octy[x + 1][y] < 10: self.octy[x + 1][y] += 1
        if self.octy[x - 1][y] < 10: self.octy[x - 1][y] += 1
        if self.octy[x][y + 1] < 10: self.octy[x][y + 1] += 1
        if self.octy[x][y - 1] < 10: self.octy[x][y - 1] += 1
        if self.octy[x + 1][y + 1] < 10: self.octy[x + 1][y + 1] += 1
        if self.octy[x + 1][y - 1] < 10: self.octy[x + 1][y - 1] += 1
        if self.octy[x - 1][y + 1] < 10: self.octy[x - 1][y + 1] += 1
        if self.octy[x - 1][y - 1] < 10: self.octy[x - 1][y - 1] += 1
      elif x == 9 and y == 9:
        if self.octy[x - 1][y] < 10: self.octy[x - 1][y] += 1
        if self.octy[x][y - 1] < 10: self.octy[x][y - 1] += 1
        if self.octy[x - 1][y - 1] < 10: self.octy[x - 1][y - 1] += 1
      elif x == 0 and y == 9:
        if self.octy[x + 1][y] < 10: self.octy[x + 1][y] += 1
        if self.octy[x][y - 1] < 10: self.octy[x][y - 1] += 1
        if self.octy[x + 1][y - 1] < 10: self.octy[x + 1][y - 1] += 1
      elif x == 9 and y == 0:
        if self.octy[x - 1][y] < 10: self.octy[x - 1][y] += 1
        if self.octy[x][y + 1] < 10: self.octy[x][y + 1] += 1
        if self.octy[x - 1][y + 1] < 10: self.octy[x - 1][y + 1] += 1
      elif x == 0 and y == 0:
        if self.octy[x + 1][y] < 10: self.octy[x + 1][y] += 1
        if self.octy[x][y + 1] < 10: self.octy[x][y + 1] += 1
        if self.octy[x + 1][y + 1] < 10: self.octy[x + 1][y + 1] += 1
      elif x == 0:
        if self.octy[x + 1][y] < 10: self.octy[x + 1][y] += 1
        if self.octy[x][y + 1] < 10: self.octy[x][y + 1] += 1
        if self.octy[x][y - 1] < 10: self.octy[x][y - 1] += 1
        if self.octy[x + 1][y + 1] < 10: self.octy[x + 1][y + 1] += 1
        if self.octy[x + 1][y - 1] < 10: self.octy[x + 1][y - 1] += 1
      elif y == 0:
        if self.octy[x + 1][y] < 10: self.octy[x + 1][y] += 1
        if self.octy[x - 1][y] < 10: self.octy[x - 1][y] += 1
        if self.octy[x][y + 1] < 10: self.octy[x][y + 1] += 1
        if self.octy[x + 1][y + 1] < 10: self.octy[x + 1][y + 1] += 1
        if self.octy[x - 1][y + 1] < 10: self.octy[x - 1][y + 1] += 1
      elif x == 9:
        if self.octy[x - 1][y] < 10: self.octy[x - 1][y] += 1
        if self.octy[x][y + 1] < 10: self.octy[x][y + 1] += 1
        if self.octy[x][y - 1] < 10: self.octy[x][y - 1] += 1
        if self.octy[x - 1][y + 1] < 10: self.octy[x - 1][y + 1] += 1
        if self.octy[x - 1][y - 1] < 10: self.octy[x - 1][y - 1] += 1
      elif y == 9:
        if self.octy[x + 1][y] < 10: self.octy[x + 1][y] += 1
        if self.octy[x - 1][y] < 10: self.octy[x - 1][y] += 1
        if self.octy[x][y - 1] < 10: self.octy[x][y - 1] += 1
        if self.octy[x + 1][y - 1] < 10: self.octy[x + 1][y - 1] += 1
        if self.octy[x - 1][y - 1] < 10: self.octy[x - 1][y - 1] += 1
    return None

def part_one(octy):
  octyswarm = OctySwarm(octy)
  for step in range(100):
    octyswarm.liftEnergyLevel()
    octyswarm.flash()
  return octyswarm.flashedCount

def part_two(octy):
  octyswarm = OctySwarm(octy)
  stepCounter = 0
  while not octyswarm.fullFlash:
    stepCounter += 1
    octyswarm.liftEnergyLevel()
    octyswarm.flash()
  return stepCounter

octy = np.empty((0, 10), dtype = int)
with open('input') as file:
  while (line := file.readline().rstrip()):
    octy = np.vstack((octy, np.array([[int(i) for i in line]])))
    octyTwo = octy.copy()

print(
    f"""Day 11:
    first solution: {part_one(octy)}
    second solution: {part_two(octyTwo)}"""
 )
