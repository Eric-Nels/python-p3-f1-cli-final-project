#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.driver import Driver
from models.team import Team

def seed_database():
    Driver.drop_table()
    Team.drop_table()
    Team.create_table()
    Driver.create_table()

    Alfa_Romeo = Team.create("Alfa Romeo", "Switzerland")
    AlphaTauri = Team.create("AlphaTauri", "Italy")
    Alpine = Team.create("Alpine", "France")
    Aston_Martin = Team.create("Aston Martin", "United Kingdom")
    Ferrari = Team.create("Ferrari", "Italy")
    Haas = Team.create("Haas", "United Sates")
    McLaren = Team.create("McLaren", "United Kingdom")
    Mercedes = Team.create("Mercedes", "Germany")
    Red_Bull = Team.create("Red Bull", "Austria")
    Williams = Team.create("Williams", "United Kingdom")

    Driver.create("Valtteri Bottas", "Driver 1", Alfa_Romeo.id)
    Driver.create("Zhou Guanyu", "Driver 2", Alfa_Romeo.id)
    Driver.create("Daniel Ricciardo", "Driver 1", AlphaTauri.id)
    Driver.create("Yuki Tsunoda", "Driver 2", AlphaTauri.id)
    Driver.create("Esteban Ocon", "Driver 1", Alpine.id)
    Driver.create("Pierre Gasly", "Driver 2", Alpine.id)
    Driver.create("Fernando Alonso", "Driver 1", Aston_Martin.id)
    Driver.create("Lance Stroll", "Driver 2", Aston_Martin.id)
    Driver.create("Charles Leclerc", "Driver 1", Ferrari.id)
    Driver.create("Carlos Sainz Jr.", "Driver 2", Ferrari.id)
    Driver.create("Kevin Magnussen", "Driver 1", Haas.id)
    Driver.create("Nico Hülkenberg", "Driver 2", Haas.id)
    Driver.create("Lando Norris", "Driver 1", McLaren.id)
    Driver.create("Oscar Piastri", "Driver 2", McLaren.id)
    Driver.create("Lewis Hamilton", "Driver 1", Mercedes.id)
    Driver.create("George Russell", "Driver 2", Mercedes.id)
    Driver.create("Max Verstappen", "Driver 1", Red_Bull.id)
    Driver.create("Sergio Pérez", "Driver 2", Red_Bull.id)
    Driver.create("Alexander Albon", "Driver 1", Williams.id)
    Driver.create("Logan Sargeant", "Driver 2", Williams.id)
    Driver.create("Liam Lawson", "Reserve", Red_Bull.id)
    Driver.create("Felipe Drugovich", "Reserve", Aston_Martin.id)
    Driver.create("Theo Pourchaire", "Reserve", Alfa_Romeo.id)
    Driver.create("Antonio Giovinazzi", "Reserve", Ferrari.id)
    Driver.create("Alex Palou", "Reserve", McLaren.id)
    Driver.create("Mick Schumacher", "Reserve", Mercedes.id)
    Driver.create("Jack Doohan", "Reserve", Alpine.id)
    Driver.create("Pietro Fittipaldi", "Reserve", Haas.id)

seed_database()
print("Seeded database")