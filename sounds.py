import pygame

class SoundEffects:
    def __init__(self):
        self.sounds = {
             'click':pygame.mixer.Sound("beep.wav"),
             'gameover' :pygame.mixer.Sound("mixkit-player-losing-or-failing-2042.wav"),
             'tir':pygame.mixer.Sound("laser1.wav"),
             'score_sound': pygame.mixer.Sound("mixkit-arcade-retro-changing-tab-206.wav"),
            
        }

    def play(self, name):
        self.sounds[name].play()