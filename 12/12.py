import json
from time import sleep


def part_one(caves):
  return None
  paths = []
  paths.append([caves['start']['name']])
  finishedPaths = []
  deletePaths = []
  newPaths = []
  nb = 0
  while len(paths) > 0:
    print('number of finished paths: ', len(finishedPaths))
    duplicates = [path for path in finishedPaths if finishedPaths.count(path) > 1]
    print('duplicates in finishedPaths: ', len(duplicates))
    if len(paths) == 68:
      print('paths: ', paths)
    nb += 1
    # print('antall nye stier: ', len(newPaths))
    if len(newPaths) > 0:
      paths = newPaths.copy()
    newPaths = []
    duplicates = [path for path in paths if paths.count(path) > 1]
    print('duplicates in paths: ', len(duplicates))
    print('number of paths to check: ', len(paths))
    for i in range(len(paths)):
      for cc in caves[paths[i][-1]]['connected_to']:
        # print('cc', cc)
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
            # # print('har kommet til liten hule')
            if cc not in path:
              # # print('har ikke vært her før, så jeg legger til')
              path.append(cc)
        if path not in paths and path != paths[i]:
          newPaths.append(path)
          # print('newPaths: ', newPaths)
  return len(finishedPaths)

def part_two(caves):
  paths = []
  paths.append([caves['start']['name']])
  finishedPaths = []
  deletePaths = []
  newPaths = []
  nb = 0
  while len(paths) > 0:
    print('number of finished paths: ', len(finishedPaths))
    duplicates = [path for path in finishedPaths if finishedPaths.count(path) > 1]
    print('duplicates in finishedPaths: ', len(duplicates))
    if len(paths) == 68:
      print('paths: ', paths)
    nb += 1
    # print('antall nye stier: ', len(newPaths))
    if len(newPaths) > 0:
      paths = newPaths.copy()
    newPaths = []
    duplicates = [path for path in paths if paths.count(path) > 1]
    print('duplicates in paths: ', len(duplicates))
    print('number of paths to check: ', len(paths))
    for i in range(len(paths)):
      for cc in caves[paths[i][-1]]['connected_to']:
        # print('cc', cc)
        path = paths[i].copy()
        if caves[cc]['type'] != 'start':
          if caves[cc]['type'] == 'end':
            if path not in finishedPaths:
              endpath = path.copy()
              endpath.append(cc)
              finishedPaths.append(endpath)
          elif caves[cc]['type'] == 'big':
            #print('har kommet til stor hule')
            path.append(cc)
          elif caves[cc]['type'] == 'small':
            #print('har kommet til liten hule')
            if cc not in path:
              # # print('har ikke vært her før, så jeg legger til')
              path.append(cc)
            else:
              sds = []
              for s in path:
                #print('s i sti: ', s)
                if s.islower() and s != 'start' and s != 'end':
                  sds.append(s)
              #print('sjekker små: ', sds)
              duplicates = [p for p in sds if sds.count(p) > 1]
              if len(duplicates) == 0:
                path.append(cc)
        if path not in paths and path != paths[i]:
          newPaths.append(path)
          # print('newPaths: ', newPaths)
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
# print(json.dumps(caves, indent=2))



print(
    f"""Day 12:
    first solution: {part_one(caves.copy())}
    second solution: {part_two(caves.copy())}"""
 )
