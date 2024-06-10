import sys

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

def determine_chord(notes):
    # Define chord variations and their corresponding notes
    chord_variations = {
        'Major': major(notes[0]),
        'Major7': major7(notes[0]),
        'Minor': minor(notes[0]),
        'Minor7': minor7(notes[0]),
        'Diminished': diminished(notes[0]),
        'Augmented': augmented(notes[0]),
        'Sus2': sus2(notes[0]),
        'Sus4': sus4(notes[0]),
        'Dominant7': dominant7(notes[0]),
        'Diminished7': diminished7(notes[0]),
        'HalfDiminished7': half_diminished7(notes[0]),
        'Major6': major6(notes[0]),
        'Minor6': minor6(notes[0]),
        # Add more chord variations and their notes as needed
    }

    # Convert input notes to a set for easier comparison
    input_notes = set(notes)

    # Iterate over chord variations and check if input notes match
    for variation, chord_notes in chord_variations.items():
        if set(chord_notes) == input_notes:
            return notes[0] + "-" + variation

    # If no match is found, return None
    return None

test_notes = ['D#', 'G#', 'A#', 'D#']
print(determine_chord(test_notes))
