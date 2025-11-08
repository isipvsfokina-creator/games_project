import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."

def get_question_and_answer():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    question = f"{a} {b}"
    correct_answer = str(math.gcd(a, b))
    return question, correct_answer
