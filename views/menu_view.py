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
            "3. See reports\n"
            "4. Exit\n"
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
            "3. Start tournament\n"
            "4. Save and quit\n"
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
        print("1. Start a round\n" "3. Save and quit\n" "-------------------------")
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

    def display_report_choice(self):
        """Display report choice"""
        print("-------------------------\n" "What do you want to see?\n" "-------------------------")
        print(
            "1. Players in alphabetical order\n"
            "2. Players in rank order\n"
            "3. Tournaments list\n"
            "4. Tournament details\n"
            "5. Rounds and matches details by tournaments\n"
            "6. Exit\n"
            "-------------------------"
        )
        return input("Choice: ")
