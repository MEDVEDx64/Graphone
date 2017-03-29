from pygame.locals import *

KS_UP = 0
KS_PRESSED = 1
KS_DOWN = 2
KS_RELEASED = 3


class KeyboardManager(object):
    def __init__(self):
        self.key_states = {}

    def handle_events(self, events):
        for k in self.key_states:
            if self.key_states[k] == KS_PRESSED:  self.key_states[k] = KS_DOWN
            if self.key_states[k] == KS_RELEASED: self.key_states[k] = KS_UP

        for e in events:
            if e.type == KEYDOWN:
                self.key_states[e.key] = KS_PRESSED
            elif e.type == KEYUP:
                self.key_states[e.key] = KS_RELEASED

    def get_key_state(self, key):
        try:
            return self.key_states[key]
        except KeyError:
            return KS_UP
