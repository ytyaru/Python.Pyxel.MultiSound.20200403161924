#!/usr/bin/env python3
# coding: utf8
import pyxel
class App:
    def __init__(self):
        pyxel.init(96, 54, caption="Sound API. Multi sounds.")
        self.__set_sounds()
        self.__play()
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.is_play: self.__stop()
            else: self.__play()
    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, 'Please SPACE key: ' + ('PLAY' if self.is_play else 'STOP'), 7)
    def __play(self):
        pyxel.play(self.ch1, self.sounds, loop=True)
        self.is_play = True
    def __stop(self):
        pyxel.stop()
        self.is_play = False
    def __set_sounds(self):
        self.ch1 = 0
        self.sounds = [0, 1]
        self.__set_sound00()
        self.__set_sound01()
    def __set_sound00(self): # Diatonic C Major
        self.__set_sound(0, "c2d2e2f2g2a2b2c3")
    def __set_sound01(self): # Diatonic D Major
        self.__set_sound(1, "d2e2f#2g2a2b2c#3d3")
    def __set_sound(self, snd, notes):
        tones = "p"
        volumes = "6"
        effects = "n"
        speed = 30
        pyxel.sound(snd).set(
            notes,
            tones,
            volumes ,
            effects ,
            speed,
        )
        
App()
