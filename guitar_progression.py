from Player import Player

notes = [
    # A minor
    5, 17, 20, 24, 20, 17, 
    5, 17, 20, 24, 20, 17,
    # D minor
    10, 17, 22, 25, 22, 17,
    10, 17, 22, 25, 22, 17,
    # F Major
    1, 17, 20, 25, 20, 17,
    1, 17, 19, 24, 19, 17,
    # E Major
    0, 17, 19, 24, 19, 17,
    0, 16, 19, 24, 19, 16, 
]

note_durations = [0.4 for note in notes]

player = Player()
player.set_active_scale("chromatic")
player.set_notes(notes)
player.set_note_durations(note_durations)
player.generate_audio()
player.save_audio("guitar progression.wav")