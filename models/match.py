class Match:
    """Match model"""

    def __init__(self, player_pairs):
        """Match constructor"""
        self.player1 = player_pairs[0]
        self.player2 = player_pairs[1]

    def __repr__(self):
        """Better representation of a match object"""
        return f"Match: {self.player1.full_name} vs {self.player2.full_name}"
