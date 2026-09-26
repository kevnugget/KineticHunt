# KineticHunt

A simple word hunt (Boggle-style) solver. Given a grid of letters, it finds every valid word that can be made by connecting adjacent letters (including diagonals), and prints them sorted from highest to lowest score.

## Requirements

- Python 3.12.3
- Tested on Windows 11 Pro 10.0.26200

## Setup

The dictionary file (`words.txt`) is already included in this repo, so no setup is required.

## Usage

Run from the project folder:

```
python word_hunt_solver.py words.txt "<board rows>"
```

The board is given as comma-separated rows of letters. For example, a 4x4 board:

```
c h a s
r e e t
o l d n
g i m a
```

is passed as:

```
python word_hunt_solver.py words.txt "chas,reet,oldn,gima"
```

To also save the results to a file, pass an output path as a third argument:

```
python word_hunt_solver.py words.txt "chas,reet,oldn,gima" results.txt
```

## How it works

- `words.txt` is loaded into a trie (prefix tree) for fast lookups.
- Starting from every cell on the board, a depth-first search walks to adjacent cells (including diagonals), without reusing a cell, checking the trie at each step to prune paths that can't form a word.
- Every valid word found is scored by length (matching typical Word Hunt scoring) and printed from highest to lowest score.
