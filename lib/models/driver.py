from models.__init__ import CURSOR, CONN
from models.team import Team

class Driver:

    all = {}

    def __init__(self, name, driver_role, team_id, id=None):
        self.id = id
        self.name = name
        self.driver_role = driver_role
        self.team_id = team_id

    def __repr__(self):
        return (
            f"<Driver {self.id}: {self.name}, {self.driver_role}, " +
            f"Team ID: {self.team_id}>"
        )
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def driver_role(self):
        return self._driver_role

    @driver_role.setter
    def driver_role(self, driver_role):
        if isinstance(driver_role, str) and len(driver_role):
            self._driver_role = driver_role
        else:
            raise ValueError("driver_role must be a non-empty string")
        
    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        if type(team_id) is int and Team.find_by_id(team_id):
            self._team_id = team_id
        else:
            raise ValueError(
                "team_id must reference a team in the database")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Driver instances """
        sql = """
            CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            driver_role TEXT,
            team_id INTEGER,
            FOREIGN KEY (team_id) REFERENCES teams(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Driver instances """
        sql = """
            DROP TABLE IF EXISTS drivers;
        """
        CURSOR.execute(sql)
        CONN.commit()
    