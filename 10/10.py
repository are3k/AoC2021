import numpy as np

def part_one(navigation):
  ends =  [')',']','}','>']
  legalPairs = ['()', '[]','{}','<>']
  syntaxErrorScore = 0
  for i in range(10):
    for pair in legalPairs:
      navigation = np.char.replace(navigation, pair, '')
  for nav in navigation:
    errorPosition = 100
    for end in ends:
      if np.char.find(nav, end) > 0 and np.char.find(nav, end) < errorPosition:
        errorPosition = np.char.find(nav, end)
        illegalChar = end
    if (errorPosition != 100):
      if (illegalChar) == ')':
        syntaxErrorScore += 3
      if (illegalChar) == ']':
        syntaxErrorScore += 57
      if (illegalChar) == '}':
        syntaxErrorScore += 1197
      if (illegalChar) == '>':
        syntaxErrorScore += 25137
  return syntaxErrorScore

def part_two(navigation):
  ends =  [')',']','}','>']
  legalPairs = ['()', '[]','{}','<>']
  needsCompletion = []
  completionScore = []
  for i in range(50):
    for pair in legalPairs:
      navigation = np.char.replace(navigation, pair, '')
  for nav in navigation:
    errorPosition = 100
    for end in ends:
      if np.char.find(nav, end) > 0 and np.char.find(nav, end) < errorPosition:
        errorPosition = np.char.find(nav, end)
    if (errorPosition == 100):
      needsCompletion.append(nav)
  for il in needsCompletion:
    score = 0
    il = il [::-1]
    for i in il:
      score = score * 5
      if i == '(':
        score += 1
      if i == '[':
        score += 2
      if i == '{':
        score +=3
      if i == '<':
        score += 4
    completionScore.append(score)
  completionScore.sort()
  middle = len(completionScore)//2
  return completionScore[middle]


with open('input') as file:
  input = [
    line.strip() for line in file.readlines()
  ]
  file.close()
  navigation = np.array(input)

print(
    f"""Day 10:
    first solution: {part_one(navigation)}
    second solution: {part_two(navigation)}"""
 )
