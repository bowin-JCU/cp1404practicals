name = input("Enter your name: ")

def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

display_menu()

choice = input("Enter your choice: ")

while choice != 'q':
    if choice == 'h':
        print(f"Hello {name}")
    elif choice == 'g':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    display_menu()
    choice = input("Enter your choice: ")

print("Finished.")
