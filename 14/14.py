import numpy as np
from time import sleep

def splitToPairs(polymer_template):
  pairs = []
  for i in range(0, len(polymer_template) - 1):
    pairs.append(polymer_template[i:i+2])
  return pairs

def extendPolymer(pairs):
  extended = []
  for pair in pairs:
    if type(pair) != list:
      pair = list(pair)
    extendpair = np.where(npPairs[:,0] == ''.join(pair))
    extended.append(pair[0] + npPairs[extendpair[0]][0][1])
  extended.append(pair[1])
  return extended

def part_one(polymer_template):
  for i in range(15):
    pairs = splitToPairs(polymer_template)
    extended_polymer = extendPolymer(pairs)
    polymer_template = ''.join(extended_polymer)
  ordered_polymer = np.array(sorted(polymer_template))
  u, count = np.unique(ordered_polymer, return_counts=True)
  print(sum(count))
  print('u, count: ', u, ', ', count)
  return max(count) - min(count)

def extend(pair, count):
  extendpair = np.where(npPairs[:,0] == pair)
  newpair = pair[0] + npPairs[extendpair[0]][0][1]
  pair_endings.append(pair[1])
  extend(newpair, count - 1)

def part_two(polymer_template):
  untreated = []
  steps = 10
  #for i in range(len(polymer_template)):
  for i in range(1):
    pair = polymer_template[i:i+2]
    extend(pair, 40)
  return None


with open('input') as file:
  input = [
    line.strip() for line in file.readlines()
  ]
  file.close()
  polymer_template = input.pop(0)
  pair_insertion_rules = []
  for pair in input:
    pair, insertion_rules = pair.split(' -> ')
    pair_insertion_rules.append([pair, insertion_rules])
  npPairs = np.array(pair_insertion_rules)
  pair_endings = []

print(
    f"""Day 14:
    first solution: {part_one(polymer_template)}
    second solution: {part_two(polymer_template)}"""
)
