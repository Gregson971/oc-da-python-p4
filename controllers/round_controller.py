import sys
from datetime import datetime

from models.tournament import Tournament, TournamentService
from models.round import Round
from models.match import Match

from views.menu_view import MenuView


class RoundController:
    def __init__(self, view: MenuView, tournament: Tournament):
        self.view = view
        self.tournament = tournament

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
                        player.opponents.append(player2.full_name)
                        player2.opponents.append(player.full_name)
                        break

                    # Check if player2 is already in player's opponents list
                    if player2 in player.opponents:
                        y += 1
                        continue
                    else:
                        players_pairs.append((player, player2))

                        # Assign players in respective lists of opponents
                        player.opponents.append(player2.full_name)
                        player2.opponents.append(player.full_name)
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
