from models.tournament import Tournament
from models.player import Player, PlayerService

from views.menu_view import MenuView


class PlayerController:
    def __init__(self, view: MenuView, tournament: Tournament):
        self.view = view
        self.tournament = tournament

    def create_player(self):
        """Create a player"""
        player_informations = self.view.create_player()
        first_name = player_informations["first_name"]
        last_name = player_informations["last_name"]
        birthdate = player_informations["birthdate"]
        chess_id = player_informations["chess_id"]

        new_player = Player(first_name, last_name, birthdate, chess_id)
        self.tournament.players.append(new_player)

        PlayerService.save_player(new_player)

    def load_players(self):
        """Load players from the database"""
        players = PlayerService.get_all_players()

        for player in players:
            new_player = PlayerService.deserialize_player(player)
            self.tournament.players.append(new_player)

        print("All players have been loaded.")
