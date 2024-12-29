from scatter_plot_game import scatter_plot_game
from algebra_practice_game import algebra_practice_game
from projectile_game import projectile_game

def main():
    while True:
        print("Choose a game:")
        print("1. Scatter Plot Game")
        print("2. Algebra Practice Game")
        print("3. Projectile Game")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            scatter_plot_game()
        elif choice == '2':
            algebra_practice_game()
        elif choice == '3':
            projectile_game()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()