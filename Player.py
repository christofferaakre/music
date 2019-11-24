import numpy as np
import simpleaudio as sa
from scipy.io import wavfile

from scales import scales

class Player(object):
    # 44100 Hz is one of the standard 
    # wav sampling rates, so we default to this
    def __init__(self, sample_rate = 44100):
        """
        Initializes a Player instance, e.g. player = Player()
        """
        # This function just uses the first digit of the number to decide
        # the scale degree to play
        self.get_note_from_integer = lambda x: int(x[0])
        self.notes = np.array([])
        self.note_durations = np.array([])
        self.duration = 0
        # 440 Hz is the standard A used for tuning
        # most instruments
        self.base = 440
        self.audio  = np.array([])
        self.sample_rate = sample_rate
        # To get scale tones, we use equal temperament,
        # where each semitone is reached by multiplying
        # the frequency of a pitch by 2^(1/12). This way,
        # an octaver will have exactly twice the frequency,
        # and the notes in between will be (gemoetrically)
        # evenly spaced. Equal temperament is pretty much
        # THE tuning method used in all of Western music.
        # See https://en.wikipedia.org/wiki/Equal_temperament
        # for more information
        self.semitone = 2 ** (1 / 12)
        self.scales = {}
    
        for scale in scales.keys():
            self.add_scale(name=scale, scale=scales[scale])

        # Defaulting the scale to harmonic minor
        self.active_scale = self.scales["harmonic minor"]

    def set_base(self, base: int):
        """
        Sets the base frequency to
        use for new scales.
        """
        self.base = base
        return self.base
    
    def set_get_note(self, function: callable):
        """
        Sets the get_note_from_integer function. By default,
        this function just uses the first digit in a number,
        but you can change that by passing set_get_note a function.
        """
        self.get_note_from_integer = function
        return self.get_note_from_integer

    def update_duration(self):
        """
        When we change the notes or
        the note durations, the total
        duration also changes, so we
        must update it. This happens automatically,
        as update_duration is called in both
        set_notes and set_note_durations.
        """
        print(f"len(self.note_durations) = {len(self.note_durations)}")
        self.duration = self.notes * self.note_durations
        return self.duration

    def set_notes(self, notes: list):
        """
        Sets the player's notes
        using the given list.
        """
        # Making sure all the notes are integers
        self.notes = np.array(notes).astype(int)
        # If the length of self.notes and self.note_durations is not
        # the same, then that probably just means you've called
        # either set_notes or set_note_durations but not the other
        # We onlyu want to call update_duration if the lengths are the same,
        # because it will (rightfully) throw an error otherwise.
        if len(self.notes) == len(self.note_durations):
            self.update_duration()
        return self.notes
        
    def set_note_durations(self, durations: list):
        """
        Uses the given list to set the
        durations of the notes.
        """
        # Making sure note durations are floats
        self.note_durations = np.array(durations).astype(float)
        # See the method declaration of set_notes; we only want to call
        # update_duration if self.notes has the same length as 
        # self.note_durations
        if len(self.notes) == len(self.note_durations):
            self.update_duration()
        return self.note_durations

    def set_active_scale(self, name: str):
        """
        Sets the active scale to the
        provided scale name, provided
        the scale exists in self.scales
        """
        self.scale = self.scales[name]
        return self.name

    def add_scale(self, name: str, scale: list, base: int = None, number_of_octaves: int = 100):
        """
        Adds a given scale to the Player
        with the given name and base,
        e.g. Player().add_scale("melodic minor", [*scaletones]).
        """
        # Defaulting the base to self.base if no base is given
        if not base:
            base = self.base
        
        # Here we extend the given scale up to many ovtaves.
        # The default is 100 octaves, but we can go higher
        # if we want to. 100 octaves is proably plenty
        # for most use cases though
        extended_scale = self.base * np.array(scale)
        for i in range(1, number_of_octaves):
            octave = self.semitone ** (12 * i)
            extended_scale = np.hstack([
                extended_scale, octave * np.array(scale)
            ])
        self.scales[name] = extended_scale
        return extended_scale
    
    def generate_audio(self, scale: list = None):
        """
        Uses the given scale, defaulting to self.active_scale,
        to generate audio from self.notes and self.note_durations,
        then stores it in self.audio.
        """
        # Make sure there is a note duration
        # specified for each note       
        try:
            len(self.notes) == len(self.note_durations)
        except:
            raise Exception("self.notes does not have the same length as self.note_durations")
        # Default the scale to self.active_scale if
        # no scale is given
        if not scale:
            scale = self.active_scale
        T = []
        frequency = []
        intervals = []

        t = 0
        progress = 0
        # Prints like this and others that come up later in this
        # function are just there to give the user an idea
        # of what is going, on, because this function can
        # take a while to run if you give it a lot of data
        print("Generating t list and intervals...")

        for i in range(0, len(self.notes)):
            # Calculate the percentage progress in the loop
            # and print it out if it is more than 1% more than
            # last time we printed it
            new_progress = (i + 1) / len(self.notes) * 100
            if new_progress - progress >= 1:
                progress = new_progress
                print(f"{int(progress)}%")
            #################################################

            # This is how many 'instances' of the note we need to 
            # cover its duration using our sample rate
            n = int(self.sample_rate * self.note_durations[i])
            # Just stick as many notes as we need into the intervals list
            intervals.extend(np.full(n, self.notes[i]))
            # Increment t n times since we added intervals to the intervals list
            for j in range(0, n):
                T.append(t)
                # 1 over the sample rate
                # is the 'smallest possible time'
                # for our melody
                t += 1 / self.sample_rate
       
        T = np.array(T)
        
        print("Converting scale intervals to frequencies...")
        intervals = np.array(intervals).astype(int)
        frequency = np.array([scale[interval] for interval in intervals])
        
        print("Building sine waves...")
        note = np.sin(frequency * T * 2 * np.pi)
        
        print("Building audio...")
        audio = note * (2 ** 15 - 1) / np.max(np.abs(note))
        audio = audio.astype(np.int16)
        
        self.audio = audio
        print("Done!")
        
        return self.audio
    
    def play(self):
        """
        Plays the audio stored in self.audio.
        """
        # Start playback
        play_object = sa.play_buffer(self.audio, 1, 2, self.sample_rate)
        # Wait until the audio is finished playing before exiting
        play_object.wait_done()
    
    def save_audio(self, filename: str, no_audio_folder: bool = False) -> str:
        """
        Saves the audio stored in self.audio
        to the specified .wav file.
        """
        save_location = ''
        if no_audio_folder:
            save_location = filename
        else:
            save_location = f"audio/{filename}"
        
        if '.wav' not in save_location:
            save_location = f"{save_location}.wav"

        wavfile.write(save_location, self.sample_rate, self.audio)
        return save_location
    
    def __repr__(self):
        """
        Defines how to show the Player instance
        e.g. when printing it.
        """
        return str({
            "scales": list(self.scales.keys()),
            "audio": list(self.audio),
            "base": self.base,
            "sample rate": self.sample_rate
        })
