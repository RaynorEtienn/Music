"""
src/constants.py
Single Source of Truth.
Defines musical constants, tuning standards, color palettes, and interval formulas.
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

# Standard Guitar Tuning (Low E to High E)
# E=4, A=9, D=2, G=7, B=11, E=4
GUITAR_TUNING_INDICES = [4, 9, 2, 7, 11, 4]

# Formulas (Semitones from Root)
# Includes Chords (Stacking) and Modes/Scales (Linear)
CHORD_FORMULAS = {
    # --- CHORDS (HARMONY) ---
    "Major": [0, 4, 7],
    "Minor": [0, 3, 7],
    "5": [0, 7],
    "7": [0, 4, 7, 10],
    "Maj7": [0, 4, 7, 11],
    "m7": [0, 3, 7, 10],
    "m9": [0, 3, 7, 10, 14],
    "sus4": [0, 5, 7],
    "dim7": [0, 3, 6, 9],
    # --- DIATONIC MODES (SCALES) ---
    "Ionian": [0, 2, 4, 5, 7, 9, 11],  # Major Scale
    "Dorian": [0, 2, 3, 5, 7, 9, 10],  # The "French Touch" / Chic Mode
    "Phrygian": [0, 1, 3, 5, 7, 8, 10],  # Spanish / Tension
    "Lydian": [0, 2, 4, 6, 7, 9, 11],  # Dreamy / Space
    "Mixolydian": [0, 2, 4, 5, 7, 9, 10],  # Rock / Bluesy Major
    "Aeolian": [0, 2, 3, 5, 7, 8, 10],  # Natural Minor
    "Locrian": [0, 1, 3, 5, 6, 8, 10],  # Unstable
    # --- PENTATONICS (GROOVE) ---
    "Minor_Pentatonic": [0, 3, 5, 7, 10],  # The Guitarist's Bread & Butter
    "Major_Pentatonic": [0, 2, 4, 7, 9],  # Country / Soul
}

COLORS = {
    "background": "#FFFFFF",
    "white_key": "#FFFFFF",
    "black_key": "#1A1A1A",
    "highlight_primary": "#DAA520",  # Gold (French Touch)
    "highlight_secondary": "#20B2AA",  # Teal
    "muted": "#CCCCCC",
    "text_main": "#333333",
    "grid": "#E0E0E0",
}
