class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)     # rows[i] = set of numbers in row i
        cols = defaultdict(set)     # cols[i] = set of numbers in col i
        boxes = defaultdict(set)    # boxes[(r,c)] = set of numbers in that box

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":      # skip empty cells
                    continue
                
                # check if already seen in this row, col, or box
                if val in rows[r] or val in cols[c] or val in boxes[(r//3, c//3)]:
                    return False
                
                # add to all three hashsets
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r//3, c//3)].add(val)
        
        return True