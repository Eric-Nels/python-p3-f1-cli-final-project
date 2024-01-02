Formula 1 CLI
Description:

The Formula 1 CLI is a command-line interface connected to a database containing information about current Formula 1 drivers and teams. Users can access and manipulate data, including adding new drivers and teams or removing existing database objects.

Installation:

1. Navigate to the program file in your terminal.

2. Install pipenv if not already installed

3. Seed the database by running: python lib/seed.py

4. Run the program: python lib/cli.py

Code Structure
The program is organized into the following files:

- models
-- __init__.py: Database connection initialization.

-- driver.py: Definition of the Driver class and related database operations.

-- team.py: Definition of the Team class and related database operations.

- cli.py: Main CLI interface with user menu and options.

- helpers.py: Helper functions for various CLI actions.

- seed.py: Script to initialize and seed the database with sample data.

Usage
The CLI provides the following options:

- Create, delete, and display information about teams and drivers.
- View drivers associated with a specific team.
- Find teams based on location.
- Seed the database with sample data.

Author
Eric Nelson

Acknowledgments
Thanks to sqlite3