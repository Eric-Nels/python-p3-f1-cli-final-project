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
    id_ = input("Enter the team's id: ")
    if team := Team.find_by_id(id_):
        team.delete()
        print(f'Team {id_} deleted')
    else:
        print(f'Team {id_} not found')

def list_teams():
    teams = Team.get_all()
    for team in teams:
        print(team)

def list_team_drivers():
    team_name = input("Enter the Team name: ")
    team = Team.find_by_name(team_name)
    team_id = team.id
    drivers = Driver.get_all()
    for driver in drivers:
        if driver.team_id == team_id:
            print(driver.name, driver.driver_role)

def find_team_by_location():
    location = input("Enter the location: ")
    teams = Team.get_all()
    for team in teams:
        if team.location == location:
            print(team.name)

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