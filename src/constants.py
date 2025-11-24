"""
src/constants.py
Single Source of Truth.
"""

# Chromatic scale (Simplified for calculation)
CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Translation map
NOTE_TRANSLATION = {
    "C": "Do",
    "C#": "Do#",
    "Db": "Réb",
    "D": "Ré",
    "D#": "Ré#",
    "Eb": "Mib",
    "E": "Mi",
    "F": "Fa",
    "F#": "Fa#",
    "Gb": "Solb",
    "G": "Sol",
    "G#": "Sol#",
    "Ab": "Lab",
    "A": "La",
    "A#": "La#",
    "Bb": "Sib",
    "B": "Si",
}

# Intervals Mapping (Semitones -> Name)
INTERVALS = {
    0: "R",
    1: "b2",
    2: "2",
    3: "b3",
    4: "3",
    5: "4",
    6: "b5",
    7: "5",
    8: "b6",
    9: "6",
    10: "b7",
    11: "7",
}

# Chord Formulas (Semitones from Root)
# Essential for French Touch / House
CHORD_FORMULAS = {
    "Major": [0, 4, 7],  # Happy
    "Minor": [0, 3, 7],  # Sad
    "5": [0, 7],  # Power Chord
    "7": [0, 4, 7, 10],  # Dominant (Funk)
    "Maj7": [0, 4, 7, 11],  # Jazzy/Dreamy
    "m7": [0, 3, 7, 10],  # The "French Touch" standard
    "m9": [0, 3, 7, 10, 14],  # Deep House
    "sus4": [0, 5, 7],  # Tension
    "dim7": [0, 3, 6, 9],  # Passing chord
}

GUITAR_TUNING_INDICES = [4, 9, 2, 7, 11, 4]  # E A D G B E

COLORS = {
    "background": "#FFFFFF",
    "white_key": "#FFFFFF",
    "black_key": "#1A1A1A",
    "highlight_primary": "#DAA520",  # Gold
    "highlight_secondary": "#20B2AA",  # Teal
    "muted": "#CCCCCC",
    "text_main": "#333333",
    "grid": "#E0E0E0",
}
