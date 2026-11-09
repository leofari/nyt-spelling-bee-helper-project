# NYT Spelling Bee Helper

Python script that scrapes today's New York Times Spelling Bee puzzle
and finds all valid words from a word list.

This is my final project for the introduction to programming class I took freshman year.  
The assignment required coding everything from scratch (we were mostly prohibited from using built-in methods).

## Installation

```bash
pip install -r requirements.txt

```
# Usage
```
python3 spelling_bee_helper.py \
  --wordlist words_alpha.txt \
  --output-dir results
```

# Example output (from 5/4/24)
```
4:
['cive', 'deve', 'devi', 'dive', 'divi', 'even', 'give', 'i...'vein', 'vend', 'vice', 'vide', 'vied', 'viii', 'vine', 'vive']
5:
['civic', 'civie', 'dived', 'divid', 'evene', 'given', 'giv... 'venin', 'viced', 'vince', 'vinci', 'vined', 'vinic', 'vivid']
6:
['cevine', 'devein', 'device', 'devide', 'divide', 'divine'...d', 'venice', 'venine', 'vicine', 'vicing', 'vignin', 'vining']
7:
['deceive', 'divided', 'divined', 'divvied', 'envined', 'ev...ndivid', 'invivid', 'veining', 'vending', 'venging', 'vivendi']
8:
['deceived', 'deveined', 'dividend', 'dividing', 'divining', 'evidence', 'evincing', 'evincive', 'ingiving']
9:
['deceiving', 'deveining', 'evidenced', 'genevieve', 'individed']
10:
['evidencing', 'evidencive', 'inevidence']

Pangrams:
['deceiving', 'evidencing']
```
