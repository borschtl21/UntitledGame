import pygame
from pygame.locals import *
import sys

pygame.init()
size_screen = 1280, 720
size_buttons = 300, 50
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255
screen = pygame.display.set_mode(size_screen, 0, 32)
screen.fill(black)
font = pygame.font.SysFont(None, 20)


class Button:
    def __init__(self, pos, size, text, screen, function):
        self.function = function
        self.screen = screen
        self.pos = pos
        self.size = size
        self.text = text
        self.img = font.render(self.text, True, black)
        self.rect = pygame.Rect(self.pos, self.size)

    def draw_button(self, color):
        pygame.draw.rect(self.screen, color, self.rect)

    def is_hovered(self):
        x, y = pygame.mouse.get_pos()
        return self.rect.collidepoint(x, y)

    def draw_text(self):
        self.screen.blit(self.img, self.pos)


def play():
    pass


def open_settings():
    pass


def open_character_menu():
    pass


buttons = []
button_play = Button((30, 30), size_buttons, 'Play', screen, play)
button_exit = Button((30, 100), size_buttons, 'Settings', screen, open_settings)
button_settings = Button((30, 240), size_buttons, 'Exit', screen, sys.exit)
button_character = Button((30, 170), size_buttons, 'Choose character', screen, open_character_menu)
buttons.extend([button_play, button_exit, button_settings, button_character])


def mainloop():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            for button in buttons:

                if button.is_hovered() and event.type == pygame.MOUSEBUTTONDOWN:
                    button.function()
                elif button.is_hovered():
                    button.draw_button(blue)
                else:
                    button.draw_button(white)
                button.draw_text()
            pygame.display.update()


if __name__ == '__main__':
    mainloop()
