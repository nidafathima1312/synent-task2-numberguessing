import random

# ANSI Colors for Terminal Styling
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def display_header():
    print(f"{CYAN}\n=============================================")
    print("      🎯 ULTIMATE NUMBER GUESSING GAME 🎯    ")
    print(f"============================================={RESET}")

def select_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy   (Range: 1-50,  Attempts: 10, Multiplier: 1x)")
    print("2. Medium (Range: 1-100, Attempts: 7,  Multiplier: 2x)")
    print("3. Hard   (Range: 1-500, Attempts: 5,  Multiplier: 3x)")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice == 1:
                return 50, 10, 1, "Easy"
            elif choice == 2:
                return 100, 7, 2, "Medium"
            elif choice == 3:
                return 500, 5, 3, "Hard"
            else:
                print(f"{YELLOW}⚠️ Invalid choice! Please enter 1, 2, or 3.{RESET}")
        except ValueError:
            print(f"{RED}⚠️ Invalid input! Please enter a whole number.{RESET}")

def play_round():
    max_range, max_attempts, multiplier, difficulty_label = select_difficulty()
    secret_number = random.randint(1, max_range)
    attempts_used = 0
    score = 100

    print(f"\n--- Starting {difficulty_label} Mode ---")
    print(f"I've picked a number between 1 and {max_range}. You have {max_attempts} attempts!")

    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        print(f"\nAttempts remaining: {remaining}")
        
        # Smart Bonus Clue when attempts are running low
        if remaining == 2:
            parity = "EVEN" if secret_number % 2 == 0 else "ODD"
            print(f"{YELLOW}💡 Bonus Clue: The secret number is {parity}!{RESET}")

        try:
            guess = int(input(f"Enter your guess (1-{max_range}): "))
        except ValueError:
            print(f"{RED}⚠️ Invalid input! Please enter a valid number.{RESET}")
            continue

        if guess < 1 or guess > max_range:
            print(f"{YELLOW}⚠️ Out of range! Please enter a number between 1 and {max_range}.{RESET}")
            continue

        attempts_used += 1

        if guess == secret_number:
            final_score = score * multiplier
            print(f"{GREEN}\n🎉 CONGRATULATIONS! You guessed it right!{RESET}")
            print(f"The number was: {secret_number}")
            print(f"Attempts used: {attempts_used}")
            print(f"Final Score   : {final_score} pts")
            return True, attempts_used, final_score

        elif guess < secret_number:
            print(f"{CYAN}📈 Too low! Try a higher number.{RESET}")
        else:
            print(f"{CYAN}📉 Too high! Try a lower number.{RESET}")

        score = max(0, score - 15)

    print(f"{RED}\n💥 GAME OVER! You ran out of attempts.{RESET}")
    print(f"The secret number was: {secret_number}")
    return False, attempts_used, 0

def main():
    display_header()
    
    total_games = 0
    total_wins = 0
    best_score = 0

    while True:
        total_games += 1
        won, attempts, score = play_round()

        if won:
            total_wins += 1
            if score > best_score:
                best_score = score

        print("\n" + "=" * 45)
        print("              GAME STATISTICS                ")
        print("=" * 45)
        print(f" Total Games Played : {total_games}")
        print(f" Games Won          : {total_wins}")
        print(f" Best Score         : {best_score} pts")
        print("=" * 45)

        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print(f"{GREEN}\nThanks for playing! See you next time! 👋{RESET}")
            break

if __name__ == "__main__":
    main()