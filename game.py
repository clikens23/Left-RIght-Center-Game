import random

players = []
MAX_PLAYERS = 8

def main():
    print("Are you ready to Left, Right, Center Game!")
    print("----------------------------------------------------")
    print("Let's play!!!")
    print("----------------------------------------------------")
    money = bet()
    print("We are betting $"+str(money)+ " per person")
    number_of_people = get_people()
    get_names(number_of_people)
    print("All names have been enter, let's play")
    run_game(players)
    winners_money = money * number_of_people
    print(f"You won, " + str(winners_money))

def get_people():
    while True:
        try:
            number_of_people = int(input("How many people are playing? (3-8) "))
            if 3 <= number_of_people <= MAX_PLAYERS:
                return number_of_people
        except ValueError:
            pass

def get_names(number_of_people):
    for name in range(number_of_people):
        name = input("Name: ").strip().title()
        players.append({"name": name, "chips": 3})

def bet():
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number. Number needs to be greater than 0")

    return amount

def run_game(players):
    chips = ["L", "R", "C", "🔴", "🔴", "🔴"]
    # any() returns TRUE if any of the players are iterable
    # any(player["chips"] > 0 for player in players):
    while True:
        for player in players:
            print(f"\n{player['name']}'s turn\n")
            if player["chips"] > 0:
                number_of_rolls = min(player["chips"], 3)
                rolls = []
                for _ in range(number_of_rolls):
                    action = random.choice(chips)
                    if action == "L":
                        left_player = players[(players.index(player) - 1) % len(players)]
                        left_player["chips"] += 1
                        rolls.append("L")
                    elif action == "R":
                        right_player = players[(players.index(player) + 1) % len(players)]
                        right_player["chips"] += 1
                        rolls.append("R")
                    elif action == "C":
                        player["chips"] -= 0
                        rolls.append("C")
                    elif action == "🔴":
                        player["chips"] += 1
                        rolls.append("🔴")
                    player["chips"] -= 1
                    #.join() takes all items in an iterable and joins into one string
                print(f"{player['name']} rolled: {', '.join(rolls)}")
            else:
                print(f"{player['name']} has no chips left. Skip turn.")
            print("\nCurrent chip counts:")
            for player in players:
                print(f"{player['name']}: {player['chips']}")
            print("----------------------------------------------------")
        remaining_players = [player for player in players if player["chips"] > 0]
        if len(remaining_players) == 1:  # Only one player remaining
            last_player = remaining_players[0]
            if "🔴" in rolls:  # Last player rolled dot, end the game
                print(f"{last_player['name']} rolled 'dot'. The game is over.")
                print(f"{last_player['name']} won!!! CONGRATS!!!!!!")
                print("----------------------------------------------------")
                return
            else:
                print(f"{last_player['name']} has to roll 'dot' to end the game.")
                continue

if __name__ == "__main__":
    main()