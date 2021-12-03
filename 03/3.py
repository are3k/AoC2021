import numpy as np
from math import ceil

def diagnostics_part_one(diagnostics):
  gamma = np.count_nonzero(diagnostics == 1, axis=0)
  epsilon = np.copy(gamma)
  gamma[gamma < 500] = 0
  gamma[gamma > 500] = 1
  epsilon[epsilon < 500] = 1
  epsilon[epsilon > 500] = 0
  gamma = "".join(map(str, gamma))
  epsilon = "".join(map(str, epsilon))
  return int(gamma, 2) * int(epsilon, 2)

def reduce_arrays(diagnostics, column, searchValue):
  diagnostics=diagnostics[diagnostics[:,column]==searchValue]
  return diagnostics

def diagnostics_part_two(diagnostics):
  co2 = np.copy(diagnostics)
  for i in range(0,12):
    rows, columns = co2.shape
    if rows == 1:
      break
    countOnes = np.count_nonzero(co2 == 1, axis=0)
    if countOnes[i] < ceil(rows / 2): 
      searchValue = 1
    else:
      searchValue = 0
    co2 = reduce_arrays(co2, i, searchValue)
  co2Lst = co2[0].tolist()
  co2StrLst = [int(co2Lst) for co2Lst in co2Lst]
  epsilon = "".join(map(str, co2StrLst))

  oxygen = np.copy(diagnostics)
  for i in range(0,12):
    rows, columns = oxygen.shape
    if rows == 1:
      break
    countOnes = np.count_nonzero(oxygen == 1, axis=0)
    if countOnes[i] >= ceil(rows / 2): 
      searchValue = 1
    else:
      searchValue = 0
    oxygen = reduce_arrays(oxygen, i, searchValue)
  oxygenLst = oxygen[0].tolist()
  oxygenStrLst = ([int(oxygenLst) for oxygenLst in oxygenLst])
  gamma = "".join(map(str, oxygenStrLst))
  return int(epsilon, 2) * int(gamma, 2)
  
diagnostics = np.empty((1000, 12))
linjeteller = 0

with open('input') as file:
  while (line := file.readline().rstrip()):
    diagnostics[linjeteller] = np.array([int(i) for i in list(line)])
    linjeteller += 1
  
  
print(
    f"""Day 3:
    first solution: {diagnostics_part_one(diagnostics)}
    second solution: {diagnostics_part_two(diagnostics)}"""
)
