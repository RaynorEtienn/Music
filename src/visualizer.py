"""
src/visualizer.py
Unified rendering engine with Functional Coloring.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.gridspec import GridSpec
from typing import List, Tuple, Optional
from src.utils import get_dual_lang_label, fret_to_note, note_to_int, get_note_color
from src.constants import COLORS, CHROMATIC_SCALE


def _draw_piano_on_ax(ax, active_semitones: List[int], root_val: Optional[int] = None):
    """Draws piano with functional coloring if root_val is provided."""

    # ... (Garder la logique de mapping Octave/Keys identique à avant) ...
    OCTAVE_PATTERN = [0, 2, 4, 5, 7, 9, 11]
    white_key_chromatic_map = []
    for oct_idx in range(2):
        for val in OCTAVE_PATTERN:
            white_key_chromatic_map.append(val + (oct_idx * 12))

    white_note_names = ["C", "D", "E", "F", "G", "A", "B"] * 2

    # --- WHITE KEYS ---
    for i in range(14):
        chromatic_val = white_key_chromatic_map[i]
        is_active = chromatic_val in active_semitones

        # COLOR LOGIC
        if is_active:
            if root_val is not None:
                # On utilise modulo 12 pour comparer la "couleur" (pitch class)
                face_color = get_note_color(root_val, chromatic_val)
            else:
                face_color = COLORS["default"]
        else:
            face_color = COLORS["white_key"]

        rect = patches.Rectangle(
            (i, 0), 1, 1, linewidth=1, edgecolor="black", facecolor=face_color
        )
        ax.add_patch(rect)

        if is_active:
            note_name = white_note_names[i]
            label_text = get_dual_lang_label(note_name)
            # Text color adapts: White text if background is dark (Root/5th), Black otherwise
            text_col = (
                COLORS["text_light"]
                if face_color in [COLORS["root"], COLORS["fifth"], COLORS["seventh"]]
                else COLORS["text_main"]
            )
            ax.text(
                i + 0.5,
                0.2,
                label_text,
                ha="center",
                fontsize=8,
                weight="bold",
                color=text_col,
            )

    # --- BLACK KEYS ---
    black_visual_offsets = [0.6, 1.7, 3.6, 4.7, 5.8]
    black_chromatic_offsets = [1, 3, 6, 8, 10]

    for oct_idx in range(2):
        base_chromatic = oct_idx * 12
        base_visual = oct_idx * 7

        for v_offset, c_offset in zip(black_visual_offsets, black_chromatic_offsets):
            chromatic_val = base_chromatic + c_offset
            visual_pos = base_visual + v_offset

            is_active = chromatic_val in active_semitones

            if is_active:
                if root_val is not None:
                    face_color = get_note_color(root_val, chromatic_val)
                else:
                    face_color = COLORS["default"]
            else:
                face_color = COLORS["black_key"]

            rect = patches.Rectangle(
                (visual_pos, 0.4),
                0.6,
                0.6,
                linewidth=1,
                edgecolor="black",
                facecolor=face_color,
            )
            ax.add_patch(rect)

            if is_active:
                note_name = CHROMATIC_SCALE[chromatic_val % 12]
                ax.text(
                    visual_pos + 0.3,
                    0.55,
                    note_name,
                    ha="center",
                    va="center",
                    color=COLORS["text_light"],
                    fontsize=7,
                    weight="bold",
                    rotation=90,
                )

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title("Piano Voicing", fontsize=10, loc="left")


def _draw_guitar_on_ax(
    ax, string_states: List[Tuple[int, int]], root_val: Optional[int] = None
):
    """Draws guitar with functional coloring."""
    # ... (Strings & Frets drawing code remains same) ...
    for i in range(6):
        ax.plot([0, 12], [i, i], color="#999999", linewidth=1)
    for i in range(13):
        width = 3 if i == 0 else 1
        ax.plot([i, i], [-0.5, 5.5], color=COLORS["text_main"], linewidth=width)
        if i > 0:
            ax.text(i - 0.5, -0.8, str(i), ha="center", fontsize=7, color="#666666")

    # Notes
    for s_idx, fret in string_states:
        if fret == -1:
            ax.text(
                0.2,
                s_idx,
                "X",
                ha="center",
                va="center",
                color=COLORS["muted"],
                fontsize=12,
                weight="bold",
            )
        else:
            note_name = fret_to_note(s_idx, fret)
            current_note_val = note_to_int(note_name)

            # COLOR LOGIC
            if root_val is not None:
                dot_color = get_note_color(root_val, current_note_val)
            else:
                dot_color = COLORS["default"]

            label = get_dual_lang_label(note_name)

            if fret == 0:
                ax.plot(-0.3, s_idx, "o", color=dot_color, markersize=10)
                ax.text(
                    -1.8,
                    s_idx,
                    label.replace("\n", " "),
                    ha="right",
                    va="center",
                    fontsize=7,
                )
            else:
                ax.plot(fret - 0.5, s_idx, "o", color=dot_color, markersize=18)
                ax.text(
                    fret - 0.5,
                    s_idx,
                    note_name,
                    ha="center",
                    va="center",
                    color="white",
                    weight="bold",
                    fontsize=8,
                )

    string_names = ["E", "A", "D", "G", "B", "E"]
    for i, name in enumerate(string_names):
        ax.text(-2.8, i, name, ha="center", va="center", weight="bold", fontsize=9)

    ax.set_xlim(-3.5, 12.5)
    ax.set_ylim(-1, 6)
    ax.axis("off")
    ax.set_title("Guitar Fretboard", fontsize=10, loc="left")


def draw_sheet(
    title: str,
    description: str,
    piano_indices: List[int],
    guitar_states: List[Tuple[int, int]],
    root_note: Optional[str] = None,  # NEW PARAMETER
    save_path: Optional[str] = None,
):
    """
    Generates sheet. Pass root_note (e.g., 'C') to enable functional coloring.
    """

    root_val = None
    if root_note:
        root_val = note_to_int(root_note)

    fig = plt.figure(figsize=(10, 8), facecolor="white")
    gs = GridSpec(3, 1, height_ratios=[0.5, 1, 1.5], hspace=0.4)

    ax_header = fig.add_subplot(gs[0])
    ax_header.axis("off")
    ax_header.text(
        0.5,
        0.7,
        title,
        ha="center",
        va="center",
        fontsize=18,
        weight="bold",
        color=COLORS["text_main"],
    )
    ax_header.text(
        0.5,
        0.3,
        description,
        ha="center",
        va="center",
        fontsize=12,
        style="italic",
        color="#555555",
    )

    # Legend for colors (Optional but nice)
    if root_note:
        legend_text = "Couleurs : Rouge=Racine | Or=Tierce | Bleu=Quinte | Violet=7ème"
        ax_header.text(
            0.5, 0.0, legend_text, ha="center", va="center", fontsize=9, color="#777777"
        )

    ax_piano = fig.add_subplot(gs[1])
    _draw_piano_on_ax(ax_piano, piano_indices, root_val)

    ax_guitar = fig.add_subplot(gs[2])
    _draw_guitar_on_ax(ax_guitar, guitar_states, root_val)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)
        print(f"Sheet saved to {save_path}")

    plt.show()
