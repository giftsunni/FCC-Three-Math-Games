import random

def algebra_practice_game():
    for _ in range(5):
        a, b = random.randint(1, 10), random.randint(1, 10)
        answer = a + b
        user_answer = int(input(f"Solve: {a} + {b} = "))
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {answer}")

if __name__ == "__main__":
    algebra_practice_game()