"""Suppose you have a grid of n x m cells, where each cell is either empty or contains a
rock. You're given a starting position in the grid (x,y), and you want to reach a target
position (tx,ty), but you can only move in four directions (up, down, left, right) and you
can only move through empty cells.You're also given a limited number of moves k
that you can make. Write a program to determine if it's possible to reach the target
position from the starting position within k moves."""
from collections import deque


def is_reachable(grid, start, target, k):
    n, m = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # (x, y, moves)

    while queue:
        x, y, moves = queue.popleft()
        if (x, y) == target and moves <= k:
            return True

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))

    return False


if __name__ == '__main__':
    # n = 3, m = 3
    _grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    _start = (0, 0)
    _target = (2, 2)
    _k = 6
    print(is_reachable(_grid, _start, _target, _k))
