#!/usr/bin/env python3
"""Brain Calculator game."""

import sys
import os

# Добавляем путь к src в Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.brain_games.engine import run_game
from src.brain_games.games import calc

def main():
    """Run the calculator game."""
    run_game(calc)

if __name__ == "__main__":
    main()
