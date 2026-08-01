import pygame


class Button:

    def __init__(self, x, y, width, height, text):

        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        self.text = text

        self.color = (70, 80, 100)
        self.hover_color = (100, 120, 150)


    def draw(self, screen):

        mouse = pygame.mouse.get_pos()

        color = self.color

        if self.rect.collidepoint(mouse):
            color = self.hover_color


        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=8
        )


        font = pygame.font.Font(None, 25)

        text = font.render(
            self.text,
            True,
            (255,255,255)
        )

        screen.blit(
            text,
            (
                self.rect.centerx - text.get_width()//2,
                self.rect.centery - text.get_height()//2
            )
        )


    def clicked(self):

        if pygame.mouse.get_pressed()[0]:

            if self.rect.collidepoint(
                pygame.mouse.get_pos()
            ):
                return True

        return False
    def set_text(self, new_text):
        self.text = new_text