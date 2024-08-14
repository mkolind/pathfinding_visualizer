import pygame 

from algorithms import * 
from utils import *

def start_action(grid, screen):
    route = bfs(grid, screen)
    highlight_path(route, grid.start_node, grid.end_node, screen)
    
def restart_action(grid, screen):
    for row in grid.blocks:
        for block in row:
            block.color = WHITE
            block.is_wall = False
    
    grid.start_node.color = GREEN
    grid.end_node.color = RED
    
def algorithm_button(grid, screen):
    print("This is on the todo list")


class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buttons = []
        
    def add_button(self, name, text, pos, width, height, color):
        self.buttons.append(Button(name, text, pos, width, height, color))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.is_clicked(event):
                    print(f"{button.name} was clicked")
        
class Button:
    def __init__(self, text, pos, width, height, color, action):
        self.text = text
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos[0], pos[1], width, height)
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_x = self.pos[0] + (self.width - text_surface.get_width()) // 2
        text_y = self.pos[1] + (self.height - text_surface.get_height()) // 2

        screen.blit(text_surface, (text_x, text_y))

    def is_clicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False
        