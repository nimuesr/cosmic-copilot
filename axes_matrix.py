def route_event_to_axis(event_category):
    """
    Sprint D Engine: Automatically routes a user-defined event category 
    to its corresponding astrological axis and assigns specific planetary trackers.
    """
    # Define the core geometric matrix structure
    matrix = {
        "injury": {
            "target_axis": "Ascendant (1st House line)",
            "description": "Physical body alterations, health traumas, or identity shifts.",
            "primary_triggers": ["Mars", "South Node", "Uranus"]
        },
        "career": {
            "target_axis": "Midheaven / MC (10th House line)",
            "description": "Changes in status, employment endings, promotions, or public direction.",
            "primary_triggers": ["Saturn", "Neptune", "Uranus", "Pluto"]
        },
        "relationship": {
            "target_axis": "Descendant (7th House line)",
            "description": "Marriages, legal divorces, contracts, or open interpersonal conflicts.",
            "primary_triggers": ["Venus", "Pluto", "Saturn", "North Node"]
        },
        "home": {
            "target_axis": "IC / Imum Coeli (4th House line)",
            "description": "Relocations, real estate changes, deep family dynamics, or parental milestones.",
            "primary_triggers": ["Moon", "Saturn", "Uranus"]
        }
    }

    # Standardize input text to prevent typos
    category = event_category.lower().strip()

    # Routing logic loop
    if category in matrix:
        return matrix[category]
    else:
        return {
            "target_axis": "General Chart Points",
            "description": "Unclassified milestone. Scanning entire chart configuration for general planet transits.",
            "primary_triggers": ["Jupiter", "Saturn"]
        }

# --- SPRINT D SYSTEM AUDIT RUN ---
print("--- SPRINT D: AUTOMATED ROUTING RUN ---")

# Let's test routing two of your specific life events through the matrix
test_event_1 = route_event_to_axis("injury")  # Your 2019 broken wrist/knee
test_event_2 = route_event_to_axis("career")  # Your July 2026 job loss

print(f"Event Type: Injury")
print(f"🎯 Routed Axis: {test_event_1['target_axis']}")
print(f"🔍 Monitoring Planets: {', '.join(test_event_1['primary_triggers'])}")
print("-" * 40)
print(f"Event Type: Career")
print(f"🎯 Routed Axis: {test_event_2['target_axis']}")
print(f"🔍 Monitoring Planets: {', '.join(test_event_2['primary_triggers'])}")
