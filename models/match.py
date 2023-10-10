import random


class Match:
    """Match model"""

    def __init__(self, player_pairs):
        """Match constructor"""
        self.player1 = player_pairs[0]
        self.player1_score = 0
        self.player1_color = None
        self.player2 = player_pairs[1]
        self.player2_score = 0
        self.player2_color = None

    def __repr__(self):
        """Better representation of a match object"""
        return f"Match: {self.player1} vs {self.player2}"


class MatchService:
    """MatchService class, used to interact with the data"""

    def __init__(self, match):
        """MatchService constructor, used to interact with the data"""
        self.match = match

    def get_serialized_match(self):
        """Method to get a serialized match"""
        return [
            [self.match.player1.full_name, self.match.player1_score],
            [self.match.player2.full_name, self.match.player2_score],
        ]

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
        return ([self.match.player1.full_name, self.player1_score], [self.player2.full_name, self.player2_score])

    def update_match(self, player1_score, player2_score):
        """Update match score"""
        self.player1_score = player1_score
        self.player2_score = player2_score
        return ([self.player1, self.player1_score], [self.player2, self.player2_score])
