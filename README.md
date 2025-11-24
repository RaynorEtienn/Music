# French Touch Theory Visualizer

A Python-based visualization toolkit designed to bridge the gap between Piano and Guitar theory. This project generates high-resolution, printable "Cheat Sheets" comparing voicings on both instruments simultaneously. It features bilingual support (English/French) and functional interval coloring, optimized for the study of Funk, Disco, and House music.

## Project Architecture

The project is modular and separated into data, logic, and presentation layers.

```text
french_touch_theory/
│
├── README.md                 # Documentation
├── requirements.txt          # Dependencies
│
├── src/
│   ├── __init__.py           # Package initialization
│   ├── constants.py          # Single Source of Truth (Formulas, Tuning, Colors)
│   ├── utils.py              # Theory Logic (Interval calc, Fret scanning)
│   └── visualizer.py         # Matplotlib Rendering Engine (GridSpec, Coloring)
│
└── notebooks/
    └── 00_playground.ipynb   # User Interface / Scripting Area
```

## Installations

```bash
pip install -r requirements.txt
```

## Usage

The core function is `draw_sheet` located in `src/visualizer.py`. It generates a unified view of Piano keys and Guitar fretboard positions.

### Basic Example Script

```python
import sys
import os
# Ensure src is in the path
sys.path.append(os.path.abspath('../'))

from src.visualizer import draw_sheet
from src.utils import calculate_piano_indices, get_all_fretboard_positions

# 1. Configuration
ROOT = 'A'
MODE = 'Dorian'
TITLE = "A Dorian - French Touch Scale"
DESC = "Standard mode for Funk/House. Notice the raised 6th (F#) giving the 'Chic' sound."

# 2. Data Calculation
# Calculate absolute semitones for piano
piano_data = calculate_piano_indices(ROOT, MODE)
# Extend to 2 octaves for better visualization
piano_data_full = piano_data + [x + 12 for x in piano_data]

# Scan the guitar neck for all valid notes
guitar_data = get_all_fretboard_positions(ROOT, MODE)

# 3. Rendering
draw_sheet(
    title=TITLE,
    description=DESC,
    piano_indices=piano_data_full,
    guitar_states=guitar_data,
    root_note=ROOT,  # Enables Functional Coloring (Root=Red, 3rd=Gold, etc.)
    save_path="../output/A_Dorian_Sheet.png"
)
```

## Module Documentation

### `src/constants.py`

Contains the static data definitions:
- `CHROMATIC_SCALE`: List of notes used for calculation.
- `CHORD_FORMULAS`: Dictionary defining intervals for Chords (m7, Maj7, m9) and Modes (Dorian, Ionian, Pentatonics).
- `COLORS` & `INTERVAL_COLOR_MAP`: Hex codes defining the aesthetic. Functional colors (Root, 3rd, 5th, 7th) are defined here.

### `src/utils.py`

Handles the music theory logic:
- `calculate_piano_indices`: Converts a Root + Formula into absolute piano key indices.
- `get_all_fretboard_positions`: Scans the guitar fretboard to find all (string, fret) tuples matching a scale or chord.
- `fret_to_note`: Converts physical coordinates to note names.
- `get_note_color`: Determines the color of a note based on its interval relationship with the root.

### src/visualizer.py

Handles the graphical rendering using Matplotlib:
- `draw_sheet`: The main entry point. Uses `GridSpec` to layout the Header, Piano, and Guitar subplots.
- Functional Coloring: Dynamically colors keys and fret dots based on the `root_note` argument.

## Key Features

1. Bilingual Notation: Automatically displays International (A, B, C) and Solfège (La, Si, Do) names.
2. Functional Coloring:
    - Red: Root
    - Gold: Thirds (Major/Minor definition)
    - Blue: Fifth (Structure)
    - Purple: Seventh (Funk flavor)
    - Teal: Extensions (9, 11, 13)
3. Unified View: Allows direct comparison of linear harmony (Piano) vs geometric patterns (Guitar).

## Future Improvements & Roadmap

1. Chord Shape Library:
    - Currently, guitar chords (specific voicings) must be defined manually or by scanning the whole neck.
    - Goal: Implement a dictionary of standard "Funk Shapes" (e.g., `shapes['m7_root5']`) to automate specific voicing visualization.
2. Inversion Logic:
    - Improve `calculate_piano_indices` to handle specific inversions (1st, 2nd, 3rd) more strictly for chord generation, ensuring the bass note is correctly placed.
3. Export Formats:
    - Add PDF export support for high-quality printing of multiple scales in a single booklet.
4. Web Interface:
    - Wrap the library in a `Streamlit` or `Flask app` to allow interactive generation without code.
5. Audio Generation:
    - Use a simple synthesis library to generate a `.wav` file of the chord/scale being visualized to verify the sound.
