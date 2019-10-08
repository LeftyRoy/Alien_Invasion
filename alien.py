import pygame
from pygame.sprite import Sprite
import time


def load_image(name):
    image = pygame.image.load(name)
    return image


class Alien(Sprite):

    image1 = ""
    image2 = ""

    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.images = []
        self.images.append(load_image(self.image1))
        self.images.append(load_image(self.image2))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Alien1(Alien):
    image1 = "Images/Alien1-1.png"
    image2 = "Images/Alien1-2.png"
    score = 150


class Alien2(Alien):
    image1 = "Images/Alien2-1.png"
    image2 = "Images/Alien2-2.png"
    score = 100


class Alien3(Alien):
    image1 = "Images/Alien3-1.png"
    image2 = "Images/Alien3-2.png"
    score = 50
