class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box={}

        for i in range(len(board)):
            for j in range(len(board[i])):
                curr= board[i][j]
                if curr != ".":
                    if curr not in box:
                        box[curr]=[]
                        box[curr].append((i,j))
                        print("ap1",box[curr])
                    else:
                        for rows,cols in box[curr]:
                            print(box[curr])
                            if rows == i:
                                print(i,j,curr,rows,cols,"row")
                                return False
                            if cols == j:
                                print(i,j,curr,"col")
                                return False
                            square = (rows//3,cols//3)
                            if square==(i//3,j//3):
                                print(i//3,j//3,curr,"square")
                                return False
                        box[curr].append((i,j))
                        print("ap2",box[curr])
        return True


        