import os
import pygame
import pygame.gfxdraw

from utils import printy


class ContentLoader(object):
    def __init__(self):
        self._cached_images = {}

        self._fallback_image = pygame.Surface([64, 64], depth=24)
        pygame.gfxdraw.box(self._fallback_image, (0, 0, 63, 63), (0, 0, 0))
        pygame.gfxdraw.box(self._fallback_image, (0, 0, 31, 31), (255, 0, 255))
        pygame.gfxdraw.box(self._fallback_image, (32, 32, 63, 63), (255, 0, 255))

    # Returns path to an asset file, OS-independently
    def get_asset(self, path):
        return os.path.join('assets', path.replace('/', os.path.sep))

    # Loads an image, even if it doesn't exist
    def load_image(self, path):
        asset = self.get_asset(path)
        if asset in self._cached_images:
            return self._cached_images[asset]

        try:
            img = pygame.image.load(asset)
            self._cached_images[asset] = img
            printy.info('Loaded image "' + path + '"')
            return img

        except Exception as e:
            printy.err('Error while loading image "' + path + '": ' + str(e))
            return self._fallback_image
