import pygame


class GridMap:

    def __init__(self, width, height, cell_size):

        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.rows = height // cell_size
        self.cols = width // cell_size


        # Create empty map
        self.grid = []

        for row in range(self.rows):
            self.grid.append(
                [0] * self.cols
            )
    def add_obstacle(self, rect):

        start_col = rect.x // self.cell_size
        start_row = rect.y // self.cell_size
        
        end_col = (rect.x + rect.width) // self.cell_size
        end_row = (rect.y + rect.height) // self.cell_size
        
        
        for row in range(start_row, end_row):
        
            for col in range(start_col, end_col):
        
                if row < self.rows and col < self.cols:
                        self.grid[row][col] = 1
                


    def draw(self, screen):

        for row in range(self.rows):

            for col in range(self.cols):

                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                pygame.draw.rect(
                    screen,
                    (55, 60, 70),
                    rect,
                    1
                )


                pygame.draw.rect(
                    screen,
                    (55,60,70),
                    rect,
                    1
                )
    def draw_path(self, screen, path):

        for row, col in path:

            rect = pygame.Rect(
                col * self.cell_size,
                row * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(
                screen,
                (255, 220, 0),
                rect
            )