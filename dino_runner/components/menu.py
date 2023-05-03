import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT
from dino_runner.components.counter import Counter

class Menu:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2

    def __init__(self, screen, message):
        screen.fill((0, 0, 0))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def update(self, game):
        self.hundle_event_on_menu(game)
        pygame.display.update()

    def draw(self, screen, score,deaths, max_score):
        font = pygame.font.Font(FONT_STYLE, 25)
        score_show = font.render(f"Score : {score}", True, (255,255,255))
        score_show_rect = score_show.get_rect()
        score_show_rect.center = (self.half_screen_width, 300)        
        screen.blit(self.text, self.text_rect)
        
        max_score = font.render(f"Max Score: {max_score}", True, (255,255,255))
        max_score_rect = max_score.get_rect()
        max_score_rect.center = (self.half_screen_width, 500)
        screen.blit(max_score, max_score_rect)
        
        dino_deaths = font.render(f"Dino Deaths: {deaths}", True, (255,255,255))
        dino_deaths_rect = dino_deaths.get_rect()
        dino_deaths_rect.center = (self.half_screen_width, 400)
        screen.blit(dino_deaths, dino_deaths_rect)
        screen.blit(self.text, self.text_rect)
        
    def reset_screen_color(self, screen):
        screen.fill((0, 0, 0))

    def hundle_event_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()
     
     