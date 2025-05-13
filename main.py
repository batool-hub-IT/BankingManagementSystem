# Function to display the main menu options
def show_menu():
    print("\n--- Simple Bank Menu ---")
    print("1. Create Account")
    print("2. View Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. View Last 5 Transactions")
    print("7. View Full Payment History")
    print("8. Exit")

# Infinite loop to keep showing the menu until user chooses to exit
while True:
    show_menu()  # Display the menu options
    choice = input("Choose an option (1-8): ")  # Get user input

    # Based on user input, display the appropriate message
    if choice == '1':
        print("-> Create Account selected.")
    elif choice == '2':
        print("-> View Balance selected.")
    elif choice == '3':
        print("-> Deposit Money selected.")
    elif choice == '4':
        print("-> Withdraw Money selected.")
    elif choice == '5':
        print("-> Transfer Money selected.")
    elif choice == '6':
        print("-> View Last 5 Transactions selected.")
    elif choice == '7':
        print("-> View Full Payment History selected.")
    elif choice == '8':
        print("Exiting... Goodbye!")  # Exit message
        break  # Exit the loop and end the program
    else:
        print("Invalid option. Please try again.")  # Handle invalid input

