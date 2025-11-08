import random

DESCRIPTION = "What is the result of the expression?"

def get_question_and_answer():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        correct_answer = a + b
    elif operator == "-":
        correct_answer = a - b
    else:
        correct_answer = a * b

    question = f"{a} {operator} {b}"
    return question, str(correct_answer)
