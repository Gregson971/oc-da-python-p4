from tinydb import TinyDB, Query


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


class PlayerService:
    """PlayerService class, used to interact with the database"""

    def __init__(self):
        """PlayerService constructor, used to interact with the database"""

    def serialize_player(player):
        """Method to get a serialized player"""

        return {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "full_name": player.full_name,
            "birthdate": player.birthdate,
            "chess_id": player.chess_id,
            "rank": player.rank,
            "score": player.score,
            "opponents": player.opponents,
        }

    def deserialize_player(player):
        """Method to deserialize a player"""
        return Player(
            first_name=player["first_name"],
            last_name=player["last_name"],
            birthdate=player["birthdate"],
            chess_id=player["chess_id"],
            rank=player["rank"],
            score=player["score"],
            opponents=player["opponents"],
        )

    def save_player(player):
        """Method to create a player in the database"""
        players_bd = TinyDB("data/tournaments/players.json", sort_keys=True, indent=4, separators=(',', ': '))
        serialized_player = PlayerService.serialize_player(player)
        players_bd.insert(serialized_player)
        print("Player created successfully")

    def get_player(chess_id):
        """Method to get a player from the database"""
        players_bd = TinyDB("data/tournaments/players.json", sort_keys=True, indent=4, separators=(',', ': '))
        return players_bd.search(Query().chess_id == chess_id)

    def get_all_players():
        """Method to get all players from the database"""
        players_bd = TinyDB("data/tournaments/players.json", sort_keys=True, indent=4, separators=(',', ': '))
        return players_bd.all()

    def update_player(self, chess_id):
        """Method to update a player in the database"""
        players_bd = TinyDB("data/tournaments/players.json", sort_keys=True, indent=4, separators=(',', ': '))
        serialized_player = self.serialize_player()
        players_bd.update(serialized_player, Query().chess_id == chess_id)
        print("Player updated successfully")
