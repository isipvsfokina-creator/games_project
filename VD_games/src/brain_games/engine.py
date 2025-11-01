"""Game engine for Brain Games."""

def welcome_user():
    """Get user's name and welcome them."""
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def run_game(game_module, rounds=3):
    """
    Run a game with the specified game module.
    
    Args:
        game_module: Module containing generate_round() function
        rounds: Number of rounds to play
    """
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(game_module.GAME_RULES)
    
    for _ in range(rounds):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")
    
    print(f"Congratulations, {name}!")
