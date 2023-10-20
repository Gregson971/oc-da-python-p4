import sys
from datetime import datetime

from controllers.report_controller import ReportController
from controllers.round_controller import RoundController
from controllers.player_controller import PlayerController

from models.tournament import Tournament

from services.tournament_service import TournamentService

from views.menu_view import MenuView

PLAYER_PER_MATCH = 2


class TournamentController:
    def __init__(self, view: MenuView):
        self.view = view
        self.tournament = None

    def create_tournament(self):
        """Create a tournament"""
        tournament_informations = self.view.create_tournament()
        name = tournament_informations["name"]
        location = tournament_informations["location"]
        description = tournament_informations["description"]

        new_tournament = Tournament(name=name, location=location, players=[], rounds=[], description=description)
        self.tournament = new_tournament

        TournamentService.save_tournament(self.tournament)

        self.add_players()

    def get_tournament(self):
        """Get a tournament"""
        return self.tournament

    def load_tournament(self):
        """Load a tournament from the database"""
        user_input = input("Enter tournament name: ")
        new_tournament = TournamentService.get_tournament(name=user_input)

        if not new_tournament:
            print("Tournament not found.")
            return

        self.tournament = TournamentService.deserialize_tournament(new_tournament)

        print("Tournament loaded successfully.")

        self.add_players()

    def start_tournament(self):
        """Start the tournament"""
        print("-------------------------\n" "Start a tournament\n" "-------------------------")
        self.tournament.start_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        print(f"START TOURNAMENT DATE: {self.tournament.start_date}")

        # Run rounds
        for i in range(self.tournament.rounds_total):
            RoundController(self.view, self.tournament).start_round(i)

        self.tournament.end_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        print(f"END DATE: {self.tournament.end_date}")

        TournamentService.update_tournament(self.tournament)

        print("-------------------------\n" "End a tournament\n" "Here is the results:\n" "-------------------------")
        ReportController(self.view, self.tournament).handle_reports()

    def add_players(self):
        """Add players to the tournament"""
        create_player_choice = self.view.display_create_player()

        if create_player_choice == "1":
            PlayerController.create_player(self)
            while len(self.tournament.players) < self.tournament.rounds_total * PLAYER_PER_MATCH:
                create_player_choice = self.view.display_create_player()

                if create_player_choice == "1":
                    PlayerController.create_player(self)
                elif create_player_choice == "2":
                    PlayerController.load_players()
                elif create_player_choice == "3":
                    self.start_tournament()
                elif create_player_choice == "4":
                    TournamentService.update_tournament(self.tournament)
                    sys.exit()
                else:
                    pass

            if len(self.tournament.players) == self.tournament.rounds_total * PLAYER_PER_MATCH:
                print("All players have been added.")
                self.start_tournament()
            else:
                pass

        elif create_player_choice == "2":
            PlayerController.load_players(self)
            self.start_tournament()
        elif create_player_choice == "3":
            self.start_tournament()
        elif create_player_choice == "4":
            TournamentService.update_tournament(self.tournament)
            sys.exit()
        else:
            pass
