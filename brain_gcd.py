#!/usr/bin/env python3
import sys
import os

# Добавляем VD_games в путь
sys.path.insert(0, os.path.dirname(__file__))

from VD_games.scripts.brain_gcd import main

if __name__ == "__main__":
    main()
