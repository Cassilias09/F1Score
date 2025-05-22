from marshmallow import Schema, fields


class DriverStandingSchema(Schema):
    position = fields.Int(required=True, metadata={
                          "description": "Driver's championship position"})
    driver_code = fields.Str(required=True, metadata={
                             "description": "Three-letter code for the driver"})
    driver_full_name = fields.Str(required=True, metadata={
                                  "description": "Full name of the driver"})
    team_name = fields.Str(required=True, metadata={
                           "description": "Name of the driver's team"})
    points = fields.Float(required=True, metadata={
                          "description": "Total points accumulated by the driver"})


class ConstructorStandingSchema(Schema):
    position = fields.Int(required=True, metadata={
                          "description": "Constructor's championship position"})
    team_name = fields.Str(required=True, metadata={
                           "description": "Full name of the constructor (team)"})
    points = fields.Float(required=True, metadata={
                          "description": "Total points accumulated by the constructor"})


class ChampionshipStandingsResponseSchema(Schema):
    season = fields.Int(required=True, metadata={
                        "description": "Year of the championship season"})
    driver_standings = fields.List(
        fields.Nested(DriverStandingSchema), required=True)
    constructor_standings = fields.List(
        fields.Nested(ConstructorStandingSchema), required=True)
