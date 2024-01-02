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
    name = input("Enter the driver's name: ")
    driver_role = input("Enter the driver's role: ")
    team_name = input("Enter the driver's team: ")
    team = Team.find_by_name(team_name)
    team_id = team.id
    try:
        driver = Driver.create(name, driver_role, team_id)
        print(f'Success: {driver}')
    except Exception as exc:
        print("Error creating driver: ", exc)

def delete_driver():
    name = input("Enter the driver's name: ")
    if driver := Driver.find_by_name(name):
        driver.delete()
        print(f'Driver {name} deleted')
    else:
        print(f'Driver {name} not found')

def list_drivers():
    drivers = Driver.get_all()
    for driver in drivers:
        print(driver)

def list_driver_team():
    name = input("Enter the driver's name: ")
    driver = Driver.find_by_name(name)
    teams = Team.get_all()
    for team in teams:
        if team.id == driver.team_id:
            print(f'{driver.name}, {team.name}')

def find_drivers_by_team_id():
    id_ = input("Enter the team's id: ")
    drivers = Driver.get_all()
    for driver in drivers:
        if driver.team_id == int(id_):
            print(driver.name, driver.driver_role)