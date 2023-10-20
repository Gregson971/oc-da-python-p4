class Player:
    """Player class, used to create a player object"""

    def __init__(self, first_name, last_name, birthdate, chess_id, rank=0, score=0, opponents=[]):
        """Player constructor, used to create a player object"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.birthdate = birthdate
        self.chess_id = chess_id
        self.rank = rank
        self.score = score
        self.opponents = opponents

    def __repr__(self):
        """Better representation of a player object"""
        return f"Name: {self.full_name}, Score: {self.score}, Rank: {self.rank}"
