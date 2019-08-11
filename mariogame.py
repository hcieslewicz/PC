import collections


class marioSavingThePrincess():

    def __init__(self, size, grid):
        self.height = size
        self.width = size
        self.grid = grid
        self.princess = "p"
        self.mario = "m"
        self.obstacle = "x"
        self.freeCell = "-"
        self.validGridValues = ['m', 'p', '-', 'x']

    def validateGrid(self):
        m = None # mario position
        p = None # princess position

        for i in range(0, self.height):
            for j in range(0, self.width):

                if self.grid[i][j] == self.mario:
                    m = (i,j)
                elif self.grid[i][j] == self.princess:
                    p = (i, j)
                elif self.grid[i][j] in self.validGridValues:
                    pass
                else:
                    return False, m
        if not m or not p:
            return False,m

        return True, m

    def convertToDirection(self, paths):
        convertedPath = []
        for path in paths:
            x ,y = path[0]
            tmp = []
            for coordinate in path[1:]:
                x2, y2 = coordinate
                if x - x2 >0:
                    tmp.append("UP")
                    x = x2
                elif x - x2 < 0:
                    tmp.append("DOWN")
                    x = x2
                elif y - y2 > 0:
                    tmp.append("LEFT")
                    y = y2
                elif y - y2 < 0:
                    tmp.append("RIGHT")
                    y = y2
            convertedPath.append(tuple(tmp))
        return convertedPath

    def bfs(self, start):
        queue = collections.deque([[start]])

        foundInLeyer = None
        paths = []
        dimension = self.height * self.width

        while queue:
            path = queue.popleft()
            if (foundInLeyer and (len(path)) > foundInLeyer) or len(path)> dimension:
                continue

            x, y = path[-1]
            if self.grid[x][y] == self.princess:
                paths.append(path)

                if not foundInLeyer:
                    foundInLeyer = len(path)

            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= x2 < self.width and 0 <= y2 < self.height and self.grid[x2][y2] != self.obstacle and (x2, y2) not in path:
                    queue.append(path + [(x2, y2)])

        return paths

    def getErrorFlag(self, isGridValid):
        if isGridValid:
            return '0b0'
        else:
            return '0b1'

    def play(self):

        isGridValid, marioPosition = self.validateGrid()

        paths = []
        if isGridValid:
            paths = self.bfs(marioPosition)
            print(len(paths), paths)

        errorFlag = self.getErrorFlag(isGridValid)
        convertedPath = self.convertToDirection(paths)

        return errorFlag, convertedPath


if __name__ == "__main__":
    mariogame = marioSavingThePrincess(3, grid = ["--m", "-x-", "p--"])
    result = mariogame.play()
    print(result)
