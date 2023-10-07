import random


class Match:
    """Match model"""

    def __init__(self, players_pair):
        """Match constructor"""
        self.player1 = players_pair[0]
        self.player1_score = 0
        self.player1_color = None
        self.player2 = players_pair[1]
        self.player2_score = 0
        self.player2_color = None

    def __repr__(self):
        """Better representation of a match object"""
        return f"{self.players}"


class MatchService:
    """MatchService class, used to interact with the data"""

    def assign_color(self):
        """Assign color to players"""
        if random.choice([True, False]):
            self.player1_color = "White"
            self.player2_color = "Black"
        else:
            self.player1_color = "Black"
            self.player2_color = "White"

    def get_match(self):
        """Get match players pair"""
        self.assign_color()
        return ([self.player1, self.player1_score], [self.player2, self.player2_score])
