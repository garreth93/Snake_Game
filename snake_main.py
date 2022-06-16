import pygame

import sys

from snake_packet import Settings

class SnakeMain:

    def __init__(self):
        
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake Game")

    def draw(self):

        self.screen.fill(self.settings.background_color)

        pygame.display.flip()


    def main_cicle(self):    

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.draw()

if __name__ == '__main__':
    game = SnakeMain()
    game.main_cicle()



