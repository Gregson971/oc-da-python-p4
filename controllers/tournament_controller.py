from datetime import datetime
import sys

from models.tournament import Tournament, TournamentService
from models.player import Player, PlayerService
from models.round import Round
from models.match import Match

PLAYER_PER_MATCH = 2


class TournamentController:
    def __init__(self, view):
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

        # TournamentService(new_tournament).save_tournament()

        self.add_players()

    def create_player(self):
        """Create a player"""
        player_informations = self.view.create_player()
        first_name = player_informations["first_name"]
        last_name = player_informations["last_name"]
        birthdate = player_informations["birthdate"]
        chess_id = player_informations["chess_id"]

        new_player = Player(first_name, last_name, birthdate, chess_id)
        self.tournament.players.append(new_player)

        # PlayerService(new_player).save_player()

    def add_players(self):
        """Add players to the tournament"""
        have_even_numbers_of_players = len(self.tournament.players) % 2 == 0
        create_player_choice = self.view.display_create_player()

        if create_player_choice == "1":
            self.create_player()

            for i in range(self.tournament.rounds_total * PLAYER_PER_MATCH):
                if have_even_numbers_of_players and len(self.tournament.players) > 0:
                    should_continue_adding_players = self.view.get_should_continue_adding_players()
                    if should_continue_adding_players:
                        self.create_player()
                    else:
                        self.start_tournament()

        elif create_player_choice == "2":
            pass
        elif create_player_choice == "3":
            # TournamentService(new_tournament).save_tournament()
            sys.exit()
        else:
            pass

    def create_pair(self, players):
        """Create a pair"""
        for i in range(0, len(players), 2):
            yield players[i], players[i + 1]

    def get_round_winner(self, players):
        """Get the winner of the round"""
        choice = self.view.display_round_winner(players)

        if choice == "1":
            self.tournament.players[0].score += 1
        elif choice == "2":
            self.tournament.players[1].score += 1
        elif choice == "3":
            self.tournament.players[0].score += 0.5
            self.tournament.players[1].score += 0.5

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

            print(f"ROUNDS: {self.tournament.rounds}")

            self.tournament.rounds[round_number].start_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")[:-3]
            print(f"ROUND START DATE: {self.tournament.rounds[round_number].start_date}")
            print(f"CURRENT ROUND: {self.tournament.current_round}")

            self.get_round_winner(self.tournament.players)

            self.tournament.rounds[round_number].end_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")[:-3]

            self.tournament.current_round += 1

        elif choice == "2":
            pass
        elif choice == "3":
            sys.exit()

    def start_tournament(self):
        """Start the tournament"""
        self.tournament.start_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")[:-3]
        print(f"START DATE: {self.tournament.start_date}")

        for i in range(self.tournament.rounds_total):
            self.start_round(i)

        # TournamentService(self.tournament).save_tournament()

        self.show_result(self.tournament.players)

    def get_winner(self):
        """Get the winner of the tournament"""
        self.view.display_winner()

    def show_result(self, players):
        self.view.display_end_tournament()

        for player in players:
            print(f"{player.full_name} - {player.score}")

        self.tournament.end_date = datetime.now()
        print(f"END DATE: {self.tournament.end_date}")

        sys.exit()

    def run(self):
        """Run the program"""
        welcome_choice = self.view.display_welcome_message()

        if welcome_choice == "1":
            self.create_tournament()
        elif welcome_choice == "2":
            pass
        elif welcome_choice == "3":
            pass
        elif welcome_choice == "4":
            self.end_tournament()
        elif welcome_choice == "5":
            sys.exit()
        else:
            pass
