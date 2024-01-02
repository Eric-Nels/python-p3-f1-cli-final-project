# lib/cli.py

from helpers import (
    exit_program,
    create_team,
    delete_team,
    list_teams,
    list_team_drivers,
    find_team_by_location,
    create_driver,
    delete_driver,
    list_drivers,
    list_driver_team,
    find_drivers_by_team_id
)    


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a Team")
    print("2. Delete a Team")
    print("3. Display all Teams")
    print("4. View Team drivers")
    print("5. Find Teams by location")
    print("6. Create a Driver")
    print("7. Delete a Driver")
    print("8. Display all Driver")
    print("9. View Drivers Team")
    print("10. Find Drivers by Team")


if __name__ == "__main__":
    main()