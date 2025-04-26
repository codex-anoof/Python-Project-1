
from account.bank_account import BankAccount, SavingsAccount, StudentAccount, CurrentAccount
from account.user import User

users = []  # List to hold all created users
accounts = []  # List to hold all created accounts

def create_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    if '@' not in email or '.' not in email:
        print("Invalid email address!")
        return
    user = User(name, email)
    users.append(user)
    print("✅ User created successfully.")

def list_users():
    if not users:
        print("No users found.")
        return
    for index, user in enumerate(users):
        print(f"{index + 1}. {user.get_user_details()}")

def create_account():
    if len(users) == 0:
        print("No users available. Please create a user first.")
        return

    list_users()
    try:
        user_choice = int(input("Select a user by number: ")) - 1
        if user_choice < 0 or user_choice >= len(users):
            print("Invalid user selection.\n")
            return
    except ValueError:
        print("Invalid user selection.\n")
        return

    try:
        amount = float(input("Enter initial deposit amount: "))
    except ValueError:
        print("Invalid amount format.")
        return

    print("Choose account type:")
    print("1. Savings Account")
    print("2. Student Account")
    print("3. Current Account")

    try:
        account_choice = int(input("Enter choice (1-3): "))
    except ValueError:
        print("Invalid account type!")
        return

    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)
    else:
        print("Invalid account type!")
        return

    account.user = users[user_choice]
    accounts.append(account)
    print("✅ Account created successfully.")
