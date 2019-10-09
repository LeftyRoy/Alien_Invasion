import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button, HighScoreButton
from ship import Ship
import game_functions as gf
import time

black = (0, 0, 0)
white = (255, 255, 255)

# Initialize game and create a screen object.
pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")

# Start Music
pygame.mixer.music.load("Sounds/theme.mp3")
pygame.mixer.music.play(-1)

# Make the Play button.
play_button = Button(ai_settings, screen, "Play")

# Make the High Scores button.
score_button = HighScoreButton(ai_settings, screen, "High Scores")

# Create an instance to store game statistics and create a scoreboard.
stats = GameStats(ai_settings)
sb = Scoreboard(ai_settings, screen, stats)

# Make a ship, a group of bullets, and a group of aliens.
ship = Ship(ai_settings, screen)
bullets = Group()
aliens = Group()
gf.create_fleet(ai_settings, screen, ship, aliens)

# Time
clock = pygame.time.Clock()
fps = 120

# images for title
alien1Img = pygame.image.load('Images/Alien1-1.png')
alien2Img = pygame.image.load('Images/Alien2-1.png')
alien3Img = pygame.image.load('Images/Alien3-1.png')


def alien_pics(image, x1, y1):
    screen.blit(image, (x1, y1))


def text_objects(text, font):
    screen = font.render(text, True, white)
    return screen, screen.get_rect()


def game_menu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        title_font = pygame.font.SysFont(None, 115)
        text_font = pygame.font.SysFont(None, 50)
        text_surf, text_rect = text_objects("SPACE INVASION", title_font)
        text_rect.center = (ai_settings.screen_width / 2, ai_settings.screen_height / 5)
        screen.blit(text_surf, text_rect)
        text_surf1, text_rect1 = text_objects("= 50", text_font)
        text_rect1.center = (ai_settings.screen_width / 1.85, ai_settings.screen_height / 3.1)
        screen.blit(text_surf1, text_rect1)
        text_rect1.center = (ai_settings.screen_width / 1.85, ai_settings.screen_height / 2.4)
        screen.blit(text_surf1, text_rect1)
        text_rect1.center = (ai_settings.screen_width / 1.85, ai_settings.screen_height / 1.95)
        screen.blit(text_surf1, text_rect1)
        alien_pics(alien1Img, ai_settings.screen_width / 2.12, ai_settings.screen_height / 3.25)
        alien_pics(alien2Img, ai_settings.screen_width / 2.12, ai_settings.screen_height / 2.5)
        alien_pics(alien3Img, ai_settings.screen_width / 2.12, ai_settings.screen_height / 2)

        if not stats.game_active:
            play_button.draw_button()
            score_button.draw_button()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                gf.check_play_button(ai_settings, screen, stats, sb, play_button,
                                     ship, aliens, bullets, mouse_x, mouse_y)
                game_loop()
        pygame.display.update()


def game_loop():
    # Start the main loop for the game
    while True:
        clock.tick(fps)

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


game_menu()
game_loop()
