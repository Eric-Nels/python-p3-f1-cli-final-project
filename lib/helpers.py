# lib/helpers.py
from models.driver import Driver
from models.team import Team

def exit_program():
    print("Goodbye!")
    exit()

def create_team():
    name = input("Enter the Team's name: ")
    location = input("Enter the Team's location: ")
    try:
        team = Team.create(name, location)
        print(f'Success: {team}')
    except Exception as exc:
        print("Error creating team: ", exc)

def delete_team():
    pass

def list_teams():
    pass

def list_team_drivers():
    pass

def find_team_by_location():
    pass

def create_driver():
    pass

def delete_driver():
    pass

def list_drivers():
    pass

def list_driver_team():
    pass

def find_drivers_by_team_id():
    pass