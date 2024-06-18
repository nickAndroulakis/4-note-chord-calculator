notes=["C","C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Major: 1-3-5
def major(note): 
    return [note, notes[(notes.index(note) + 4) % 12], notes[(notes.index(note) + 7) % 12]]

# Major 1st Inversion: 3-5-1
def major_inversion(note):
    return [notes[(notes.index(note) + 4) % 12], notes[(notes.index(note) + 7) % 12], note]

# Major 2nd Inversion: 5-1-3
def major_inversion2(note):
    return [notes[(notes.index(note) + 7) % 12], note, notes[(notes.index(note) + 4) % 12]]

# Minor: 1-b3-5
def minor(note):
    return [note, notes[(notes.index(note) + 3) % 12], notes[(notes.index(note) + 7) % 12]]

# Minor 1st Inversion: b3-5-1
def minor_inversion(note):
    return [notes[(notes.index(note) + 3) % 12], notes[(notes.index(note) + 7) % 12], note]

# Minor 2nd Inversion: 5-1-b3
def minor_inversion2(note):
    return [notes[(notes.index(note) + 7) % 12], note, notes[(notes.index(note) + 3) % 12]]

def return_dry(note):
    return str(major(note)) + "\n" + str(major_inversion(note)) + "\n" + str(major_inversion2(note)) + "\n" + str(minor(note)) + "\n" + str(minor_inversion(note)) + "\n" + str(minor_inversion2(note)) + "\n"

f = open("output_simple.txt", "a")
for note in notes:
    f.write(return_dry(note))
f.close()