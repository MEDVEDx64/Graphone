import pygame

from . import base
from config import config
from utils import keyboard
from pygame.locals import *


class QuitHandlerLayer(base.InteractiveLayer):
    def tick(self, events):
        for e in events:
            if e.type == QUIT:
                self.app.running = False


class SimpleArrowKeysHandlerLayer(base.InteractiveLayer):
    def tick(self, events):
        speed = 4
        km = self.app.km
        km.handle_events(events)

        if km.get_key_state(K_UP) == keyboard.KS_DOWN:
            self.app.context.offset_y += speed
        if km.get_key_state(K_DOWN) == keyboard.KS_DOWN:
            self.app.context.offset_y -= speed
        if km.get_key_state(K_LEFT) == keyboard.KS_DOWN:
            self.app.context.offset_x += speed
        if km.get_key_state(K_RIGHT) == keyboard.KS_DOWN:
            self.app.context.offset_x -= speed


class TTFInitLayer(base.Layer):
    def __init__(self, app):
        super(TTFInitLayer, self).__init__(app)
        pygame.font.init()
        self.app.font = pygame.font.Font(self.app.get_asset('FreeSans.ttf'), 12)
