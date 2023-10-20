import sys

from tabulate import tabulate

from models.tournament import Tournament

from services.tournament_service import TournamentService
from services.player_service import PlayerService

from views.menu_view import MenuView


class ReportController:
    def __init__(self, view: MenuView, tournament: Tournament):
        self.view = view
        self.tournament = tournament

    def handle_reports(self):
        """Handle reports"""
        choice = self.view.display_report_choice()

        if choice == "1":
            self.display_players_alphabetically()
        elif choice == "2":
            self.display_players_by_ranking()
        elif choice == "3":
            self.display_tournaments_list()
        elif choice == "4":
            self.display_tournament_details()
        elif choice == "5":
            self.display_rounds_and_matches_details_by_tournaments()
        elif choice == "6":
            sys.exit()
        else:
            pass

    def display_players_alphabetically(self):
        """Display the list of players"""
        players = PlayerService.get_all_players()
        sorted_players = sorted(players, key=lambda player: player["first_name"])
        self.view.display_message(message=tabulate(sorted_players, headers="keys", tablefmt="fancy_grid"))

    def display_players_by_ranking(self):
        """Display the list of players"""
        players = PlayerService.get_all_players()
        sorted_players = sorted(players, key=lambda player: player["rank"])
        self.view.display_message(message=tabulate(sorted_players, headers="keys", tablefmt="fancy_grid"))

    def display_tournaments_list(self):
        """Display the list of tournaments"""
        tournaments = TournamentService.get_all_tournaments()
        clean_tournaments = [
            {key: value for key, value in element.items() if key not in ['players', 'rounds']}
            for element in tournaments
        ]
        self.view.display_message(message=tabulate(clean_tournaments, headers="keys", tablefmt="fancy_grid"))

    def display_tournament_details(self):
        """Display tournament details"""
        user_input = self.view.display_message(input_message="Enter tournament name: ")
        tournament = TournamentService.get_tournament(name=user_input)
        if tournament:
            deserialized_tournament = TournamentService.deserialize_tournament(tournament)
            self.view.display_message(
                message=f"Tournament name : {deserialized_tournament.name}\n"
                f"Start date : {deserialized_tournament.start_date}\n"
                f"End date : {deserialized_tournament.end_date}\n"
            )
        else:
            self.view.display_message(message="Tournament not found.")

    def display_rounds_and_matches_details_by_tournaments(self):
        """Display the list of tournaments"""
        user_input = input("Enter tournament name: ")
        tournament = TournamentService.get_tournament(name=user_input)
        if tournament:
            deserialized_tournament = TournamentService.deserialize_tournament(tournament)
            rounds = deserialized_tournament.rounds
            for round in rounds:
                self.view.display_message(message=f"Round : {round['name']}")
                matches = round['matches']
                for match in matches:
                    self.view.display_message(message=f"Match : {match[0][0]} vs {match[1][0]}")
        else:
            self.view.display_message(message="Tournament not found.")
