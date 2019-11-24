import numpy as np
from Player import Player


chords = [
    {
    "name": "A minor",
    "notes": [0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4],
    "note_durations": np.full(12, 0.4),
    "scale": "harmonic minor"
    }
]

for chord in chords:
    notes = chord["notes"]
    note_durations = chord["note_durations"]
    
    player = Player()
    if "scale" in chord.keys():
        player.set_active_scale(chord["scale"])
    player.set_notes(notes)
    player.set_note_durations(note_durations)
    player.generate_audio()
    player.save_audio("A minor.wav")