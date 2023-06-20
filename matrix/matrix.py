class Matrix:
    def __init__(self, matrix_string):
        self.m =  [[int(e) for e in r.split()] for r in matrix_string.split('\n')]

    def row(self, index):
        return self.m[index - 1]

    def column(self, index):
        return [r[index - 1] for r in self.m]
