class MatchService:
    """MatchService class, used to interact with the data"""

    def serialize_match(match):
        """Method to get a serialized match"""
        return [
            [match.player1.full_name, match.player1.score],
            [match.player2.full_name, match.player2.score],
        ]
