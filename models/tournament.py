from tinydb import TinyDB, Query

from models.round import RoundService
from models.player import PlayerService


class Tournament:
    """Tournament class"""

    def __init__(
        self,
        name,
        location,
        description='',
        players: list = [],
        rounds: list = [],
        start_date=None,
        end_date=None,
        rounds_total=4,
        current_round=1,
    ):
        """Tournament constructor"""
        self.name = name
        self.location = location
        self.description = description
        self.rounds = rounds
        self.players = players
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_total = rounds_total
        self.current_round = current_round

    def __repr__(self):
        """Better representation of a tournament object"""
        return f"Tournament name: {self.name}, Location: {self.location}, Description: {self.description}"


class TournamentService:
    """TournamentService class, used to interact with the database"""

    def __init__(self):
        """TournamentService constructor, used to interact with the database"""

    def serialize_tournament(tournament):
        """Method to get a serialized tournament"""
        serialized_players = []
        for player in tournament.players:
            serialized_player = PlayerService.serialize_player(player)
            serialized_players.append(serialized_player)

        serialized_rounds = []
        for round in tournament.rounds:
            serialized_round = RoundService.serialize_round(round)
            serialized_rounds.append(serialized_round)

        return {
            "name": tournament.name,
            "location": tournament.location,
            "description": tournament.description,
            "rounds": serialized_rounds,
            "players": serialized_players,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "rounds_total": tournament.rounds_total,
            "current_round": tournament.current_round,
        }

    def deserialize_tournament(tournament):
        """Method to deserialize a tournament"""
        return Tournament(
            name=tournament[0]["name"],
            location=tournament[0]["location"],
            description=tournament[0]["description"],
            players=tournament[0]["players"],
            rounds=tournament[0]["rounds"],
            start_date=tournament[0]["start_date"],
            end_date=tournament[0]["end_date"],
            rounds_total=tournament[0]["rounds_total"],
            current_round=tournament[0]["current_round"],
        )

    def save_tournament(tournament):
        """Method to create a tournament in the database"""
        tournaments_bd = TinyDB("data/tournaments/tournaments.json", sort_keys=True, indent=4, separators=(',', ': '))
        serialized_tournament = TournamentService.serialize_tournament(tournament)
        tournaments_bd.insert(serialized_tournament)
        print("Tournament created successfully")

    def get_tournament(name):
        """Method to get a tournament from the database"""
        tournaments_bd = TinyDB("data/tournaments/tournaments.json", sort_keys=True, indent=4, separators=(',', ': '))
        return tournaments_bd.search(Query().name == name)

    def get_all_tournaments():
        """Method to get all tournaments from the database"""
        tournaments_bd = TinyDB("data/tournaments/tournaments.json", sort_keys=True, indent=4, separators=(',', ': '))
        return tournaments_bd.all()

    def update_tournament(tournament):
        """Method to update a tournament in the database"""
        tournaments_bd = TinyDB("data/tournaments/tournaments.json", sort_keys=True, indent=4, separators=(',', ': '))
        serialized_tournament = TournamentService.serialize_tournament(tournament)

        tournaments_bd.update(serialized_tournament, Query().name == tournament.name)
        print("Tournament updated successfully")
