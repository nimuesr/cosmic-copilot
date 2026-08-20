import swisseph as swe
from datetime import datetime

# A — THE LOGIC ENGINE: Define your static birth date (Roberval, QC)
BIRTH_YEAR = 1983
BIRTH_MONTH = 1
BIRTH_DAY = 28
LATITUDE = 48.5167    # Roberval Coordinates
LONGITUDE = -72.2333

# D — THE EVENT AXIS MATRIX: Guide the app on which houses to score
# Maps user choices to natural house archetypes
EVENT_WEIGHTS = {
    "injury": {"target_houses":, "planets": ["Mars", "SouthNode"]},
    "career": {"target_houses":, "planets": ["Saturn", "Neptune", "Uranus", "Pluto"]},
    "crisis": {"target_houses":, "planets": ["Pluto", "Saturn"]}
}

# User enters their real life milestones
user_events = [
    {"date": "2019-04-15", "type": "injury", "desc": "Broke knee & wrist"},
    {"date": "2022-10-15", "type": "crisis", "desc": "Burnout medical leave"},
    {"date": "2026-07-01", "type": "career", "desc": "Complicated job loss"}
]

# B — THE MINUTE-SHIFTER LOOP
# Test every single minute in a 2-hour window around 3:09 PM (15:09)
def run_rectification_audit():
    leaderboard = []
    
    # Loop from 2:00 PM (14:00) to 4:00 PM (16:00) minute-by-minute
    for hour in range(14, 16):
        for minute in range(0, 60):
            total_ping_score = 0
            
            # C — THE STATIC SIGNPOST TRACKER
            # Calculate House Cusps for this specific simulated minute
            # (Converts local time to Universal Time for accuracy)
            jd_birth = swe.julday(BIRTH_YEAR, BIRTH_MONTH, BIRTH_DAY, hour + (minute / 60.0))
            cusps, ascmc = swe.houses(jd_birth, LATITUDE, LONGITUDE, b'P') # 'P' for Placidus
            
            simulated_asc = ascmc[0] # Exact Ascendant degree for this minute
            simulated_mc = ascmc[1]  # Exact Midheaven degree for this minute
            
            # E — THE TWO-SPEED SCORING SYSTEM
            # Now run through each event to see if the transits "ping" these simulated angles
            for event in user_events:
                event_date = datetime.strptime(event["date"], "%Y-%m-%d")
                jd_event = swe.julday(event_date.year, event_date.month, event_date.day, 12.0) # Midday transit
                
                # Check where the "Slow Mastermind" planets were on that exact event day
                # 0 = Sun, 1 = Moon, 4 = Mars, 5 = Jupiter, 6 = Saturn, 7 = Uranus, 8 = Neptune, 9 = Pluto
                slow_planets = {
                    "Saturn": 6, "Uranus": 7, "Neptune": 8, "Pluto": 9, "Mars": 4
                }
                
                for planet_name, planet_id in slow_planets.items():
                    # Fetch transit planet position from NASA data
                    res, ret = swe.calc_ut(jd_event, planet_id)
                    transit_lon = res[0] # Planet's position in degrees (0-360)
                    
                    # See if transit planet forms an exact hard aspect to the simulated MC
                    # Check for Conjunction (0° separation) within a tight 1° orb of error
                    mc_diff = abs(transit_lon - simulated_mc)
                    if mc_diff < 1.0 or abs(mc_diff - 180) < 1.0 or abs(mc_diff - 90) < 1.0:
                        # If this planet matters to the event type, award maximum points!
                        if planet_name in EVENT_WEIGHTS[event["type"]]["planets"]:
                            total_ping_score += 10 # High score ping!
                            
                    # Check if transit planet hits the simulated Ascendant
                    asc_diff = abs(transit_lon - simulated_asc)
                    if asc_diff < 1.0 or abs(asc_diff - 180) < 1.0:
                        if event["type"] == "injury" and planet_name == "Mars":
                            total_ping_score += 15 # Severe physical injury bonus weight
            
            # Store the score for this simulated birth time
            time_string = f"{hour}:{minute:02d}"
            leaderboard.append({"time": time_string, "score": total_ping_score})
            
    # Sort leaderboard to find the highest total mathematical pings
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    
    print("--- TOP RECOMMENDATIONS FROM RECTIFICATION CALCULATOR ---")
    for rank, entry in enumerate(leaderboard[:3], 1):
        print(f"Rank {rank}: Time {entry['time']} PM (Score: {entry['score']} points match)")

# Run the backend script
run_rectification_audit()
