class Round:
    """Round model"""

    def __init__(self, name):
        """Round constructor"""
        self.name = name
        self.matches = []
        self.start_date = None
        self.end_date = None

    def __repr__(self):
        """Better representation of a round object"""
        return f"Round: {self.name}, Matches: {self.matches}"
