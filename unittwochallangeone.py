lass BankApp:
    def __init__(self):
        self.users = {}  # {account_number: {"name": "", "address": "", "contact": "", "password": "", "balance": 0, "transactions": []}}
        self.logged_in_user = None

    def register(self):
        name = input("Enter your full name: ")
        address = input("Enter your address: ")
        contact = input("Enter your contact number: ")
        password = input("Enter a password: ")
        account_number = str(len(self.users) + 1).zfill(6)
        self.users[account_number] = {"name": name, "address": address, "contact": contact, "password": password, "balance": 0, "transactions": []}
        print(f"Registration successful! Your account number is {account_number}")

    def login(self):
        account_number = input("Enter your account number: ")
        password = input("Enter your password: ")
        if account_number in self.users and self.users[account_number]["password"] == password:
            self.logged_in_user = account_number
            print("Login successful!")
        else:
            print("Invalid account number or password.")

    def logout(self):
        self.logged_in_user = None
        print("Logged out successfully!")

    def dashboard(self):
        user = self.users[self.logged_in_user]
        print(f"Welcome, {user['name']}!")
        print(f"Balance: ${user['balance']}")
        print("Last 5 transactions: ", user["transactions"][-5:])

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.users[self.logged_in_user]["balance"] += amount
        self.users[self.logged_in_user]["transactions"].append(f"Deposited ${amount}")
        print(f"${amount} deposited successfully!")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= self.users[self.logged_in_user]["balance"]:
            self.users[self.logged_in_user]["balance"] -= amount
            self.users[self.logged_in_user]["transactions"].append(f"Withdrew ${amount}")
            print(f"${amount} withdrawn successfully!")
        else:
            print("Insufficient balance.")

    def transfer(self):
        recipient_account = input("Enter recipient account number: ")
        amount = float(input("Enter the amount to transfer: "))
        if recipient_account in self.users and amount <= self.users[self.logged_in_user]["balance"]:
            self.users[self.logged_in_user]["balance"] -= amount
            self.users[recipient_account]["balance"] += amount
            self.users[self.logged_in_user]["transactions"].append(f"Transferred ${amount} to {recipient_account}")
            self.users[recipient_account]["transactions"].append(f"Received ${amount} from {self.logged_in_user}")
            print(f"${amount} transferred successfully!")
        else:
            print("Invalid account or insufficient balance.")

    def run(self):
        while True:
            print("\n--- Banking App ---")
            print("1. Register")
            print("2. Login")
            print("3. Logout")
            print("4. Dashboard")
            print("5. Deposit")
            print("6. Withdraw")
            print("7. Transfer")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.logout()
            elif choice == "4":
                if self.logged_in_user:
                    self.dashboard()
                else:
                    print("Please log in first.")
            elif choice == "5":
                if self.logged_in_user:
                    self.deposit()
                else:
                    print("Please log in first.")
            elif choice == "6":
                if self.logged_in_user:
                    self.withdraw()
                else:
                    print("Please log in first.")
            elif choice == "7":
                if self.logged_in_user:
                    self.transfer()
                else:
                    print("Please log in first.")
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = BankApp()
    app.run()


