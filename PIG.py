import random


# Function to roll the dice
def roll():
    return random.randint(1, 6)


# Get number of players
while True:
    players = input("Enter the number of players (2-4): ")

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Invalid input! Please enter a number.")


max_score = 50
player_scores = [0 for _ in range(players)]


# Main Game Loop
while max(player_scores) < max_score:

    for player_idx in range(players):

        print("\n======================================")
        print(f"🎲 Player {player_idx + 1}'s Turn")
        print("======================================")
        print(f"Current Total Score: {player_scores[player_idx]}")

        current_score = 0

        while True:

            should_roll = input("\nRoll the dice? (y/n): ").lower()

            if should_roll == "n":
                print("You chose to stop rolling.")
                break

            elif should_roll != "y":
                print("Invalid input! Please enter y or n.")
                continue

            value = roll()

            print(f"You rolled a {value}.")

            if value == 1:
                print("Oops! You rolled a 1.")
                print("You lose all points earned this turn.")
                current_score = 0
                break

            current_score += value

            print(f"Current Turn Score: {current_score}")

        player_scores[player_idx] += current_score

        print(f"Total Score: {player_scores[player_idx]}")

        # Check if player has won
        if player_scores[player_idx] >= max_score:
            break


# Find Winner
winner_score = max(player_scores)
winner = player_scores.index(winner_score)

print("\n======================================")
print("🎉🎉 GAME OVER 🎉🎉")
print("======================================")

print(f"\n🏆 Congratulations Player {winner + 1}!")
print(f"You won the game with {winner_score} points!\n")

print("📊 Final Scores")
print("----------------------")

for i, score in enumerate(player_scores):
    print(f"Player {i + 1}: {score}")

print("\nThanks for playing! 😊")