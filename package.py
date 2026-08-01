import pygame
class Package:
    WAITING = "Waiting"
    PICKED_UP = "Picked up"
    DELIVERED = "Delivered"
    ASSIGNED = "Assigned"
    def __init__(self, position, destination):
        self.position = position
        self.destination = destination
        self.delivery_slot = destination
        self.delivered = False
        self.status = Package.WAITING  # Waiting, Picked up, Delivered
    def draw(self, screen, cell_size):
        row, col = self.position
        rect = pygame.Rect(
            col * cell_size,
            row * cell_size,
            cell_size,
            cell_size
        )
        #Main box
        pygame.draw.rect(
            screen,
            (149, 140, 70),
            rect,
            border_radius=5
        )
        # Border
        pygame.draw.rect(
            screen,
            (90, 60, 30),
            rect,
            2,
            border_radius=5
        )
        pygame.draw.line(
            screen,
            (120, 80, 40),
            (rect.centerx, rect.top ),
            (rect.centerx, rect.bottom),
            2
        )
        pygame.draw.line(
            screen,
            (120, 80, 40),
            (rect.left, rect.centery),
            (rect.right, rect.centery),
            2
        )
        font = pygame.font.Font(None, 22)
        text = font.render("P", True, (255, 255, 255))
        screen.blit(
            text,
            (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2)
        )