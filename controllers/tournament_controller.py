import sys
from datetime import datetime
from tabulate import tabulate


from models.tournament import Tournament, TournamentService
from models.player import Player, PlayerService
from models.round import Round
from models.match import Match
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

        new_tournament = Tournament(name, location, [], [], description)
        self.tournament = new_tournament

        TournamentService.save_tournament(self.tournament)

        self.add_players()

    def add_players(self):
        """Add players to the tournament"""
        create_player_choice = self.view.display_create_player()

        if create_player_choice == "1":
            self.create_player()
            while len(self.tournament.players) < self.tournament.rounds_total * PLAYER_PER_MATCH:
                create_player_choice = self.view.display_create_player()

                if create_player_choice == "1":
                    self.create_player()
                elif create_player_choice == "2":
                    self.load_players()
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

        elif create_player_choice == "2":
            self.load_players()
            self.start_tournament()
        elif create_player_choice == "3":
            self.start_tournament()
        elif create_player_choice == "4":
            TournamentService.update_tournament(self.tournament)
            sys.exit()
        else:
            pass

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

    def load_tournament(self):
        """Load a tournament from the database"""
        new_tournament = TournamentService.get_tournament(name="Tournament 1")
        self.tournament = TournamentService.deserialize_tournament(new_tournament)

        print("Tournament loaded successfully.")

    def start_tournament(self):
        """Start the tournament"""
        print("-------------------------\n" "Start a tournament\n" "-------------------------")
        self.tournament.start_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        print(f"START TOURNAMENT DATE: {self.tournament.start_date}")

        # Run rounds
        for i in range(self.tournament.rounds_total):
            self.start_round(i)

        print("-------------------------\n" "End a tournament\n" "Here is the results:\n" "-------------------------")
        self.tournament.end_date = datetime.now().strftime("%d-%m-%Y %H:%M")
        print(f"END DATE: {self.tournament.end_date}")

        TournamentService.update_tournament(self.tournament)
        # self.show_result(self.tournament.players)

    def start_round(self, round_number):
        """Start the round"""
        choice = self.view.display_start_round_choice()
        if choice == "1":
            players_pairs = list(self.create_pair(self.tournament.players))

            matches = []
            for pair in players_pairs:
                match = Match(pair)
                matches.append(match)

            round = Round(f"Round {round_number + 1}", matches)
            self.tournament.rounds.append(round)

            print(f"CURRENT ROUND: {self.tournament.current_round}")

            # Start round
            self.tournament.rounds[round_number].start_date = datetime.now().strftime("%d-%m-%Y %H:%M")
            print(f"ROUND START DATE: {self.tournament.rounds[round_number].start_date}")

            for pair in players_pairs:
                self.get_round_winner(pair)

            # End round
            self.tournament.rounds[round_number].end_date = datetime.now().strftime("%d-%m-%Y %H:%M")
            print(f"ROUND END DATE: {self.tournament.rounds[round_number].end_date}")

            self.tournament.current_round += 1

        elif choice == "2":
            TournamentService.update_tournament(self.tournament)
            sys.exit()

    def create_pair(self, players):
        """Create a pair"""

        # First round
        if self.tournament.current_round == 1:
            sorted_players = sorted(players, key=lambda player: player.rank, reverse=True)
            return list(zip(sorted_players[::2], sorted_players[1::2]))

        # Other rounds
        else:
            sorted_players = []
            sorted_players_by_score = sorted(players, key=lambda player: player.score, reverse=True)

            for i, player in enumerate(sorted_players_by_score):
                try:
                    sorted_players.append(player)
                except player.score == sorted_players_by_score[i + 1].score:
                    if player.rank > sorted_players_by_score[i + 1].rank:
                        top_player = player
                        bottom_player = sorted_players_by_score[i + 1]
                    else:
                        top_player = sorted_players_by_score[i + 1]
                        bottom_player = player
                    sorted_players.append(top_player)
                    sorted_players.append(bottom_player)
                except IndexError:
                    sorted_players.append(player)

            # Split the list in two
            top_players = sorted_players[::2]
            bottom_players = sorted_players[1::2]

            players_pairs = []

            # Create pairs
            for i, player in enumerate(top_players):
                y = 0
                while True:
                    try:
                        player2 = bottom_players[i + y]
                    except IndexError:
                        player2 = bottom_players[i]
                        players_pairs.append((player, player2))

                        # Assign players in respective lists of opponents
                        player.opponents.append(player2)
                        player2.opponents.append(player)
                        break

                    # Check if player2 is already in player's opponents list
                    if player2 in player.opponents:
                        y += 1
                        continue
                    else:
                        players_pairs.append((player, player2))

                        # Assign players in respective lists of opponents
                        player.opponents.append(player2)
                        player2.opponents.append(player)
                        break

            return players_pairs

    def get_round_winner(self, players):
        """Get the winner of the round"""
        choice = self.view.display_round_winner(players)

        if choice == "1":
            players[0].score += 1
        elif choice == "2":
            players[1].score += 1
        elif choice == "3":
            players[0].score += 0.5
            players[1].score += 0.5

        # Update players rank
        self.update_player_rank(self.tournament.players)

        TournamentService.update_tournament(self.tournament)

    def update_player_rank(self, players):
        """Update the rank of a player"""
        # Sort players by points
        sorted_players = sorted(players, key=lambda player: player.score, reverse=True)

        # Update rank
        for rank, player in enumerate(sorted_players, start=1):
            player.rank = rank

        return players

    def handle_repports(self):
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
        print(tabulate(sorted_players, headers="keys", tablefmt="fancy_grid"))

    def display_players_by_ranking(self):
        """Display the list of players"""
        players = PlayerService.get_all_players()
        sorted_players = sorted(players, key=lambda player: player["rank"])
        print(tabulate(sorted_players, headers="keys", tablefmt="fancy_grid"))

    def display_tournaments_list(self):
        """Display the list of tournaments"""
        tournaments = TournamentService.get_all_tournaments()
        clean_tournaments = [
            {key: value for key, value in element.items() if key not in ['players', 'rounds']}
            for element in tournaments
        ]
        print(tabulate(clean_tournaments, headers="keys", tablefmt="fancy_grid"))

    def display_tournament_details(self):
        """Display tournament details"""
        user_input = input("Enter tournament name: ")
        tournament = TournamentService.get_tournament(name=user_input)
        if tournament:
            deserialized_tournament = TournamentService.deserialize_tournament(tournament)
            print(f"Tournament name : {deserialized_tournament.name}")
            print(f"Start date : {deserialized_tournament.start_date}")
            print(f"End date : {deserialized_tournament.end_date}")
        else:
            print("Tournament not found.")

    def display_rounds_and_matches_details_by_tournaments(self):
        """Display the list of tournaments"""
        user_input = input("Enter tournament name: ")
        tournament = TournamentService.get_tournament(name=user_input)
        if tournament:
            deserialized_tournament = TournamentService.deserialize_tournament(tournament)
            rounds = deserialized_tournament.rounds
            for round in rounds:
                print(f"Round : {round['name']}")
                matches = round['matches']
                for match in matches:
                    print(f"Match : {match[0][0]} vs {match[1][0]}")
        else:
            print("Tournament not found.")

    def run(self):
        """Run the program"""
        welcome_choice = self.view.display_welcome_message()

        if welcome_choice == "1":
            self.create_tournament()
        elif welcome_choice == "2":
            self.load_tournament()
            self.add_players()
        elif welcome_choice == "3":
            self.handle_repports()
        elif welcome_choice == "4":
            sys.exit()
        else:
            pass
