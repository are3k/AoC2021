import numpy as np
 
def part_one(input):
  found = 0
  for i in range(input[0].size):
    countChars = np.array([len(t) for t in input[:,i]])
    knownChars = np.where((countChars != 5) & (countChars != 6))
    found += knownChars[0].size
  return found

def findPositions(sa):
  segments = np.empty((7,1), dtype=str)
  sa_ = list(map(lambda sa: len(sa), sa))  # remark: py3 would work different here
  sa = sa[np.argsort(sa_)]
  sa = sa.astype('U')
  segments[0] = ''.join(set(sa[1]).difference(set(sa[0])))
  for letter in sa[9]:
    if sum(np.char.count(sa, sub = letter)) == 9:
      segments[5] = letter
    if sum(np.char.count(sa, sub = letter)) == 4:
      segments[4] = letter
    if sum(np.char.count(sa, sub = letter)) == 6:
      segments[1] = letter
    if sum(np.char.count(sa, sub = letter)) == 8:
      if letter != segments[0]:
        segments[2] = letter
    if sum(np.char.count(sa, sub = letter)) == 7:
      if len(''.join(set(sa[2]).intersection(letter))) == 1:
        segments[3] = letter
      else:
        segments[6] = letter
  return segments
  
def getNumberFromPositions(positions, value):
  if len(value) == 2:
    return 1
  if len(value) == 3:
    return 7
  if len(value) == 4:
    return 4
  if len(value) == 7:
    return 8
  if len(value) == 5:
    if len(set(value).intersection(positions[1])) == 1:
      return 5
    elif len(set(value).intersection(positions[4])) == 1:
      return 2
    else:
      return 3
  if len(value) == 6:
    if len(set(value).intersection(positions[3])) == 0:
      return 0
    elif len(set(value).intersection(positions[4])) == 1:
      return 6
    else:
      return 9


def part_two(signals, values):
  resultnumber = 0
  for i in range(signals[:,0].size):
    resultValue = []
    positions = findPositions(signals[i])
    for value in values[i]:
      resultValue.append(getNumberFromPositions(positions, value))
    resultnumber += int(''.join(map(str, resultValue)))
  return resultnumber

signalList = np.empty((200,10), dtype=object)
outputValues =  np.empty((200,4), dtype=object)
with open('input') as file:
  input = [
    line.strip() for line in file.readlines()
  ]
  file.close()
  for i in range(len(input)):
    patterns, ovs = input[i].split(' | ')
    signalList[i] = np.array([patterns.split(' ')])
    outputValues[i] = np.array([ovs.split(' ')]) 

print(
    f"""Day 8:
    first solution: {part_one(outputValues)}
    second solution: {part_two(signalList, outputValues)}"""
 )
