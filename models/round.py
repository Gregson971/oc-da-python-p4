from models.match import MatchService


class Round:
    """Round model"""

    def __init__(self, name, matches: list):
        """Round constructor"""
        self.name = name
        self.matches = matches
        self.start_date = None
        self.end_date = None

    def __repr__(self):
        """Better representation of a round object"""
        return f"Round: {self.name}, Matches: {self.matches}"


class RoundService:
    """RoundService class, used to interact with the data"""

    def __init__(self, round):
        """RoundService constructor, used to interact with the data"""
        self.round = round

    def get_serialized_round(self):
        """Method to get a serialized round"""
        serialized_matches = []
        for match in self.round.matches:
            serialized_match = MatchService(match).get_serialized_match()
            serialized_matches.append(serialized_match)

        return {
            "name": self.round.name,
            "matches": serialized_matches,
            "start_date": self.round.start_date,
            "end_date": self.round.end_date,
        }
