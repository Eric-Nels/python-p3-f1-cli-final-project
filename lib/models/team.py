class Team:
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location