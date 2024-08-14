import pygame
import sys

from grid import *
from settings import *
from algorithms import *

def main():
    
    # Initializes the game
    pygame.init()
    
    screen_width, screen_height = 800, 600
    block_size = 20
    UI_height = screen_height * 0.15
    
    block_width = (screen_width // block_size)
    block_height = int((screen_height // block_size) - (UI_height // block_size))
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pathfinding visualizer")
    
    running = True
    grid = Grid(block_width, block_height, block_size, screen)
    
    ui = UI(UI_height, screen_width)
    ui.add_button( "start", ((800//8*3 + 12),(600 - 600 * 0.10)), 75, 25, GREEN, start_action)
    ui.add_button("restart", ((800//8*4 + 12), (600-600*0.10)), 75, 25, RED, restart_action)
    
    ui.add_button("BFS", ((800//8*2 + 12), (600-600*0.10)), 75, 25, LIGHT_BLUE, bfs)
    ui.add_button("B", ((800//8*1 + 12), (600-600*0.10)), 75, 25, LIGHT_BLUE, algorithm_button)
    ui.add_button("A", ((800//8*0 + 12), (600-600*0.10)), 75, 25, LIGHT_BLUE, algorithm_button )
    
    ui.add_button("Random", ((800//8*5 + 12), (600-600*0.10)), 75, 25, LIGHT_BLUE, random_walls)
    ui.add_button("Maze", ((800//8*6 + 12), (600-600*0.10)), 75, 25, LIGHT_BLUE, maze)
    ui.add_button("Bla", ((800//8*7 + 12), (600-600*0.10)), 75, 25, LIGHT_BLUE, algorithm_button )
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if grid.is_clicked(event.pos):
                    grid.handle_click(event.pos, screen)
                else:
                    for button in ui.buttons:
                        if button.is_clicked(event):
                            print(f"{button.text} was clicked")
                            button.action(grid, screen)

        screen.fill((0, 0, 0))
        grid.draw()
        for button in ui.buttons:
            button.draw(screen)
        pygame.display.update()
        
        
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
