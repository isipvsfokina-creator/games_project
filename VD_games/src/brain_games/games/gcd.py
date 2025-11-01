"""Greatest Common Divisor game."""

import random

GAME_RULES = "Find the greatest common divisor of given numbers."

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def generate_round():
    """Generate a round for the GCD game."""
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    
    question = f"{a} {b}"
    correct_answer = str(gcd(a, b))
    
    return question, correct_answer
