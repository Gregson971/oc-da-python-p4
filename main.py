# Description: Main file of the application

from controllers.main_controller import MainController
from views.menu_view import MenuView


def main():
    """Main function"""
    menu_view = MenuView()
    main_controller = MainController(menu_view)
    main_controller.run()


if __name__ == "__main__":
    main()
