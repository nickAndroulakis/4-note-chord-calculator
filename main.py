notes=["C","C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Major: 1-3-5
def major(note): 
    return [note, notes[(notes.index(note) + 4) % 12], notes[(notes.index(note) + 7) % 12], note]

# Minor: 1-b3-5
def minor(note):
    return [note, notes[(notes.index(note) + 3) % 12], notes[(notes.index(note) + 7) % 12], note]

# Diminished: 1-b3-b5
def diminished(note):
    return [note, notes[(notes.index(note) + 3) % 12], notes[(notes.index(note) + 6) % 12], note]

# Augmented: 1-3-#5
def augmented(note):
    return [note, notes[(notes.index(note) + 4) % 12], notes[(notes.index(note) + 8) % 12], note]

# Sus2: 1-2-5
def sus2(note):
    return [note, notes[(notes.index(note) + 2) % 12], notes[(notes.index(note) + 7) % 12], note]

# Sus4: 1-4-5
def sus4(note):
    return [note, notes[(notes.index(note) + 5) % 12], notes[(notes.index(note) + 7) % 12], note]

# Major7: 1-3-5-7
def major7(note):
    return [note, notes[(notes.index(note) + 4) % 12], notes[(notes.index(note) + 7) % 12], notes[(notes.index(note) + 11) % 12]]

# Minor7: 1-b3-5-b7
def minor7(note):
    return [note, notes[(notes.index(note) + 3) % 12], notes[(notes.index(note) + 7) % 12], notes[(notes.index(note) + 10) % 12]]

# Dominant7: 1-3-5-b7
def dominant7(note):
    return [note, notes[(notes.index(note) + 4) % 12], notes[(notes.index(note) + 7) % 12], notes[(notes.index(note) + 10) % 12]]

# Diminished7: 1-b3-b5-6
def diminished7(note):
    return [note, notes[(notes.index(note) + 3) % 12], notes[(notes.index(note) + 6) % 12], notes[(notes.index(note) + 9) % 12]]

# HalfDiminished7: 1-b3-b5-b7
def half_diminished7(note):
    return [note, notes[(notes.index(note) + 3) % 12], notes[(notes.index(note) + 6) % 12], notes[(notes.index(note) + 10) % 12]]

# Major6: 1-3-5-6
def major6(note):
    return [note, notes[(notes.index(note) + 4) % 12], notes[(notes.index(note) + 7) % 12], notes[(notes.index(note) + 9) % 12]]

# Minor6: 1-b3-5-6
def minor6(note):
    return [note, notes[(notes.index(note) + 3) % 12], notes[(notes.index(note) + 7) % 12], notes[(notes.index(note) + 9) % 12]]

def return_dry(note):
    return str(major(note)) + "\n" + str(major7(note)) + "\n" + str(minor(note)) + "\n" + str(minor7(note)) + "\n" + str(diminished(note)) + "\n" + str(augmented(note)) + "\n" + str(sus2(note)) + "\n" + str(sus4(note)) + "\n" + str(dominant7(note)) + "\n" + str(diminished7(note)) + "\n" + str(half_diminished7(note)) + "\n" + str(major6(note)) + "\n" + str(minor6(note)) + "\n"

f = open("output.txt", "a")
for note in notes:
    f.write(return_dry(note))
f.close()