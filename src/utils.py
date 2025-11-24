"""
src/utils.py
Logic for notes, intervals, and chord/scale calculation.
"""

from typing import List, Tuple
from src.constants import (
    CHROMATIC_SCALE,
    GUITAR_TUNING_INDICES,
    NOTE_TRANSLATION,
    CHORD_FORMULAS,
    COLORS,
    INTERVAL_COLOR_MAP,
)


def note_to_int(note: str) -> int:
    """Converts 'C' to 0, 'C#' to 1, ... 'B' to 11."""
    flat_map = {"Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#"}
    clean_note = flat_map.get(note, note)
    try:
        return CHROMATIC_SCALE.index(clean_note)
    except ValueError:
        raise ValueError(f"Note {note} not found in chromatic scale.")


def get_dual_lang_label(note_en: str) -> str:
    """Returns formatted string 'C\n(Do)'."""
    note_fr = NOTE_TRANSLATION.get(note_en, note_en)
    return f"{note_en}\n({note_fr})"


def get_note_color(root_val: int, note_val: int) -> str:
    """
    Returns the hex color code based on the interval between root and note.
    """
    # Distance en demi-tons (modulo 12)
    interval = (note_val - root_val) % 12

    color_key = INTERVAL_COLOR_MAP.get(interval, "default")
    return COLORS[color_key]


def fret_to_note(string_index: int, fret_number: int) -> str:
    """Returns the note name at a specific guitar position."""
    base = GUITAR_TUNING_INDICES[string_index]
    return CHROMATIC_SCALE[(base + fret_number) % 12]


def calculate_piano_indices(
    root_note: str, formula_name: str, inversion: int = 0
) -> List[int]:
    """
    Calculates ABSOLUTE SEMITONE INDICES relative to C3 (0) for Piano.
    Compatible with Chords AND Scales.
    """
    if formula_name not in CHORD_FORMULAS:
        raise ValueError(f"Formula '{formula_name}' not defined.")

    root_val = note_to_int(root_note)
    formula = CHORD_FORMULAS[formula_name]

    # Generate notes (Absolute semitones from C0 reference, adjusted to C3 start)
    # We map Root relative to C.
    chord_notes = [(root_val + interval) for interval in formula]

    # Apply Inversion (Only makes sense for chords, but code handles list rotation)
    if inversion > 0:
        for _ in range(inversion):
            note = chord_notes.pop(0)
            chord_notes.append(note + 12)  # Move octave up

    # Normalize for Visualizer (Aim for C3-B4 range: 0 to 23)
    # 1. Shift down if too high
    while min(chord_notes) >= 12:
        chord_notes = [n - 12 for n in chord_notes]
    # 2. Shift up if too low
    while min(chord_notes) < 0:
        chord_notes = [n + 12 for n in chord_notes]

    return chord_notes


def get_all_fretboard_positions(
    root_note: str, formula_name: str, max_fret: int = 12
) -> List[Tuple[int, int]]:
    """
    Scans the guitar fretboard and returns ALL (string, fret) tuples
    that match the notes in the requested scale/chord.

    Args:
        root_note: 'A', 'C#', etc.
        formula_name: 'Dorian', 'm7', etc.
        max_fret: How far to scan (default 12).
    """
    if formula_name not in CHORD_FORMULAS:
        raise ValueError(f"Formula '{formula_name}' not defined.")

    root_val = note_to_int(root_note)
    formula = CHORD_FORMULAS[formula_name]

    # Calculate the valid pitch classes (0-11) for this scale
    valid_pitch_classes = set((root_val + interval) % 12 for interval in formula)

    positions = []

    # Iterate over every possible position on the neck
    for string_idx in range(6):  # 0 to 5
        string_base_pitch = GUITAR_TUNING_INDICES[string_idx]

        for fret in range(max_fret + 1):
            current_pitch = (string_base_pitch + fret) % 12

            if current_pitch in valid_pitch_classes:
                positions.append((string_idx, fret))

    return positions
