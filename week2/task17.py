
secret_number = 7
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if attempts == max_attempts and guess != secret_number:
    print("Game Over!")
