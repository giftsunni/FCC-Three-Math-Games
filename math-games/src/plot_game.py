import matplotlib.pyplot as plt
import random

def scatter_plot_game():
    points = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(5)]
    plt.scatter(*zip(*points))
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.show()
    
    for point in points:
        x, y = map(int, input(f"Enter coordinates for point {point}: ").split(','))
        if (x, y) == point:
            print("Correct!")
        else:
            print(f"Wrong! The correct coordinates were {point}")

if __name__ == "__main__":
    scatter_plot_game()