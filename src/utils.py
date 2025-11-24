"""
src/utils.py
Logic for notes, intervals, and chord calculation.
"""

from typing import List
from src.constants import (
    CHROMATIC_SCALE,
    GUITAR_TUNING_INDICES,
    NOTE_TRANSLATION,
    CHORD_FORMULAS,
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
    """Returns 'C\n(Do)'."""
    note_fr = NOTE_TRANSLATION.get(note_en, note_en)
    return f"{note_en}\n({note_fr})"


def fret_to_note(string_index: int, fret_number: int) -> str:
    """Returns the note name at a specific guitar position."""
    base = GUITAR_TUNING_INDICES[string_index]
    return CHROMATIC_SCALE[(base + fret_number) % 12]


def calculate_piano_indices(
    root_note: str, chord_type: str, inversion: int = 0
) -> List[int]:
    """
    Calculates ABSOLUTE SEMITONE INDICES relative to the starting C (C3).
    C3 = 0, C#3 = 1, ... C4 = 12 ...

    Args:
        root_note: 'C', 'A#', etc.
        chord_type: 'm7', 'Major', etc.
        inversion: 0, 1, 2...

    Returns:
        List[int]: List of absolute semitones to highlight (e.g., [9, 12, 16, 19] for Am7).
    """
    if chord_type not in CHORD_FORMULAS:
        raise ValueError(f"Chord type '{chord_type}' not defined.")

    root_val = note_to_int(root_note)  # 0-11
    formula = CHORD_FORMULAS[chord_type]  # e.g. [0, 3, 7, 10]

    # 1. Create base chord notes (Absolute semitones from C0)
    # We assume the root is in the first octave (0-11) initially
    chord_notes = [(root_val + interval) for interval in formula]

    # 2. Apply Inversion (Rotate lowest note up by 12 semitones)
    for _ in range(inversion):
        note = chord_notes.pop(0)
        chord_notes.append(note + 12)

    # 3. Normalize for Visualizer (Fit into the 2-octave window if possible)
    # The visualizer usually shows C3 (0) to B4 (23).
    # If the chord is too low or too high, we shift octaves.

    # Shift down if everything is high
    while min(chord_notes) >= 12:
        chord_notes = [n - 12 for n in chord_notes]

    # Shift up if we have negatives (shouldn't happen with logic above but safe)
    while min(chord_notes) < 0:
        chord_notes = [n + 12 for n in chord_notes]

    return chord_notes
