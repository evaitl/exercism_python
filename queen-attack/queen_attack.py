class Queen:
    def _valid(row, column):
        if row < 0:
            raise ValueError("row not positive")
        if column < 0:
            raise ValueError("column not positive")
        if row >= 8:
            raise ValueError("row not on board")
        if column >= 8:
            raise ValueError("column not on board")
    
    def __init__(self, row, column):
        Queen._valid(row, column)
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        return any(
            (
                self.row == another_queen.row,
                self.column == another_queen.column,
                (self.row + self.column) == (another_queen.row + another_queen.column),
                (self.row - self.column) == (another_queen.row - another_queen.column),
            )
        )
