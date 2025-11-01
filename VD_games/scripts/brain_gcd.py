#!/usr/bin/env python3
"""Brain GCD game."""

import sys
import os

# Добавляем путь к src в Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.brain_games.engine import run_game
from src.brain_games.games import gcd

def main():
    """Run the GCD game."""
    run_game(gcd)

if __name__ == "__main__":
    main()
