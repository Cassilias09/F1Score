import fastf1


class ChampionshipService:
    def __init__(self):
        # Enable cache for faster subsequent requests.
        # It's good practice to enable it once at the service initialization.
        fastf1.Cache.enable_cache('src/cache/fastf1')

    def get_championship_standings(self, season: int):
        """
        Retrieves championship standings (drivers and constructors) for a given season.
        """
        try:
            # Get the full event schedule for the season
            schedule = fastf1.get_event_schedule(season)

            # Filter for race events and get the max round
            race_events = schedule[schedule['EventFormat'].isin(
                ['conventional', 'sprint'])]

            if race_events.empty:
                raise ValueError(
                    f"No race events found for season {season}. Standings cannot be retrieved.")

            # Let's get the race with the highest round number
            last_round_number = race_events['RoundNumber'].max()

            # Ensure we get the 'Race' session type for the last round
            session = fastf1.get_session(season, last_round_number, 'R')

            # Load the session data. This will include final standings.
            session.load()

            # Access the final standings directly from the session object
            driver_standings_df = session.results

            # Process driver standings
            processed_driver_standings = []
            for _, row in driver_standings_df.iterrows():
                processed_driver_standings.append({
                    "position": int(row['Position']),
                    "classified_position": row['ClassifiedPosition'],
                    "grid_position": int(row['GridPosition']),
                    "driver_code": row['Abbreviation'],
                    "driver_full_name": f"{row['FirstName']} {row['LastName']}",
                    "team_name": row['TeamName'],
                    "points": float(row['Points'])
                })

            return {
                "season": season,
                "driver_standings": processed_driver_standings,
            }
        except Exception as e:
            # FastF1 can raise errors if data isn't available for the season/round
            print(
                f"Error fetching championship standings for season {season}: {e}")
            # Reraise a more specific error or handle gracefully
            raise ValueError(
                f"Could not retrieve championship standings for season {season}. Details: {e}")
