import math
import Spot
from queue import PriorityQueue
import pygame


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((abs(x1 - x2)**2) + (abs(y1 - y2)**2))


def reconstruct_path(came_from, current, draw):
    path = []
    while current['id'] in came_from:
        current = came_from[current['id']]
        if(not(Spot.is_start(current))):
            current = Spot.make_path(current)
            path.append(Spot.get_pos(current))
            draw()
        else:
            print("is_start")
    return path


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot['id']: float("inf") for row in grid for spot in row}
    g_score[start['id']] = 0

    f_score = {spot['id']: float("inf") for row in grid for spot in row}
    f_score[start['id']] = h(Spot.get_pos(start), Spot.get_pos(end))

    open_set_hash = [start]

    while not(open_set.empty()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if (current == end):
            path = reconstruct_path(came_from, current, lambda: draw)
            end = Spot.make_end(end)
            return path

        current = Spot.update_neighbors(current, grid)

        for neighbor in current['neighbors']:
            temp_g_score = g_score[current['id']] + 1

            if(temp_g_score < g_score[neighbor['id']]):
                came_from[neighbor['id']] = current
                g_score[neighbor['id']] = temp_g_score
                f_score[neighbor['id']] = temp_g_score + \
                    h(Spot.get_pos(neighbor), Spot.get_pos(end))

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put(
                        (f_score[neighbor['id']], count, neighbor))
                    open_set_hash.append(neighbor)
                    neighbor = Spot.make_open(neighbor)
        if current != start:
            current = Spot.make_closed(current)
        draw()
    return False
