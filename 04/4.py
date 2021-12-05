def fillIn(bingoNumber, boards):
  for board in boards:
    for row in range(5):
      for value in range(5):
        if boards[board]['rows'][str(row)][str(value)]['num'] == int(bingoNumber):
          boards[board]['rows'][str(row)][str(value)]['selected'] = True
    for col in range(5):
      for value in range(5):
        if boards[board]['cols'][str(col)][str(value)]['num'] == int(bingoNumber):
          boards[board]['cols'][str(col)][str(value)]['selected'] = True
  return boards

def checkBoardForBingo(board):
  bingo = 0
  for row in range(5):
    for value in range(5):
      if board['rows'][str(row)][str(value)]['selected']:
        bingo += 1
      else:
        bingo = 0
        break
    if (bingo == 5):
      return True
  bingo = 0
  for col in range(5):
    for value in range(5):
      if board['cols'][str(col)][str(value)]['selected']:
        bingo += 1
      else:
        bingo = 0
        break
    if (bingo == 5):
      return True
  return False

def checkForBingo(boards):
  bingo = 0
  for board in boards:
    for row in range(5):
      for value in range(5):
        if boards[board]['rows'][str(row)][str(value)]['selected']:
          bingo += 1
        else:
          bingo = 0
          break
      if (bingo == 5):
        return board
    for col in range(5):
      for value in range(5):
        if boards[board]['cols'][str(col)][str(value)]['selected']:
          bingo += 1
        else:
          bingo = 0
          break
      if (bingo == 5):
        return board
  return 1000

def findSumOfUnselected(boardNum, boards):
  mySum = 0
  for row in range(5):
    for value in range(5):
      if not boards[boardNum]['rows'][str(row)][str(value)]['selected']:
        mySum += boards[boardNum]['rows'][str(row)][str(value)]['num']
  return mySum

def bingo_part_one(bingoDraws, boards):
  for i in bingoDraws[0:5]:
    boards = fillIn(i, boards)
  bingo = checkForBingo(boards)
  if int(bingo) < 1000:
      sumOfUnselected = findSumOfUnselected(bingo, boards)
      return str(sumOfUnselected * int(i))
  for i in bingoDraws[5:]:
    boards = fillIn(i, boards)
    bingo = checkForBingo(boards)
    if int(bingo) < 1000:
      sumOfUnselected = findSumOfUnselected(bingo, boards)
      return str(sumOfUnselected * int(i))

def countBoardsWithoutBingo(boardsWithBingo):
  boardsWithoutBingo = 0
  for board in boardsWithBingo:
    if not boardsWithBingo[str(board)]:
      boardsWithoutBingo += 1
  return boardsWithoutBingo

def findLastBoard(ingoDraws, boards):
  lastBoard = 0
  boardsWithBingo = {}
  for i in boards:
    boardsWithBingo[str(i)] = False
  for i in bingoDraws:
    boards = fillIn(i, boards)
    for board in boards:
      if not boardsWithBingo[str(board)]:
        if checkBoardForBingo(boards[board]):
          boardsWithBingo[str(board)] = True
        if countBoardsWithoutBingo(boardsWithBingo) == 1:
          for j in boardsWithBingo:
            if not boardsWithBingo[str(j)]:
              return j

def bingo_part_two(bingoDraws, boards):
  lastBoard = findLastBoard(bingoDraws, boards)
  for i in bingoDraws:
    boards = fillIn(i, boards)
    if checkBoardForBingo(boards[str(lastBoard)]):
      break
  sumOfUnselected = findSumOfUnselected(lastBoard, boards)
  return str(sumOfUnselected * int(i))
              


def createCols(rows):
  col = {}
  cols = {}
  values = {}
  for i in range(5):
    values = {}
    for j in range(5):
      values[str(j)] = rows[str(j)][str(i)]
    cols[str(i)] = values
  return cols

boardCount = 0
boards = {}
row = {}
rows = {}

with open('input') as file:
  for i, line in enumerate(file):
    if i == 0:
      bingoDraws = line.rstrip().split(',')
    elif len(line.rstrip()) == 0 :
      rowCount = 0
      if i > 2:
        boardCount += 1
    else:
      row ={}
      lineValues = line.rstrip().split()
      for valueCount in range(len(lineValues)):
        row[str(valueCount)] = {'num': int(lineValues[valueCount]), 'selected': False}
      rows[str(rowCount)] = row
      rowCount += 1
      if rowCount > 4:
        cols = createCols(rows)
        boards[str(boardCount)] = {'rows': rows, 'cols': cols}
        rows = {}
        

print(
    f"""Day 4:
    first solution: {bingo_part_one(bingoDraws, boards)}
    second solution: {bingo_part_two(bingoDraws, boards)}"""
)
