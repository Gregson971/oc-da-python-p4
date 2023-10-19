class Match:
    """Match model"""

    def __init__(self, player_pairs):
        """Match constructor"""
        self.player1 = player_pairs[0]
        self.player2 = player_pairs[1]

    def __repr__(self):
        """Better representation of a match object"""
        return f"Match: {self.player1.full_name} vs {self.player2.full_name}"


class MatchService:
    """MatchService class, used to interact with the data"""

    def serialize_match(match):
        """Method to get a serialized match"""
        return [
            [match.player1.full_name, match.player1.score],
            [match.player2.full_name, match.player2.score],
        ]
