from services.match_service import MatchService


class RoundService:
    """RoundService class, used to interact with the data"""

    def serialize_round(round):
        """Method to get a serialized round"""
        if isinstance(round, dict):
            return round

        serialized_matches = []
        for match in round.matches:
            serialized_match = MatchService.serialize_match(match)
            serialized_matches.append(serialized_match)

        return {
            "name": round.name,
            "matches": serialized_matches,
            "start_date": round.start_date,
            "end_date": round.end_date,
        }
