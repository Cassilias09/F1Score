from flask.views import MethodView
from flask_smorest import Blueprint, abort

from src.schemas.championship.championship_schema import ChampionshipStandingsResponseSchema
from src.schemas.championship.championship_filter_schema import ChampionshipStandingsFilterSchema
from src.services.championship_service import ChampionshipService
from src.utils.http import HttpStatusCode

blp = Blueprint(
    "Championship", __name__, description="Operations on F1 championship standings"
)

championship_service = ChampionshipService()


@blp.route("/api/championship/standings")
class ChampionshipStandings(MethodView):

    @blp.arguments(ChampionshipStandingsFilterSchema, location="query")
    @blp.response(HttpStatusCode.OK, ChampionshipStandingsResponseSchema)
    def get(self, args):
        """
        Get championship standings for a specific season.
        """
        season = args["season"]
        try:
            standings = championship_service.get_championship_standings(season)
            return standings
        except ValueError as e:
            abort(HttpStatusCode.BAD_REQUEST, message=str(e))
        except Exception as _:
            abort(HttpStatusCode.INTERNAL_SERVER_ERROR,
                  message="An error occurred while fetching championship standings.")
