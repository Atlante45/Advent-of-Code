from collections import defaultdict
from queue import PriorityQueue
import numpy as np


def p(*args):
    return np.array(args)


def v(*args):
    return np.array(args)


def gen_primes():
    """Generate an infinite sequence of prime numbers."""
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def binary_search(f, low, high):
    while low < high:
        mid = (low + high) // 2
        if f(mid):
            high = mid
        else:
            low = mid + 1
    return low


def neighbors4(i, j, max_i, max_j=None):
    if isinstance(max_i, list):
        max_j = len(max_i[0])
        max_i = len(max_i)

    if not max_j:
        max_j = max_i

    cells = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ]

    return [(x, y) for (x, y) in cells if x >= 0 and x < max_i and y >= 0 and y < max_j]


def neighbors8(i, j, max_i, max_j=None):
    if isinstance(max_i, list) or isinstance(max_i, tuple):
        max_j = len(max_i[0])
        max_i = len(max_i)

    if not max_j:
        max_j = max_i

    cells = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 1),
    ]

    return [(x, y) for (x, y) in cells if x >= 0 and x < max_i and y >= 0 and y < max_j]


def neighbors6(i, j, k, max_i, max_j=None, max_k=None, min=0):
    if (
        isinstance(max_i, list)
        and isinstance(max_i[0], list)
        and isinstance(max_i[0][0], list)
    ):
        max_i = len(max_i)
        max_j = len(max_i[0])
        max_k = len(max_i[0][0])

    if not max_j:
        max_j = max_i
    if not max_k:
        max_k = max_i

    cells = [
        (i - 1, j, k),
        (i + 1, j, k),
        (i, j - 1, k),
        (i, j + 1, k),
        (i, j, k - 1),
        (i, j, k + 1),
    ]

    return [
        (x, y, z)
        for (x, y, z) in cells
        if x >= -10 and x < max_i and y >= -10 and y < max_j and z >= -10 and z < max_k
    ]


def dijkstra(starts, neighbors, cost=None):
    if not isinstance(starts, list):
        starts = [starts]
    if cost is None:
        cost = lambda c, n: 1

    frontier = PriorityQueue()
    came_from = {}
    cost_so_far = {}

    for start in starts:
        frontier.put(start, 0)
        came_from[start] = None
        cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = current

    return came_from, cost_so_far


# Keeps track of all shortest paths
def dijkstra_full(starts, neighbors, cost=None):
    if not isinstance(starts, list):
        starts = [starts]
    if cost is None:
        cost = lambda c, n: 1

    frontier = PriorityQueue()
    came_from = defaultdict(list)
    cost_so_far = {}

    for start in starts:
        frontier.put(start, 0)
        cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = [current]
            if next in cost_so_far and new_cost == cost_so_far[next]:
                came_from[next].append(current)
    return came_from, cost_so_far


def a_star(starts, goal, neighbors, cost=None, heuristic=None):
    if not isinstance(starts, list):
        starts = [starts]
    if heuristic is None:
        heuristic = lambda a, b: sum(abs(x - y) for x, y in zip(a, b))
    if cost is None:
        cost = lambda c, n: 1

    frontier = PriorityQueue()
    came_from = {}
    cost_so_far = {}

    for start in starts:
        frontier.put(start, 0)
        came_from[start] = None
        cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far
