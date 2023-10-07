from tinydb import TinyDB, Query


class Player:
    """Player class, used to create a player object"""

    def __init__(self, first_name, last_name, birthdate, chess_id):
        """Player constructor, used to create a player object"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.birthdate = birthdate
        self.chess_id = chess_id
        self.rank = 0
        self.score = 0
        self.tournament_score = 0
        self.opponents = []

    def __repr__(self):
        """Better representation of a player object"""
        return f"Name: {self.full_name}, Score: {self.score}, Rank: {self.rank}"


class PlayerService:
    """PlayerService class, used to interact with the database"""

    def __init__(self, player):
        """PlayerService constructor, used to interact with the database"""
        self.player = player
        self.players_bd = TinyDB("data/tournaments/players.json", sort_keys=True, indent=4, separators=(',', ': '))
        self.serialized_player = self.get_serialized_player()

    def get_serialized_player(self):
        """Method to get a serialized player"""
        return {
            "first_name": self.player.first_name,
            "last_name": self.player.last_name,
            "full_name": self.player.full_name,
            "birthdate": self.player.birthdate,
            "chess_id": self.player.chess_id,
            "rank": self.player.rank,
            "score": self.player.score,
            "tournament_score": self.player.tournament_score,
            "opponents": self.player.opponents,
        }

    def save_player(self):
        """Method to create a player in the database"""
        self.players_bd.insert(self.serialized_player)
        print("Player created successfully")

    def get_player(self, chess_id):
        """Method to get a player from the database"""
        self.players_bd.search(Query().chess_id == chess_id)

    def get_all_players(self):
        """Method to get all players from the database"""
        self.players_bd.all()

    def update_player(self, chess_id):
        """Method to update a player in the database"""
        self.players_bd.update(self.serialized_player, Query().chess_id == chess_id)
        print("Player updated successfully")
