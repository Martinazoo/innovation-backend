import heapq
import math


class AStar:

    DIRECTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def heuristic(self, a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])

    def in_bounds(self, node):
        x, y = node
        return 0 <= x < self.width and 0 <= y < self.height

    def walkable(self, node):
        x, y = node
        return self.grid[y][x]

    def neighbors(self, node):
        x, y = node

        for dx, dy in self.DIRECTIONS:
            nx = x + dx
            ny = y + dy

            neighbor = (nx, ny)

            if self.in_bounds(neighbor) and self.walkable(neighbor):
                yield neighbor

    def cost(self, a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])

        if dx == 1 and dy == 1:
            return math.sqrt(2)

        return 1

    def find_path(self, start, goal):

        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}

        g_score = {start: 0}

        while open_set:

            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):

                tentative_g = g_score[current] + self.cost(current, neighbor)

                if neighbor not in g_score or tentative_g < g_score[neighbor]:

                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g

                    f = tentative_g + self.heuristic(neighbor, goal)

                    heapq.heappush(open_set, (f, neighbor))

        return []

    def reconstruct_path(self, came_from, current):

        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        path.reverse()

        return path