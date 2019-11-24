import numpy as np
import random
import simpleaudio as sa
from scipy.io.wavfile import write
from functions import get_notes_from_file

fs = 44100  # 44100 samples per second

notes = np.array(get_notes_from_file("fib.txt"))
note_durations = np.array([0.3 for note in notes])

duration = sum(note_durations)

c = 2 ** (1 / 12)
major_scale = np.array([])
for i in range(0, 1000):
    base = c ** (12 * i)
    major_scale = np.hstack([major_scale, base * np.array([1, c ** 2,  c ** 4, c ** 5, c ** 7, c ** 9, c ** 11, c ** 12])]) 
major_scale *= 440

t = []
frequency = []
intervals = []

T = 0
for i in range(0, len(notes)):
    n = int(fs * note_durations[i])
    intervals.extend(np.full(n, notes[i]))
    for j in range(0, n):
        t.append(T)
        T += 1 / fs

t = np.array(t)
frequency = np.array([major_scale[i] for i in intervals])
 # Our played note will be 440 Hz
print(f"len(intervals): {len(intervals)}")
print(f"len(t): {len(t)}")
print(t)
# Generate a 440 Hz sine wave
note = np.sin(frequency * t * 2 * np.pi)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int16)
write("fib.wav", fs, audio)
# Start playback
#lay_obj = sa.play_buffer(audio, 1, 2, fs)

# Wait for playback to finish before exiting
#play_obj.wait_done()