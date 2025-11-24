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

# Mapping Semitones -> Interval Name (Simplified)
INTERVAL_MAP = {
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

COLORS = {
    "background": "#FFFFFF",
    "white_key": "#FFFFFF",
    "black_key": "#1A1A1A",
    # --- FUNCTIONAL COLORS (NEW) ---
    "root": "#FF4500",  # OrangeRed (La base)
    "third": "#FFD700",  # Gold (L'émotion - Majeure ou Mineure)
    "fifth": "#4682B4",  # SteelBlue (La structure stable)
    "seventh": "#9370DB",  # MediumPurple (Le Funk)
    "extension": "#20B2AA",  # LightSeaGreen (9, 11, 13 - La couleur House)
    "default": "#DAA520",  # Fallback
    "muted": "#CCCCCC",
    "text_main": "#333333",
    "text_light": "#FFFFFF",
    "grid": "#E0E0E0",
}

# Mapping Interval Semitone -> Color Key
INTERVAL_COLOR_MAP = {
    0: "root",
    3: "third",
    4: "third",  # Tierces min/maj
    7: "fifth",  # Quinte
    10: "seventh",
    11: "seventh",  # 7èmes min/maj
    2: "extension",
    14: "extension",  # 9ème
    5: "extension",  # 11ème / 4te
    9: "extension",  # 13ème / 6te
}
