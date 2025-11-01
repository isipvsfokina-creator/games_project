"""Calculator game."""

import random

GAME_RULES = "What is the result of the expression?"

def generate_round():
    """Generate a round for the calculator game."""
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{a} {operator} {b}"
    
    if operator == '+':
        correct_answer = str(a + b)
    elif operator == '-':
        correct_answer = str(a - b)
    else:  # operator == '*'
        correct_answer = str(a * b)
    
    return question, correct_answer
