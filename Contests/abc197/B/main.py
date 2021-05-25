#!/usr/bin/env python3
import sys


def search(_map, H, W, x, y, dx, dy):
    if x+dx < 0 or y+dy < 0 or x+dx == H or y+dy == W:
        return 0
    elif _map[x+dx][y+dy] == '#':
        return 0
    else:
        return search(_map, H, W, x+dx, y+dy, dx, dy) + 1


def solve(_map, H, W, X, Y):

    x = X-1
    y = Y-1

    count = 1

    count += search(_map, H, W, x, y, -1, 0)
    count += search(_map, H, W, x, y, 1, 0)
    count += search(_map, H, W, x, y, 0, -1)
    count += search(_map, H, W, x, y, 0, 1)

    print(count)


def main():
    input = sys.stdin.readline

    H, W, X, Y = map(int, input().split())
    _map = []
    for h in range(H):
        _map.append(input())

    solve(_map, H, W, X, Y)

    return


if __name__ == '__main__':
    main()
