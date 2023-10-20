from datetime import datetime

from models.tournament import Tournament
from models.player import Player

from services.player_service import PlayerService

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

        birthdate = None
        while not birthdate:
            birthdate_string = player_informations["birthdate"]
            try:
                datetime.strptime(birthdate_string, "%d-%m-%Y")
                birthdate = birthdate_string
                if len(birthdate) != 10 or birthdate[2] != "-" or birthdate[5] != "-":
                    self.view.display_message(message="Invalid birthdate format. Please use DD-MM-YYYY format.")
                    birthdate = None
            except ValueError:
                self.view.display_message(message="Please enter a valid date in format DD-MM-YYYY.")
                break

        chess_id = None
        while not chess_id:
            chess_id_str = player_informations["chess_id"]
            if len(chess_id_str) != 7:
                self.view.display_message(
                    message="Invalid chess ID format. Please use 2 letters followed by 5 digits."
                )
                break
            if not chess_id_str[:2].isalpha() or not chess_id_str[2:].isdigit():
                self.view.display_message(
                    message="Invalid chess ID format. Please use 2 letters followed by 5 digits."
                )
                break
            chess_id = chess_id_str

        if not first_name or not last_name or not birthdate or not chess_id:
            self.view.display_message(message="Please enter valid informations.")
            return

        new_player = Player(first_name, last_name, birthdate, chess_id)
        self.tournament.players.append(new_player)

        PlayerService.save_player(new_player)

    def load_players(self):
        """Load players from the database"""
        players = PlayerService.get_all_players()

        for player in players:
            new_player = PlayerService.deserialize_player(player)
            self.tournament.players.append(new_player)

        self.view.display_message(message="All players have been loaded.")
