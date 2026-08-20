def calculate_aspect_angle(planet_degree, natal_degree):
    """
    Calculates the exact shortest angular distance between two points in a 360° circle,
    and identifies if it matches a major astrological aspect within a 1-degree error window.
    """
    # Step 1: Find raw mathematical distance on a 360-degree wheel
    raw_diff = abs(planet_degree - natal_degree)
    
    # Step 2: Correct for circle loop-around (shortest distance can never exceed 180°)
    if raw_diff > 180:
        angle = 360 - raw_diff
    else:
        angle = raw_diff

    # Step 3: Set allowed margin of error (1 degree orb)
    orb = 1.0

    # Step 4: Run aspect identification filters
    # HARD ASPECTS (Friction/Disruption Triggers)
    if abs(angle - 0) <= orb:
        return {"type": "Conjunction", "nature": "Friction Trigger (Massive Climax/Clean Slate)", "hit": True}
        
    elif abs(angle - 90) <= orb:
        return {"type": "Square", "nature": "Friction Trigger (Forced Block/Immediate Action Required)", "hit": True}
        
    elif abs(angle - 180) <= orb:
        return {"type": "Opposition", "nature": "Friction Trigger (Tug-of-War Conflict/Sudden Break)", "hit": True}
        
    elif abs(angle - 150) <= orb:
        return {"type": "Quincunx", "nature": "Friction Trigger (Blind-spot/Awkward Necessary Pivot)", "hit": True}

    # SOFT ASPECTS (Release Triggers)
    elif abs(angle - 120) <= orb:
        return {"type": "Trine", "nature": "Release Trigger (Trap Door/Easy Exit Ramp)", "hit": True}
        
    elif abs(angle - 60) <= orb:
        return {"type": "Sextile", "nature": "Release Trigger (Open Opportunity/Supportive Window)", "hit": True}

    # No exact geometric correlation hit
    return {"type": "None", "nature": "Background Noise", "hit": False}

# --- QUICK TEST RUN FOR ESS' CHART ---
# Testing your actual July 2026 job loss transits against your chart degrees:
# Transit Saturn was at 6° Aries (36° total layout longitude)
# Your Natal Saturn sits at 4° Scorpio (214° total layout longitude)

result = calculate_aspect_angle(36.0, 214.0)

print(f"--- ASPECT AUDIT DETECTED ---")
print(f"Geometric Aspect: {result['type']}")
print(f"Event Manifestation Character: {result['nature']}")
