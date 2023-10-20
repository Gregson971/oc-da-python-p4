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
