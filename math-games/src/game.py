import matplotlib.pyplot as plt
import numpy as np

def projectile_game():
    wall_height = random.randint(5, 15)
    wall_position = random.randint(5, 15)
    
    def plot_trajectory(a, b, c):
        x = np.linspace(0, 20, 400)
        y = a * x**2 + b * x + c
        plt.plot(x, y)
        plt.axhline(y=wall_height, color='r', linestyle='-')
        plt.axvline(x=wall_position, color='r', linestyle='-')
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        plt.show()
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    plot_trajectory(a, b, c)

if __name__ == "__main__":
    projectile_game()