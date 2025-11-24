# French Touch Music Theory Tools

A Python-based visualization toolkit for learning Guitar and Piano theory simultaneously, with a specific focus on French Touch, Disco, and House music styles.

## 🎯 Goal

To generate high-quality, printable visual aids (Matplotlib charts) comparing Piano voicings and Guitar fretboard shapes, bridging the gap between International notation (A, B, C) and French Solfège (La, Si, Do).

## 🛠 Project Structure

- `src/constants.py`: Single Source of Truth for Notes, Tuning, and Colors.
- `src/utils.py`: Logic for note calculation (`fret_to_note`) and translation (`get_dual_lang_label`).
- `src/visualizer.py`: Rendering engine for Piano and Guitar charts.

## 🚀 Usage

### Installation

```bash
pip install -r requirements.txt
```
