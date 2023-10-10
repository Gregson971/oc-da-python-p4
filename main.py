# Description: Main file of the application

from controllers.tournament_controller import TournamentController
from views.menu_view import MenuView


def main():
    """Main function"""
    menu_view = MenuView()
    tournament_controller = TournamentController(menu_view)
    tournament_controller.run()


if __name__ == "__main__":
    main()
