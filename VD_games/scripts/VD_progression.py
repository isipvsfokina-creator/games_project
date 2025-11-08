import random
from VD_games.scripts.VD_main import run_game


def generate_progression(start, step, length):
    """Создает арифметическую прогрессию"""
    return [start + i * step for i in range(length)]


def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(2, 10)
    length = random.randint(5, 10)

    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))
    return question, correct_answer


def main():
    description = 'What number is missing in the progression?'
    run_game(description, get_question_and_answer)


if __name__ == '__main__':
    main()
