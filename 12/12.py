def part_one(caves):
  paths = []
  paths.append([caves['start']['name']])
  finishedPaths = []
  newPaths = []
  while len(paths) > 0:
    if len(newPaths) > 0:
      paths = newPaths.copy()
    newPaths = []
    for i in range(len(paths)):
      for cc in caves[paths[i][-1]]['connected_to']:
        path = paths[i].copy()
        if caves[cc]['type'] != 'start':
          if caves[cc]['type'] == 'end':
            if path not in finishedPaths:
              endpath = path.copy()
              endpath.append(cc)
              finishedPaths.append(endpath)
          elif caves[cc]['type'] == 'big':
            path.append(cc)
          elif caves[cc]['type'] == 'small':
            if cc not in path:
              path.append(cc)
        if len(path) > len(paths[i]):
          newPaths.append(path)
    paths = newPaths.copy()
  return len(finishedPaths)

def part_two(caves):
  paths = []
  paths.append([caves['start']['name']])
  finishedPaths = []
  newPaths = []
  while len(paths) > 0:
    if len(newPaths) > 0:
      paths = newPaths.copy()
    newPaths = []
    for i in range(len(paths)):
      for cc in caves[paths[i][-1]]['connected_to']:
        path = paths[i].copy()
        if caves[cc]['type'] != 'start':
          if caves[cc]['type'] == 'end':
            if path not in finishedPaths:
              endpath = path.copy()
              endpath.append(cc)
              finishedPaths.append(endpath)
          elif caves[cc]['type'] == 'big':
            path.append(cc)
          elif caves[cc]['type'] == 'small':
            if cc not in path:
              path.append(cc)
            else:
              sds = []
              for s in path:
                if s.islower() and s != 'start' and s != 'end':
                  sds.append(s)
              duplicates = [p for p in sds if sds.count(p) > 1]
              if len(duplicates) == 0:
                path.append(cc)
        if len(path) > len(paths[i]):
          newPaths.append(path)
    paths = newPaths.copy()
  return len(finishedPaths)


lines = []
caves = {}
with open('input') as file:
  while (line := file.readline().rstrip()):
    lines.append(line)
for line in lines:
  for c in line.split('-'):
    if c not in caves:
      if c == 'start':
        cavetype = 'start'
      elif c == 'end':
        cavetype = 'end'
      elif c.isupper():
        cavetype = 'big'
      else:
        cavetype = 'small'
      caves[c] = {'name': c, 'type': cavetype, 'connected_to': []}
  fc, tc = line.split('-')
  if fc not in caves[tc]['connected_to']:
    caves[tc]['connected_to'].append(fc)
  if tc not in caves[fc]['connected_to']:
    caves[fc]['connected_to'].append(tc)

print(
    f"""Day 12:
    first solution: {part_one(caves.copy())}
    second solution: {part_two(caves.copy())}"""
)
