class MenuView:
    def display_welcome_message(self):
        """Display welcome message"""
        print(
            "-------------------------\n"
            "Welcome to Chess Tournament Manager\n"
            "-------------------------\n"
            "What do you want to do?\n"
            "-------------------------\n"
            "1. Create a tournament\n"
            "2. Load a tournament\n"
            "3. Create a player\n"
            "4. See reports\n"
            "5. Exit\n"
            "-------------------------"
        )
        return input("Choice: ")

    def display_create_player(self):
        """Display create player"""
        print(
            "-------------------------\n"
            "What do you want to do?\n"
            "1. Create a player\n"
            "2. Load players\n"
            "3. Save and quit\n"
            "-------------------------"
        )
        return input("Choice: ")

    def create_tournament(self):
        """Display create tournament"""
        print("-------------------------\n" "Create a tournament\n" "-------------------------")
        name = input("Name: ")
        location = input("Location: ")
        description = input("Description: ")
        return {"name": name, "location": location, "description": description}

    def create_player(self):
        """Display create player"""
        print("-------------------------\n" "Create a player\n" "-------------------------")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        birthdate = input("Birthdate: ")
        chess_id = input("Chess ID: ")
        return {"first_name": first_name, "last_name": last_name, "birthdate": birthdate, "chess_id": chess_id}

    def display_start_round_choice(self):
        """Display start round choice"""
        print("-------------------------\n" "What do you want to do?\n" "-------------------------")
        print("1. Start a round\n" "2. Load a round\n" "3. Save and quit\n" "-------------------------")
        return input("Choice: ")

    def display_round_winner(self, players):
        """Get winning player"""
        player1_name = players[0].full_name
        player2_name = players[1].full_name
        print(
            "-------------------------\n"
            "Who is the winner?\n"
            f"1. {player1_name}\n"
            f"2. {player2_name}\n"
            "3. A draw\n"
            "-------------------------"
        )
        return input("Winning player: ")

    def display_end_tournament(self):
        """Display end tournament"""
        print("-------------------------\n" "End a tournament\n" "Here is the results:\n" "-------------------------")

    def display_load_tournament(self):
        """Display load tournament"""
        print("-------------------------\n" "Load a tournament\n" "-------------------------")

    def display_start_tournament(self):
        """Display start tournament"""
        print("-------------------------\n" "Start a tournament\n" "-------------------------")

    def display_report(self):
        """Display report"""
        print("-------------------------\n" "Report\n" "-------------------------")

    def display_exit(self):
        """Display exit"""
        print("-------------------------\n" "Exit\n" "-------------------------")

    def display_winner(self):
        """Display winner"""
        print("-------------------------")
        print("Winner")
        print("-------------------------")

    def get_should_continue_adding_players(self):
        """Get should continue adding players"""
        choise = input("Do you want to add a player? (y/n): ")
        if choise == "y":
            return True
        else:
            return False
