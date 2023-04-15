#!/usr/bin/env python3
# Adapted From YouTube StackOverflow
# https://stackoverflow.com/questions/31674416/python-realtime-audio-streaming-with-pyaudio-or-something-else
# https://people.csail.mit.edu/hubert/pyaudio/#examples

import pyaudio
import sys
import numpy as np

waveform = np.sin
wavetable_length = 64
wave_table = np.zeros((wavetable_length,))
for n in range(wavetable_length):
    wave_table[n] = waveform(2 * np.pi * n / wavetable_length)

#CHUNK = 1024

#if len(sys.argv) < 2:
#    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#    sys.exit(-1)

#total_samples = round(t * sample_rate)

#wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

#data = wf.readframes(CHUNK)

#while data != '':
#    stream.write(data)
#    data = wf.readframes(CHUNK)

for n in total_samples:
    stream.write(wave_table[int(np.floor(index))])
    index += indexIncrement
    index %= wavetable_length

stream.stop_stream()
stream.close()

p.terminate()

