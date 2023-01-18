import numpy as np
import simpleaudio as sa

SAMPLE_RATE = 44100
DURATION = 200
TIME_VECT = np.linspace(0, DURATION, DURATION * SAMPLE_RATE, False)

frequencies = [440, 520, 630, 740, 880, 740, 630, 520, 440]
volume = 15

for frequency in frequencies:
    audio = np.round(np.sin(frequency * TIME_VECT * 2 * np.pi))
    audio *= volume * 32767
    audio = audio.astype(np.int16)
    sa.stop_all()
    sa.play_buffer(audio, 1, 2, SAMPLE_RATE)