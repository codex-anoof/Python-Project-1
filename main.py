
from bank_operator.bank_operator import create_user, list_users, create_account

def main():
    while True:
        print("\n====== PyBank CLI Menu ======")
        print("1. Create User")
        print("2. List Users")
        print("3. Create Bank Account")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            create_user()
        elif choice == 2:
            list_users()
        elif choice == 3:
            create_account()
        elif choice == 4:
            print("👋 Exiting PyBank CLI. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose from 1 to 4.")

if __name__ == "__main__":
    main()
