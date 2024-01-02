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

    def save(self):
        """ Insert a new row with the name, driver role, and team id values of the current Driver object.
        Update object id attribute using the primary key value of the new row.
        Save the object in the local dictionary using the table row's PK as the dictionary key"""
        sql = """
                INSERT INTO drivers (name, driver_role, team_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.driver_role, self.team_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Driver instance."""
        sql = """
            UPDATE drivers
            SET name = ?, driver_role = ?, team_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.driver_role, self.team_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Driver instance,
        delete the dictionary entry, and reassign the id attribute"""

        sql = """
            DELETE FROM drivers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None
    