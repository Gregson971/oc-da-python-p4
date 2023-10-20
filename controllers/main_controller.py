import sys

from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.report_controller import ReportController

from views.menu_view import MenuView


class MainController:
    def __init__(self, view: MenuView):
        self.view = view
        self.tournament = None

    def run(self):
        """Run the program"""

        welcome_choice = self.view.display_welcome_message()
        tournament_controller = TournamentController(self.view)

        if welcome_choice == "1":
            tournament_controller.create_tournament()
        elif welcome_choice == "2":
            tournament_controller.load_tournament()
        elif welcome_choice == "3":
            self.tournament = tournament_controller.get_tournament()
            report_controller = ReportController(self.view, self.tournament)
            report_controller.handle_reports()
        elif welcome_choice == "4":
            sys.exit()
        else:
            pass
