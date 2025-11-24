"""
src/constants.py

Defines the musical constants, tuning standards, and visual styling for the project.
This file serves as the Single Source of Truth for note naming and aesthetic configuration.
"""

# Chromatic scale using Sharps for simplicity in calculation
# Index 0 = C
CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Translation map: International (Key) -> Solfège (Value)
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
# Represented by their index in the CHROMATIC_SCALE
# E=4, A=9, D=2, G=7, B=11, E=4
GUITAR_TUNING_INDICES = [4, 9, 2, 7, 11, 4]

# Visual Styling - French Touch Aesthetic
COLORS = {
    "background": "#FFFFFF",
    "white_key": "#FFFFFF",
    "black_key": "#1A1A1A",
    "highlight_primary": "#DAA520",  # Goldenrod (The "Touch" Gold)
    "highlight_secondary": "#20B2AA",  # LightSeaGreen (Extensions/Modulations)
    "highlight_root": "#FF4500",  # OrangeRed (Root Notes)
    "muted": "#A9A9A9",  # DarkGray (Muted Strings)
    "text_main": "#333333",
    "text_light": "#FFFFFF",
}
