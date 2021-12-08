import numpy as np

class Matrix:
  
  def __init__(self):
    self.xyVectors = []
    self.points = np.zeros((1,3), dtype=int)

  def setVector(self, vectors):
   self.xyVectors = vectors
  
  def setPoints(self):
    for vector in self.xyVectors:
      minX = min(vector[0], vector[2])
      minY = min(vector[1], vector[3])
      maxX = max(vector[0], vector[2])
      maxY = max(vector[1], vector[3])
      diffX = max(vector[0], vector[2]) - min(vector[0], vector[2])
      diffY = max(vector[1], vector[3]) - min(vector[1], vector[3])
      if vector[0] == vector[2]:
        for y in range(minY, maxY + 1):
          self.incrementPoint(vector[0], y)
      elif vector[1] == vector[3]:
        for x in range(minX, maxX + 1):
          self.incrementPoint(x, vector[1])
      elif (diffX == diffY):
        for increment in range(0, diffX + 1):
          if vector[0] < vector[2] and vector[1] < vector[3]:
            x = minX + increment
            y = minY + increment
          elif vector[0] > vector[2] and vector[1] < vector[3]:
            x = maxX - increment
            y = minY + increment
          elif vector[0] < vector[2] and vector[1] > vector[3]:
            x = minX + increment
            y = maxY - increment
          elif vector[0] > vector[2] and vector[1] > vector[3]:
            x = maxX - increment
            y = maxY - increment
          self.incrementPoint(x, y)

  def incrementPoint(self, x, y):
    results = np.where((self.points[:,0] == x) & (self.points[:,1] ==y))
    if len(results[0]) == 1:
      valueNow = self.points[results[0]][0][2]
      valueNow += 1
      self.points[results[0]] = [x, y, valueNow]
    elif len(results[0]) == 0:
      self.points = np.vstack([self.points, [x, y, 1]])

def vents_part_one(vectors):
  vectors = vectors[np.where((vectors[:,0] == vectors[:,2]) | (vectors[:,1] == vectors[:,3]))]
  vectors = vectors[vectors[:,0].argsort()]
  matrix = Matrix()
  matrix.setVector(vectors)
  matrix.setPoints()
  result = np.where(matrix.points[:,2] > 1)
  return(len(result[0]))

def vents_part_two(vectors):
  vectors = vectors[vectors[:,0].argsort()]
  matrix2 = Matrix()
  matrix2.setVector(vectors)
  matrix2.setPoints()
  result = np.where(matrix2.points[:,2] > 1)
  return(len(result[0]))

vectors = []
npVectors = []
with open('input') as file:
  input =[
    line.strip() for line in file.readlines()
  ]
  file.close()
  for row in range(len(input)):
    start, finish = input[row].split(' -> ')
    start_x, start_y = start.split(',')
    finish_x, finish_y = finish.split(',')
    vectors.append([int(start_x), int(start_y), int(finish_x), int(finish_y)])
  npVectors = np.array((vectors))

print(
    f"""Day 5:
    first solution: {vents_part_one(npVectors)}
    second solution: {vents_part_two(npVectors)}"""
)
