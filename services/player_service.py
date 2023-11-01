from tinydb import TinyDB, Query

from models.player import Player


class PlayerService:
    """PlayerService class, used to interact with the database"""

    def serialize_player(player):
        """Method to get a serialized player"""
        if isinstance(player, dict):
            return player

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

    def update_player(player):
        """Method to update a player in the database"""
        players_bd = TinyDB("data/tournaments/players.json", sort_keys=True, indent=4, separators=(',', ': '))
        serialized_player = PlayerService.serialize_player(player)
        players_bd.update(serialized_player, Query().chess_id == player.chess_id)

    def reset_players(player):
        """Method to reset the players database"""
        players_bd = TinyDB("data/tournaments/players.json", sort_keys=True, indent=4, separators=(',', ': '))
        serialized_player = PlayerService.serialize_player(player)
        serialized_player.rank = 0
        serialized_player.score = 0
        serialized_player.opponents = []
        players_bd.update(serialized_player, Query().chess_id == player.chess_id)
