import random
from enum import IntEnum

game_result = None
user_action = None
computer_action = None

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: [GameAction.Paper, GameAction.Spock],
    GameAction.Paper: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Scissors: [GameAction.Rock, GameAction.Spock],
    GameAction.Lizard: [GameAction.Scissors, GameAction.Rock],
    GameAction.Spock: [GameAction.Paper, GameAction.Lizard]

}

def assess_game(user_action, computer_action):

    global game_result

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Lizard:
            print("Rock crushes lizard. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Paper:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Spock:
            print("Spock vaporizes rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock:
            print("Papel disaproves Spock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Scissors:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Lizard:
            print("Lizard eats paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Spock:
            print("Spock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Paper:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Lizard:
            print("Scissors decapitates lizard. You won!")
            game_result = GameResult.Victory


    # You picked Lizard
    elif user_action == GameAction.Lizard:
        if computer_action == GameAction.Scissors:
            print("Scissors decapitates lizard. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Rock:
            print("Rock crushes lizard. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Paper:
            print("Lizard eats paper. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock:
            print("Lizard poisons Spock. You won!")
            game_result = GameResult.Victory

    # You picked Spock
    elif user_action == GameAction.Spock:
        if computer_action == GameAction.Paper:
            print("Papel disaproves Spock. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Lizard:
            print("Lizard poisons Spock. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Rock:
            print("Spock vaporizes rock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Scissors:
            print("Spock smashes scissors. You won!")
            game_result = GameResult.Victory

    return game_result


def get_computer_action():

    global game_result
    global user_action
    global computer_action

    # Computer picks Paper to start
    if game_result == None:
        computer_selection = 1

    # If computer won, computer picks last action the user picked
    elif game_result == GameResult.Defeat:
        computer_selection = user_action.value

    # If computer lost, computer picks the action that did not show up
    elif game_result == GameResult.Victory:
        was_not_picked = [action.value for action in GameAction if action not in [computer_action, user_action]]
        computer_selection = GameAction(was_not_picked[(random.randint(0, len(was_not_picked) - 1))])

    # If it is a Draw game, computer picks random action
    elif game_result == GameResult.Tie:
        computer_selection = random.randint(0, len(GameAction) - 1)

    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    global user_action
    global computer_action
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():
    while True:

        try:
            get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()