import random
elements = ["rock", "paper", "scissors", "lizard", "spock"]
elements_list = "(rock paper scissors lizard spock)?"


def choose_element():
    player_element = input(f"Make your choose {elements_list}\n>>>  ").lower()
    pc_element = random.choice(elements)
    if player_element not in elements:
        print(f"invalid input {player_element}")
        choose_element()
    else:
        if player_element == pc_element:
            print(f"Player: {player_element}\nComputer: {pc_element}\nDraw")

        if player_element == "scissors":
            if pc_element == "spock" or pc_element == "rock":
                print(f"Player: {player_element}\nComputer: {pc_element}\nComputer WIN!")
            elif pc_element == "paper" or pc_element == "lizard":
                print(f"Player: {player_element}\nComputer: {pc_element}\nPlayer WIN!")

        elif player_element == "paper":
            if pc_element == "scissors" or pc_element == "lizard":
                print(f"Player: {player_element}\nComputer: {pc_element}\nComputer WIN!")
            elif pc_element == "rock" or pc_element == "spock":
                print(f"Player: {player_element}\nComputer: {pc_element}\nPlayer WIN!")

        elif player_element == "rock":
            if pc_element == "paper" or pc_element == "spock":
                print(f"Player: {player_element}\nComputer: {pc_element}\nComputer WIN!")
            elif pc_element == "scissors" or pc_element == "lizard":
                print(f"Player: {player_element}\nComputer: {pc_element}\nPlayer WIN!")

        elif player_element == "lizard":
            if pc_element == "rock" or pc_element == "scissors":
                print(f"Player: {player_element}\nComputer: {pc_element}\nComputer WIN!")
            elif pc_element == "paper" or pc_element == "spock":
                print(f"Player: {player_element}\nComputer: {pc_element}\nPlayer WIN!")

        elif player_element == "spock":
            if pc_element == "paper" or pc_element == "lizard":
                print(f"Player: {player_element}\nComputer: {pc_element}\nComputer WIN!")
            elif pc_element == "scissors" or pc_element == "rock":
                print(f"Player: {player_element}\nComputer: {pc_element}\nPlayer WIN!")


choose_element()