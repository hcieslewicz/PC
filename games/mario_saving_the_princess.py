import collections
from utilities.utilities import boolen_to_binary


class MarioSavingThePrincess:
    def __init__(self, size, grid):
        self.height = size
        self.width = size
        self.grid = grid
        self.mario = "m"
        self.princess = "p"
        self.obstacle = "x"
        self.freeCell = "-"
        self.validGridValues = [self.mario, self.princess,  self.obstacle, self.freeCell]

    def validate_grid(self):
        m = None    # mario position
        p = None    # princess position

        print(self.height)
        print(self.width)
        print(self.grid)

        for i in range(0, self.height):
            for j in range(0, self.width):
                print(i, j)
                if self.grid[i][j] == self.mario:
                    m = (i, j)
                elif self.grid[i][j] == self.princess:
                    p = (i, j)
                elif self.grid[i][j] in self.validGridValues:
                    pass
                else:
                    return False, m
        if not m or not p:
            return False, m

        return True, m

    @staticmethod
    def convert_to_direction(paths):
        converted_path = []
        for path in paths:
            x, y = path[0]
            tmp = []
            for coordinate in path[1:]:
                x2, y2 = coordinate
                if x - x2 > 0:
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
            converted_path.append(tuple(tmp))
        return converted_path

    def bfs(self, start):
        queue = collections.deque([[start]])

        found_in_leyer = None
        paths = []
        dimension = self.height * self.width

        while queue:
            path = queue.popleft()
            if (found_in_leyer and (len(path)) > found_in_leyer) or len(path) > dimension:
                continue

            x, y = path[-1]
            if self.grid[x][y] == self.princess:
                paths.append(path)

                if not found_in_leyer:
                    found_in_leyer = len(path)

            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= x2 < self.width and 0 <= y2 < self.height and self.grid[x2][y2] != self.obstacle \
                        and (x2, y2) not in path:
                    queue.append(path + [(x2, y2)])

        return paths

    def play(self):

        is_grid_valid, mario_position = self.validate_grid()

        paths = []
        if is_grid_valid:
            paths = self.bfs(mario_position)
            print(len(paths), paths)

        error_flag = boolen_to_binary(is_grid_valid)
        converted_path = self.convert_to_direction(paths)

        return error_flag, converted_path


if __name__ == "__main__":
    mariogame = MarioSavingThePrincess(3, ["--m", "-x-", "p--"])
    result = mariogame.play()
    print(result)
