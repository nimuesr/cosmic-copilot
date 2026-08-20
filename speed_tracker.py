def calculate_planet_speed_weight(planet_name):
    """
    Sprint E Engine: Classifies planets by their astronomical transit speeds
    and awards specific mathematical point weights for rectification scoring.
    """
    # Define our two cosmic speeds
    slow_masterminds = ["Pluto", "Neptune", "Uranus", "Saturn", "Jupiter"]
    fast_getaway_drivers = ["Mars", "Venus", "Mercury", "Sun", "Moon"]

    name = planet_name.capitalize().strip()

    # Scoring Weight Logic
    if name in slow_masterminds:
        return {
            "classification": "Slow Mastermind",
            "base_points": 10,
            "description": "Establishes long-term structural pressure, lifecycle chapters, and event windows."
        }
    elif name in fast_getaway_drivers:
        return {
            "classification": "Fast Getaway Driver",
            "base_points": 3,
            "description": "Acts as the daily trigger or spark that ignites the event on an exact date."
        }
    else:
        return {
            "classification": "Minor Point",
            "base_points": 1,
            "description": "Background celestial tracking point."
        }

# --- SPRINT E SYSTEM AUDIT RUN ---
print("--- SPRINT E: DUAL-CLOCK SPEED AUDIT ---")

# Let's run a test calculation using the real planets that triggered your July 2026 job loss!
test_planets = ["Saturn", "Neptune", "Mars"]

total_calculated_points = 0

for planet in test_planets:
    profile = calculate_planet_speed_weight(planet)
    total_calculated_points += profile["base_points"]
    print(f"🪐 Tracking Planet: {planet}")
    print(f"   ⏱️ Speed Profile: {profile['classification']}")
    print(f"   📊 Score Value: +{profile['base_points']} Points")
    print(f"   📝 System Role: {profile['description']}\n")

print(f"🏆 Cumulative Potential Metric Score for this configuration: {total_calculated_points} Points")
