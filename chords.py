import numpy as np
from Player import Player


chords = [
    {
    "name": "A minor",
    "notes": [0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4],
    "note_durations": np.full(12, 0.4),
    },
    {
    "name": "D minor",
    "notes": [3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7],
    "note_durations": np.full(12, 0.4),
    },
    {
    "name": "F major",
    "notes": [5, 7, 9, 5, 7, 9, 5, 7, 9, 5, 7, 9],
    "note_durations": np.full(12, 0.4),
    "scale": "major"
    },
    {
    "name": "E major",
    "notes": [4, 6, 8, 4, 6, 8, 4, 6, 8, 4, 6, 8],
    "note_durations": np.full(12, 0.4)
    },
    
]

# Chord progression
# Am Dm Fmaj EMaj
player = Player()
notes = []
note_durations = []

for chord in chords:
    notes.extend(chord["notes"])
    note_durations.extend(chord["note_durations"])
player.set_notes(notes)
player.set_note_durations(note_durations)
player.set_base(220)
player.generate_audio()
player.save_audio("Am-Dm-Fmaj-Emaj.wav")

# Separate files
for chord in chords:
    notes = chord["notes"]
    note_durations = chord["note_durations"]
    
    player = Player()
    player.set_notes(notes)
    player.set_note_durations(note_durations)
    player.set_base(220)
    player.generate_audio()
    player.save_audio(f"{chord['name']}.wav")