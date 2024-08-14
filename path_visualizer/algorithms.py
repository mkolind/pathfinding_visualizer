import pygame
import queue

from grid import *
from colors import *
from utils import *

def bfs(grid: Grid, screen):
    path_found = False
    q = queue.Queue()
    visited = set([])
    predecessors = {}

    root = grid.start_node
    end_node = grid.end_node
    
    q.put(root)
    visited.add(root)

    
    while q.qsize() > 0:
        v: Block = q.get()
        delay_size = int(100 / (1  + q.qsize()))
        delay_time = delay_size
        
        if v == end_node:
            path_found = True
            break
        
        if v != root:
            visited.add(v)
            v.change_color(BLUE, screen)
            v.draw(screen)
            pygame.display.update()
            pygame.time.delay(delay_time)
        
        
        for neighbour in grid.get_neighbours(v):
            if neighbour not in visited:
                visited.add(neighbour)
                q.put(neighbour)
                predecessors[neighbour] = v
    
    if path_found:
        highlight_path(predecessors, grid.start_node, grid.end_node, screen)

#def dijkstra(grid, screen):      
                    

def random_walls(grid: Grid, screen):
    width = grid.resolution[0]
    height = grid.resolution[1]
    
    row = 0
    while row < width:
        col = 0
        while col < height:
            block = grid.blocks[row][col]
            if not block.is_wall:
                block.click(screen)
                block.draw(screen)
                pygame.display.update()
                pygame.time.delay(12)
            
            step_y = random.randint(1,4)
            col += step_y
        
        step_x = random.randint(1,3)
        row += step_x
   
#TODO: maze doesn't work     
def maze(grid: Grid, screen):
    width = grid.resolution[0]
    height = grid.resolution[1]
    
    stack = []
    visited = set()
    
    # Creates a grid like structure within the grid to build the maze from 
    for y in range(height):
        for x in range(width):
            block = grid.blocks[x][y]
            if (y-1)*x % 2 == 0:
                block.click(screen)
                                           
    current_block = grid.start_node
    stack.append(current_block)
    visited.add(current_block)
    
    while stack:
        current_block = stack.pop()
        x = current_block.pos[0]
        y = current_block.pos[1]

            # Calculate new positions
        new_positions = [
            (x, max(0, y - 2)),  # Two blocks above
            (x, min(height - 1, y + 2)),  # Two blocks below
            (max(0, x - 2), y),  # Two blocks left
            (min(width - 1, x + 2), y)  # Two blocks right
            ]
        
        random.shuffle(new_positions)
        
        new_blocks = []

        
        for move in new_positions:        
            new_block = grid.blocks[move[0]][move[1]]
            
            if new_block not in visited:
                new_blocks.append(new_block)
                
        for block in new_blocks:
            wall = wall_to_remove(grid, current_block, new_block)
            if wall not in visited and wall.is_wall:
                wall.click(screen)
                visited.add(wall)
            visited.add(new_block)
            stack.append(current_block)
            stack.append(new_block)
             
            

         

        
        

    
    
    
    
                    
    
            
            
        
        
            
        
    
            
        
        
        
        
            
            
    
    
        
        
        
        
    
    
    