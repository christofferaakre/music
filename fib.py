from Player import Player
import numpy as np

file = open("data/fib.txt", 'r')
notes = []
for line in file.readlines():
    # Get the first digit of each number
    note = int(line.replace('\n', '')[0])
    notes.append(note)

# Just picking a reasonable fixed note duration here
# You can definetely be more creative
note_durations = np.array([0.3 for note in notes])

player = Player()

player.set_notes(notes)
player.set_note_durations(note_durations)
player.generate_audio()
player.save_audio(filename="fib.wav")