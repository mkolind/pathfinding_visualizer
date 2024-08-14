import pygame

from grid import *
from colors import *

def highlight_path(predecessors, start_block, end_block, screen):
    current = end_block
    path = []
    
    
    while current != start_block:
        path.append(current)
        current = predecessors[current]
    path.append(start_block) 
    for block in path:
        if block.is_start_or_end_node:
            continue
        block.change_color(LIGHT_BLUE, screen)
        block.draw(screen)
        pygame.display.update()
        pygame.time.delay(50)
        
def wall_to_remove(grid, current_block, new_block):
    x1, y1 = current_block.pos
    x2, y2 = new_block.pos
    
    wall_x = (x1 + x2) // 2
    wall_y = (y1 + y2) // 2
    
    return grid.blocks[wall_x][wall_y]

    

