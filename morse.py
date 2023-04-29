import numpy as np
import pyaudio

from beeps import *
from alphabet import morse_dict

class MorsePlayer(object):
    def __init__(self):
        configs = read_beeps_config_file()

        if configs is None:
            print("configs was None")
            sys.exit(1)
        else:
            self.sample_rate = configs['sample_rate']
            self.dit_time = configs['dit_time']
            self.frequency = configs['frequency']

        # dit_time comes from config file
        self.char_space_time = self.dit_time * 3
        self.word_space_time = self.dit_time * 7
        self.dah_time = self.char_space_time

        self.py_audio = mk_pyaudio()
        self.stream = open_stream(self.py_audio, self.sample_rate)

    def __del__(self):
        close_stream(self.stream)
        stop_pyaudio(self.py_audio)

    def dit(self):
        tone(self.stream, self.sample_rate, self.dit_time, self.frequency)

    def dah(self):
        tone(self.stream, self.sample_rate, self.dah_time, self.frequency)

    def word_space(self):
        tone(self.stream, self.sample_rate, self.word_space_time, 0)

    def char_space(self):
        tone(self.stream, self.sample_rate, self.char_space_time, 0)

    def el_space(self):
        tone(self.stream, self.sample_rate, self.dit_time, 0)

    def dit_or_dah(self, s):
        if s == '.':
            self.dit()
        elif s == '-':
            self.dah()

    def play_ditdahs(self, s):
        if len(s) == 0:
            return
        elif len(s) == 1:
            self.dit_or_dah(s)
        else: # more than one
            first = s[0]
            rest = s[1:]

            self.dit_or_dah(first)

            for c in rest:
                self.el_space()
                self.dit_or_dah(c)


        for c in rest:
            char_space(stream)

            play_ditdahs(stream, morse_dict[c])
    def dit_or_dah(self, s):
        if s == '.':
            self.dit()
        elif s == '-':
            self.dah()

def play_string(stream, s):
    words = s.split()

    if len(words) == 0:
        return
    elif len(words) == 1:
        play_word(stream, words[0])
    else:
        first = words[0]
        rest = words[1:]

        play_word(stream, first)

        for w in rest:
            word_space(stream)
            play_word(stream, w)
