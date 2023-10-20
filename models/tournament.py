class Tournament:
    """Tournament class"""

    def __init__(
        self,
        name,
        location,
        description='',
        players: list = [],
        rounds: list = [],
        start_date=None,
        end_date=None,
        rounds_total=4,
        current_round=1,
    ):
        """Tournament constructor"""
        self.name = name
        self.location = location
        self.description = description
        self.rounds = rounds
        self.players = players
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_total = rounds_total
        self.current_round = current_round

    def __repr__(self):
        """Better representation of a tournament object"""
        return f"Tournament name: {self.name}, Location: {self.location}, Description: {self.description}"
