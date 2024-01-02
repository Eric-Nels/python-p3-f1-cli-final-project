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
    