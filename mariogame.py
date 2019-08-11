import collections

def bfs(start):
    queue = collections.deque([[start]])


    foundInLeyer = None
    paths = []
    dimension = height * width
    seen = set([start])
    while queue:
        path = queue.popleft()

        if (foundInLeyer and (len(path)) > foundInLeyer) or len(path) > dimension:
            continue

        x, y = path[-1]
        if grid[x][y] == "p":
            paths.append(path)

            print("FOUND!!!!!!!!!!!!!!!!!!!")
            if not foundInLeyer:
                foundInLeyer = len(path)

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):


            if 0 <= x2 < width and 0 <= y2 < height and grid[x2][y2] != "x" and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


    print(paths)
    return paths

if __name__ == "__main__":
    size = 3
    width = size
    height = size
    grid = ["--m", "-x-", "p--"]
    start = (0,2)

    print("paths: {}".format(bfs(start)))
