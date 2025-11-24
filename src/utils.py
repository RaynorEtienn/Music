"""
src/utils.py

Helper functions for music theory logic and string formatting.
Handles the conversion between mathematical fretboard positions and human-readable notes.
"""

from typing import Tuple
from src.constants import CHROMATIC_SCALE, GUITAR_TUNING_INDICES, NOTE_TRANSLATION


def get_dual_lang_label(note_en: str) -> str:
    """
    Returns a formatted string with both English and French notation.
    Example Input: "C" -> Output: "C\n(Do)"
    """
    # Clean input (handle potential flat/sharp inconsistencies if needed later)
    note_fr = NOTE_TRANSLATION.get(note_en, note_en)
    return f"{note_en}\n({note_fr})"


def fret_to_note(string_index: int, fret_number: int) -> str:
    """
    Calculates the musical note name based on the string index and fret number.

    Args:
        string_index (int): 0 (Low E) to 5 (High E).
        fret_number (int): The fret number (0 for open).

    Returns:
        str: The English note name (e.g., "A#", "C").
    """
    if not (0 <= string_index <= 5):
        raise ValueError("String index must be between 0 and 5.")

    # 1. Get the base note index of the open string (e.g., Low E is index 4 in Chromatic Scale)
    base_note_index = GUITAR_TUNING_INDICES[string_index]

    # 2. Add the fret number to get the absolute semitone distance
    current_note_index = base_note_index + fret_number

    # 3. Modulo 12 to wrap around the chromatic scale
    final_note_index = current_note_index % 12

    return CHROMATIC_SCALE[final_note_index]


def get_interval_name(root_note: str, target_note: str):
    """
    Placeholder for future logic to calculate intervals (e.g., "m7", "P5").
    Useful for advanced diagrams later.
    """
    pass
