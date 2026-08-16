class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkLine(board: List[str]) -> bool:
            seen = []
            for s in board:
                if s == ".":
                    continue
                if s in seen:
                    return False
                seen.append(s)
            return True
        # check rows
        for row in board:
            if not checkLine(row):
                return False

        # check cols
        for i in range(9):
            line = []
            for r in range(9):
                line.append(board[r][i])
            if not checkLine(line):
                return False

        # check boxes
        boxes = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                box = (r//3)*3 + c//3
                boxes[box].append(board[r][c])
        for b in boxes:
            if not checkLine(b):
                return False

        return True