from tinydb import TinyDB, Query

from models.round import RoundService
from models.player import PlayerService


class Tournament:
    """Tournament class"""

    def __init__(self, name, location, players: list, rounds: list, description=''):
        """Tournament constructor"""
        self.name = name
        self.location = location
        self.description = description
        self.rounds = rounds
        self.players = players
        self.start_date = None
        self.end_date = None
        self.rounds_total = 4
        self.current_round = 1

    def __repr__(self):
        """Better representation of a tournament object"""
        return print(f"Name:{self.name}, Location:{self.location}, Participants: {self.players}, Round:{self.rounds}")


class TournamentService:
    """TournamentService class, used to interact with the database"""

    def __init__(self, tournament):
        """TournamentService constructor, used to interact with the database"""
        self.tournament = tournament
        self.tournaments_bd = TinyDB(
            "data/tournaments/tournaments.json", sort_keys=True, indent=4, separators=(',', ': ')
        )
        self.serialized_tournament = self.get_serialized_tournament()

    def get_serialized_tournament(self):
        """Method to get a serialized tournament"""
        serialized_players = []
        for player in self.tournament.players:
            serialized_player = PlayerService(player).get_serialized_player()
            serialized_players.append(serialized_player)

        serialized_rounds = []
        for round in self.tournament.rounds:
            serialized_round = RoundService(round).get_serialized_round()
            serialized_rounds.append(serialized_round)

        return {
            "name": self.tournament.name,
            "location": self.tournament.location,
            "description": self.tournament.description,
            "rounds": serialized_rounds,
            "players": serialized_players,
            "start_date": self.tournament.start_date,
            "end_date": self.tournament.end_date,
            "rounds_total": self.tournament.rounds_total,
            "current_round": self.tournament.current_round,
        }

    def save_tournament(self):
        """Method to create a tournament in the database"""
        self.tournaments_bd.insert(self.serialized_tournament)
        print("Tournament created successfully")

    def get_tournament(self, name):
        """Method to get a tournament from the database"""
        self.tournaments_bd.search(Query().name == name)

    def get_all_tournaments(self):
        """Method to get all tournaments from the database"""
        self.tournaments_bd.all()

    def update_tournament(self, name):
        """Method to update a tournament in the database"""
        self.tournaments_bd.update(self.serialized_tournament, Query().name == name)
        print("Tournament updated successfully")
