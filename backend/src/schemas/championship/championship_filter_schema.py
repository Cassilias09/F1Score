from marshmallow import Schema, fields, validate
from datetime import datetime


class ChampionshipStandingsFilterSchema(Schema):
    # ANTES: season = fields.Int(..., description="...")
    season = fields.Int(
        required=True,
        validate=validate.Range(min=1950, max=datetime.today().year),
        metadata={
            "description": "The year of the F1 season to retrieve standings for."}
    )
