import pygame


class Environment:

    def __init__(self):

        # Warehouse obstacles
        self.shelves = [

            pygame.Rect(200, 150, 100, 200),
            pygame.Rect(500, 120, 100, 250),
            pygame.Rect(750, 300, 100, 200)

        ]


        # Charging station
        self.charging_station = pygame.Rect(
            50,
            550,
            80,
            80
        )


        # Delivery zone
        self.delivery_zone = pygame.Rect(
            850,
            50,
            100,
            100
        )
        self.delivery_slots = [
            (1, 17),
            (2, 17),
            (1, 18),
            (2, 18)
        ]

    def check_collision(self, robot_rect):
            for shelf in self.shelves:
                if robot_rect.colliderect(shelf):
                    return True
            return False


    def draw(self, screen):
        font = pygame.font.Font(None, 25)

        # Draw shelves
        for shelf in self.shelves:

            pygame.draw.rect(
                screen,
                (130, 90, 50),
                shelf
            )
            shelf_text = font.render("SHELF", True, (255, 255, 255))
            screen.blit(
                shelf_text,
                (shelf.x + 10, shelf.y + 10))


        # Draw charging station
        pygame.draw.rect(
            screen,
            (50, 200, 80),
            self.charging_station
        )
        font = pygame.font.Font(None, 25)
        charging_text = font.render("CHARGING", True, (255, 255, 255)) 
        screen.blit(
            charging_text,
            (self.charging_station.x , self.charging_station.y - 25)
        )
        #Delivery_text = font.render("DELIVERY", True, (255, 255, 255))
        delivery_text = font.render("DELIVERY", True, (255, 255, 255))
        screen.blit(
            delivery_text,
            (self.delivery_zone.x , self.delivery_zone.y - 25)
        )


        # Draw delivery zone
        pygame.draw.rect(
            screen,
            (70, 150, 255),
            self.delivery_zone
        )
        for row, col in self.delivery_slots:
             rect = pygame.Rect(
                 col * 50,
                 row * 50,
                 50,
                 50
             )
             pygame.draw.rect(
                 screen,
                (120, 180, 255),
                rect,
                 3
         )
        
    
    