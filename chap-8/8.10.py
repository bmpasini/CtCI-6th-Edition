# Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a
# new color, fill in the surrounding area until the color changes from the original color.

from pprint import pprint

def paint_fill(screen, p, new_color):
    if screen[p[0]][p[1]] == new_color:
        return None
    _paint_fill(screen, p, screen[p[0]][p[1]], new_color)

def _paint_fill(screen, p, old_color, new_color):
    if p[0] < 0 or p[0] >= len(screen)    or \
       p[1] < 0 or p[1] >= len(screen[0]) or \
       screen[p[0]][p[1]] != old_color:
        return None
    screen[p[0]][p[1]] = new_color
    # surrounding = [[p[0]-1, p[1]-1], [p[0]-1, p[1]], [p[0]-1, p[1]+1],
    #                [p[0]  , p[1]-1], [p[0]  , p[1]], [p[0]  , p[1]+1],
    #                [p[0]+1, p[1]-1], [p[0]+1, p[1]], [p[0]+1, p[1]+1]]
    surrounding = [(p[0]-1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1), (p[0]+1, p[1])]
    for next_p in surrounding:
        _paint_fill(screen, next_p, old_color, new_color)

if __name__ == "__main__":
    screen = [[1,1,1,1,1],
              [1,2,2,2,1],
              [1,2,3,2,1],
              [1,2,2,2,1],
              [1,1,1,1,1]]
    pprint(screen)
    paint_fill(screen, (2,2), 1)
    pprint(screen)
    paint_fill(screen, (2,2), 3)
    pprint(screen)
    paint_fill(screen, (0,0), 2)
    pprint(screen)
    paint_fill(screen, (2,2), 2)
    pprint(screen)
    paint_fill(screen, (0,0), 0)
    pprint(screen)