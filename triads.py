from Player import Player

notes = [
    10,
    17,
    22,
    [10, 17, 22],
    [10, 17, 22],
    [10, 17, 22],
    [10, 17, 22],
    [17],
    [20],
    [24],
    [17, 20, 24], 
    [1, 17, 20],
    [0, 17, 19],
    ]

note_durations = [0.4 for note in notes]

player = Player()
player.set_active_scale("chromatic")
player.set_notes(notes)
player.set_note_durations(note_durations)
player.generate_audio()
player.save_audio("triads.wav")
player.play()