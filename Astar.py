import math
from queue import PriorityQueue
import pygame


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((abs(x1 - x2)**2) + (abs(y1 - y2)**2))


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        if(not(current.is_start())):
            current.make_path()
            draw()


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not(open_set.empty()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if (current == end):
            reconstruct_path(came_from, current, lambda: draw)
            end.make_end()
            return came_from

        current.update_neighbors(grid)

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if(temp_g_score < g_score[neighbor]):
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                    h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        if current != start:
            current.make_closed()
        draw()
    return False
