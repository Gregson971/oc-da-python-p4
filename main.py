from models.player import Player, PlayerService
from models.tournament import Tournament, TournamentService
from models.round import Round
from models.match import Match


def main():
    player = Player("Jean", "Dupont", "01/01/2000", "AB12345")
    player2 = Player("John", "Doe", "15/04/1986", "CD67890")
    # save_player(player)
    # save_player(player2)

    players = [player, player2]
    match = Match(players)
    rounds = Round("Round 1", [match])
    tournament = Tournament("Tournament 1", "Paris", players, [rounds], "Description : Hello World")

    save_tournament(tournament)


def save_player(player):
    return PlayerService(player).save_player()


def save_tournament(tournament):
    return TournamentService(tournament).save_tournament()


if __name__ == "__main__":
    main()
