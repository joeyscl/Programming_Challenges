def printBoard(board):
        print('')
        for i in range(9):
            print(board[i])

def solve(board):

    def insert(i, j, num):
        board[i][j] = num


    def remove(i, j):
        board[i][j] = 0


    def boardValid(i, j):
        
        def rowValid(r, c):
            nums = set()
            for c in range(9):
                num = board[r][c]
                if num == 0:
                    continue
                elif num not in nums:
                    nums.add(num)
                else:
                    return False
            return True

        def colValid(r, c):
            nums = set()
            for r in range(9):
                num = board[r][c]
                if num == 0:
                    continue
                elif num not in nums:
                    nums.add(num)
                else:
                    return False
            return True


        def quadValid(r, c):
            topLeft = [0, 0]

            topLeft[0] = (r // 3) * 3
            topLeft[1] = (c // 3) * 3

            nums = set()

            for i in range(topLeft[0], topLeft[0] + 3):
                for j in range(topLeft[1], topLeft[1] + 3):
                    num = board[i][j]
                    if num == 0:
                        continue
                    elif num not in nums:
                        nums.add(num)
                    else:
                        return False
            return True

        return colValid(i, j) and rowValid(i, j) and quadValid(i, j)


    def parseBoard(): #get the fixed cells
        fixed = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != 0:
                    fixed.add((r,c))

        return fixed


    # solver
    fixed = parseBoard()

    i, j = 0, 0
    numToInsert = 1

    while i < 9:
        if (i,j) not in fixed:
            insert(i,j, numToInsert)

        if boardValid(i, j):
            numToInsert = 1
            j += 1
            if j >= 9:
                j = 0
                i += 1
        else:
            numToInsert += 1
            if numToInsert <= 9:
                pass
            else:
                while numToInsert > 9 or (i,j) in fixed:
                    if (i,j) not in fixed:
                        remove(i, j)
                    j -= 1
                    if j < 0:
                        j = 8
                        i -= 1

                    numToInsert = board[i][j] + 1


board0 = [\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\

[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\

[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0],\
[0,0,0,0,0,0,0,0,0]\
]

# easy
board1 = [\
[0,2,7,9,1,0,5,0,0],\
[3,0,0,0,6,0,0,0,0],\
[1,9,0,4,0,0,7,6,0],\

[5,1,0,8,0,0,0,0,0],\
[8,7,4,0,0,0,1,2,6],\
[0,0,0,0,0,7,0,5,9],\

[0,3,1,0,0,8,0,9,5],\
[0,0,0,0,9,0,0,0,4],\
[0,0,6,0,3,4,2,7,0]\
]

# "evil"
board2 = [\
[0,5,0,1,0,0,9,0,0],\
[0,0,0,0,4,0,0,0,2],\
[0,0,7,0,6,5,0,0,0],\

[0,9,5,0,0,0,0,4,0],\
[0,7,6,0,0,0,8,1,0],\
[0,3,0,0,0,0,2,5,0],\

[0,0,0,5,3,0,6,0,0],\
[9,0,0,0,8,0,0,0,0],\
[0,0,2,0,0,4,0,8,0]\
]

solve(board2)
printBoard(board2)




