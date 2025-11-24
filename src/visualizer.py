"""
src/visualizer.py

Matplotlib rendering engine for generating Piano and Guitar charts.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import List, Tuple, Optional
from src.utils import get_dual_lang_label, fret_to_note
from src.constants import COLORS


def draw_piano_voicing(
    active_keys_indices: List[int],
    title: str = "Piano Voicing",
    save_path: Optional[str] = None,
):
    """
    Renders a 2-octave piano keyboard highlighting specific keys.
    active_keys_indices: 0=C3 ... 7=C4 ... 14=C5
    """
    fig, ax = plt.subplots(figsize=(10, 4))

    # White keys logic
    white_notes_base = ["C", "D", "E", "F", "G", "A", "B"]
    white_keys_labels = white_notes_base * 2

    for i in range(14):
        is_active = i in active_keys_indices
        face_color = COLORS["highlight_primary"] if is_active else COLORS["white_key"]

        rect = patches.Rectangle(
            (i, 0), 1, 1, linewidth=1, edgecolor="black", facecolor=face_color
        )
        ax.add_patch(rect)

        if is_active:
            label = get_dual_lang_label(white_keys_labels[i])
            ax.text(
                i + 0.5,
                0.2,
                label,
                ha="center",
                fontsize=9,
                weight="bold",
                color=COLORS["text_main"],
            )

    # Black keys logic
    black_offsets = [0.6, 1.7, 3.6, 4.7, 5.8]
    for octave in range(2):
        for offset in black_offsets:
            pos = (octave * 7) + offset
            rect = patches.Rectangle(
                (pos, 0.4),
                0.6,
                0.6,
                linewidth=1,
                edgecolor="black",
                facecolor=COLORS["black_key"],
            )
            ax.add_patch(rect)

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title(title, fontsize=14, pad=15)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()


def draw_guitar_chord(
    string_states: List[Tuple[int, int]],
    title: str = "Guitar Chord",
    save_path: Optional[str] = None,
):
    """
    Renders a guitar fretboard diagram.

    Args:
        string_states (List[Tuple[int, int]]):
            List of (string_index, fret_number).
            string_index: 0 (Low E) to 5 (High E).
            fret_number: -1 for mute, 0 for open, >0 for fretted.

            *Note: The function automatically calculates the Note Name.*
    """
    fig, ax = plt.subplots(figsize=(10, 4))

    # Draw Strings
    for i in range(6):
        ax.plot([0, 12], [i, i], color="gray", linewidth=1)

    # Draw Frets (0 to 12)
    for i in range(13):
        width = 3 if i == 0 else 1
        ax.plot([i, i], [-0.5, 5.5], color="black", linewidth=width)
        if i > 0:
            ax.text(i - 0.5, -0.8, str(i), ha="center", fontsize=8)

    # Draw Notes
    for s_idx, fret in string_states:

        if fret == -1:  # Muted
            ax.text(
                0.2,
                s_idx,
                "X",
                ha="center",
                va="center",
                color=COLORS["muted"],
                fontsize=14,
                weight="bold",
            )
        else:
            # Automatic Note Calculation
            note_name_en = fret_to_note(s_idx, fret)
            label = get_dual_lang_label(note_name_en)

            if fret == 0:  # Open String
                ax.plot(
                    -0.3, s_idx, "o", color=COLORS["highlight_primary"], markersize=12
                )
                ax.text(
                    -1.5,
                    s_idx,
                    label.replace("\n", " "),
                    ha="right",
                    va="center",
                    fontsize=8,
                )
            else:  # Fretted
                ax.plot(
                    fret - 0.5,
                    s_idx,
                    "o",
                    color=COLORS["highlight_primary"],
                    markersize=20,
                )
                # Simplified label inside dot (English only for readability inside the dot)
                ax.text(
                    fret - 0.5,
                    s_idx,
                    note_name_en,
                    ha="center",
                    va="center",
                    color="white",
                    weight="bold",
                    fontsize=9,
                )
                # Optional: French subtitle below/above could be added here

    # String Labels
    string_names = ["E", "A", "D", "G", "B", "E"]
    for i, name in enumerate(string_names):
        ax.text(-2.5, i, name, ha="center", va="center", weight="bold", fontsize=10)

    ax.set_xlim(-3, 12.5)
    ax.set_ylim(-1, 6)
    ax.axis("off")
    ax.set_title(title, fontsize=14)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()
