from pprint import PrettyPrinter

def solve(sudoku):
    empty=find_empty(sudoku)

    if not empty:
        return True
    else:
       row, column = empty

    for i in range(1,10):
          if valid(sudoku,i,(row,column)):
              sudoku[row][column] = i

              if solve(sudoku):
                 return True

              sudoku[row][column] = 0

    return False




def valid(sudoku,num,pos):
    for i in range(9):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    box0 = pos[0] // 3
    box1 = pos[1] // 3


    for i in  range(box0*3,box0*3+3):
        for j in range(box1*3,box1*3+3):
            if sudoku[i][j] == num  and pos != (i,j):
                return False

    return True

def find_empty(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                return (i,j)

    return None


sudoku = [[3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]]

if solve(sudoku):
    p=PrettyPrinter(indent=4)
    p.pprint(sudoku)
else:
    print("Nothing")