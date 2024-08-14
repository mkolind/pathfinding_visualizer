import pygame
import random

from colors import*

class Block:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x*size, y*size, size, size)
        self.pos = [x,y]
        self.color = WHITE
        self.is_wall = False
        self.is_start_or_end_node = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 1)
    
    def change_color(self, color, screen):
        self.color = color
        self.draw(screen)
        
    def click(self, screen):
        if not self.is_start_or_end_node:
            if self.is_wall:
                self.change_color(WHITE, screen)
            else: 
                self.change_color(BLACK, screen)
            self.is_wall = not self.is_wall

        

class Grid:
    def __init__(self, block_width, block_height, block_size, screen):
        self.block_size = block_size
        self.resolution = (block_width, block_height)
        self.screen = screen
        self.blocks = self.make_blocks()
        self.start_node = self.set_node("start")
        self.end_node = self.set_node("end")
        
    def is_clicked(self, pos):
        x, y = pos
        if 0 <= x < self.block_size * self.resolution[0] and 0 <= y < self.block_size * self.resolution[1]:
            return True
        return False

    def draw(self):
        for block_row in self.blocks:
            for block in block_row:
                block.draw(self.screen)

    def make_blocks(self):
        blocks = []
        width = self.resolution[0]
        height = self.resolution[1]
        
        for x in range(0, width):
            block_row = []
            for y in range(0, height):
                block_row.append(Block(x, y, self.block_size))   
                
            blocks.append(block_row)             
        return blocks
    
    def handle_click(self, pos, screen):
        x = pos[0] // self.block_size
        y = pos[1] // self.block_size
        
        self.blocks[x][y].click(screen)            
    
    def set_node(self, node_desc):
        color = GREEN if node_desc == "start" else RED
        
        # Makes sure that start and end lands "inside" the grid
        x = 2 * random.randint(0, (self.resolution[0] - 1) // 2) + 1
        y = random.randint(0, (self.resolution[1] // 2) - 1) * 2   
        
        self.blocks[x][y].is_start_or_end_node = True
        self.blocks[x][y].change_color(color, self.screen)
        return self.blocks[x][y]
    
    def get_neighbours(self, block: Block):
        neighbours = []
        x = block.pos[0]
        y = block.pos[1]
        
        if x != 0 and not self.blocks[x-1][y].is_wall:
            neighbours.append(self.blocks[x-1][y])
        if x != self.resolution[0] - 1 and not self.blocks[x+1][y].is_wall:
            neighbours.append(self.blocks[x+1][y])
        if y != 0 and not self.blocks[x][y-1].is_wall:
            neighbours.append(self.blocks[x][y-1])
        if y != self.resolution[1] - 1 and not self.blocks[x][y+1].is_wall:
            neighbours.append(self.blocks[x][y+1])
        
        return neighbours
                       