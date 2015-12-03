# You have a stack of n boxes, with widths w_i, heights h_i and depths d_i. The boxes cannot
# be rotated and can only be stacked on top of one another if each box in the stack is strictly
# larger than the box above it in width, height, and depth. Implement a method to build the tallest
# stack possible, where the height of a stack is the sum of the heights of each box.

from random import random
from math import floor
from pprint import pprint

def stack_of_boxes(boxes):
    boxes = sorted(boxes, key=lambda x: x['height'], reverse=True)
    max_height = 0
    max_heights = [ None for _ in range(len(boxes)) ]
    for i in range(len(boxes)):
        height = _stack_of_boxes(boxes, i, max_heights)
        max_height = max(height, max_height)
    return max_height

def _stack_of_boxes(boxes, i, max_heights):
    if max_heights[i] is not None:
        return max_heights[i]
    bottom = boxes[i]
    max_height = 0
    for j in range(i+1, len(boxes)):
        if meet_requirements(bottom, boxes[j]):
            height = _stack_of_boxes(boxes, j, max_heights)
            max_height = max(height, max_height)
    max_height += bottom['height']
    max_heights[i] = max_height
    return max_height

def meet_requirements(bottom, top):
    return bottom['height'] > top['height'] and \
           bottom['width']  > top['width'] and \
           bottom['depth']  > top['depth']

def create_box(h,w,d):
    return { 'height': h, 'width': w, 'depth': d }

if __name__ == "__main__":
    boxes = [ create_box(1+floor(200*random()),
                         1+floor(200*random()),
                         1+floor(200*random())
                        ) for _ in range(0,10) ]
    pprint(boxes)
    pprint(stack_of_boxes(boxes))    
