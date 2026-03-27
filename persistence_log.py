import os

FILE_NAME = "database.txt"


def add_blocker():
    """Prompt user input and append it to the file (Persistence)."""
    blocker = input("Enter your Daily Blocker: ").strip()

    if blocker:
        with open(FILE_NAME, "a") as file:
            file.write(blocker + "\n")
        print("✔ Blocker saved successfully.\n")
    else:
        print("⚠ Empty input. Nothing was saved.\n")


def fetch_blockers():
    """Read and display all blockers (Fetch operation)."""
    if not os.path.exists(FILE_NAME):
        print("⚠ File does not exist. Please add a blocker first.\n")
        return

    with open(FILE_NAME, "r") as file:
        blockers = file.readlines()

    if not blockers:
        print("ℹ No blockers found.\n")
        return

    print("\n--- Team Daily Blockers ---")
    for i, blocker in enumerate(blockers, start=1):
        print(f"{i}. {blocker.strip()}")
    print("----------------------------\n")


def reset_database():
    """Warn before overwriting the file."""
    if os.path.exists(FILE_NAME):
        confirm = input("⚠ Warning: This will overwrite all data. Continue? (yes/no): ").lower()

        if confirm == "yes":
            with open(FILE_NAME, "w") as file:
                file.write("")  # Overwrites file
            print("✔ Database reset successfully.\n")
        else:
            print("❌ Operation cancelled.\n")
    else:
        print("ℹ No file exists to overwrite.\n")


def main():
    """Main CLI menu."""
    while True:
        print("=== Team Daily Status ===")
        print("1. Add Blocker")
        print("2. Fetch Blockers")
        print("3. Reset Database")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_blocker()
        elif choice == "2":
            fetch_blockers()
        elif choice == "3":
            reset_database()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("⚠ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
