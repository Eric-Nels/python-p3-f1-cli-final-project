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
    