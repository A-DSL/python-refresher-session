# Task: Re-create your old program where it would print a random guitar note on your EADGBE-tuned guitar.
# 1. Establish basic functionality. A random guitar note should be picked and then printed.
# 2. Make the program continuous following an initial prompt, providing notes every few seconds.
import random

# Lists of every string's un-fretted note + 15 fretted notes
lowEstring = ["E2", "F2", "F#2", "Gb2", "G2", "G#2", "Ab2", "A2", "A#2", "Bb2", "B2", "C3", "C#3", "Db3", "D3", "D#3", "Eb3", "E3", "F3", "F#3", "Gb3", "G3"]
Astring = ["A2", "A#2", "Bb2", "B2", "C3", "C#3", "Db3", "D3", "D#3", "Eb3", "E3", "F3", "F#3", "Gb3", "G3", "G#3", "Ab3", "A3", "A#3", "Bb3", "B3", "C4"]
Dstring = ["D3", "D#3", "Eb3", "E3", "F3", "F#3", "Gb3", "G3", "G#3", "Ab3", "A3", "A#3", "Bb3", "B3", "C4", "C#4", "Db4", "D4", "D#4", "Eb4", "E4", "F4"]
Gstring = ["G3", "G#3", "Ab3", "A3", "A#3", "Bb3", "B3", "C4", "C#4", "Db4", "D4", "D#4", "Eb4", "E4", "F4", "F#4", "Gb4", "G4", "G#4", "Ab4", "A4", "A#4", "Bb4"]
Bstring = ["B3", "C4", "C#4", "Db4", "D4", "D#4", "Eb4", "E4", "F4", "F#4", "Gb4", "G4", "G#4", "Ab4", "A4", "A#4", "Bb4", "B4", "C5", "C#5", "Db5", "D5"]
highEstring = ["E4", "F4", "F#4", "Gb4", "G4", "G#4", "Ab4", "A4", "A#4", "Bb4", "B4", "C5", "C#5", "Db5", "D5", "D#5", "Eb5", "E5", "F5", "F#5", "Gb5", "G5"]
guitarStrings = [lowEstring, Astring, Dstring, Gstring, Bstring, highEstring]

# Function to select string and note
def selectString():
    selectedString = guitarStrings[random.randint(0, 5)]
    if selectedString == lowEstring:
        note = lowEstring[random.randint(0, len(lowEstring)-1)]
        return "Play " + note + " on the low E string."
    elif selectedString == Astring:
        note = Astring[random.randint(0, len(Astring)-1)]
        return "Play " + note + " on the A string."
    elif selectedString == Dstring:
        note = Dstring[random.randint(0, len(Dstring)-1)]
        return "Play " + note + " on the D string."
    elif selectedString == Gstring:
        note = Gstring[random.randint(0, len(Gstring)-1)]
        return "Play " + note + " on the G string."
    elif selectedString == Bstring:
        note = Bstring[random.randint(0, len(Bstring)-1)]
        return "Play " + note + " on the B string."
    elif selectedString == highEstring:
        note = highEstring[random.randint(0, len(highEstring)-1)]
        return "Play " + note + " on the high E string."
    else:
        return "Error"

print(selectString())