from datetime import datetime

from models.tournament import Tournament
from models.player import Player

from services.player_service import PlayerService

from views.menu_view import MenuView

PLAYER_PER_MATCH = 2


class PlayerController:
    def __init__(self, view: MenuView, tournament: Tournament):
        self.view = view
        self.tournament = tournament

    def create_player(self):
        """Create a player"""
        player_informations = self.view.create_player()
        first_name = player_informations["first_name"]
        last_name = player_informations["last_name"]
        birthdate = self.validate_birthdate(player_informations["birthdate"])
        chess_id = self.validate_chess_id(player_informations["chess_id"])

        if not first_name or not last_name or not birthdate or not chess_id:
            self.view.display_message(message="Please enter valid informations.")
            return

        new_player = Player(first_name, last_name, birthdate, chess_id)
        self.tournament.players.append(new_player)

        PlayerService.save_player(new_player)

    def validate_birthdate(self, birthdate_string):
        """Validate birthdate"""
        while True:
            try:
                datetime.strptime(birthdate_string, "%d-%m-%Y")
                if len(birthdate_string) != 10 or birthdate_string[2] != "-" or birthdate_string[5] != "-":
                    self.view.display_message(message="Invalid birthdate format. Please use DD-MM-YYYY format.")
                else:
                    return birthdate_string
            except ValueError:
                self.view.display_message(message="Please enter a valid date in format DD-MM-YYYY.")
                return None

    def validate_chess_id(self, chess_id_str):
        """Validate chess ID"""
        while True:
            if len(chess_id_str) != 7:
                self.view.display_message(
                    message="Invalid chess ID format. Please use 2 letters followed by 5 digits."
                )
                return None
            if not chess_id_str[:2].isalpha() or not chess_id_str[2:].isdigit():
                self.view.display_message(
                    message="Invalid chess ID format. Please use 2 letters followed by 5 digits."
                )
                return None
            return chess_id_str

    def load_players(self):
        """Load players from the database"""
        players = PlayerService.get_all_players()

        for player in players:
            if len(self.tournament.players) < self.tournament.rounds_total * PLAYER_PER_MATCH:
                new_player = PlayerService.deserialize_player(player)
                self.tournament.players.append(new_player)

        self.view.display_message(message="All players have been loaded.")
