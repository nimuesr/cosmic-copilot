def fetch_career_archetype(midheaven_sign):
    """
    Sprint G Engine: Acts as the data routing hook that automatically
    parses the master database and outputs the career text profile.
    """
    # The complete 12-sign master text database library
    archetype_database = {
        "Aries": {
            "title": "The Pioneer",
            "profile": "Driven by fast-paced, independent actions, competition, or entrepreneurship. Needs to call the shots."
        },
        "Taurus": {
            "title": "The Builder",
            "profile": "Seeks stable, lucrative, and tangible career tracks (finance, design, real estate). Highly resistant to unexpected chaos."
        },
        "Gemini": {
            "title": "The Jack-of-All-Trades",
            "profile": "Requires continuous mental variety, writing, or multitasking. Often runs two distinct paths or side-hustles simultaneously."
        },
        "Cancer": {
            "title": "The Nurturer",
            "profile": "Focused on human caretaking, psychology, emotional support, or protective business structures that treat colleagues like family."
        },
        "Leo": {
            "title": "The Performer",
            "profile": "Thrives when explicitly recognized, visible, or placed in a leadership spotlight. Suffocates when hidden away in a cubicle."
        },
        "Virgo": {
            "title": "The Strategist",
            "profile": "Highly analytical, organized, and focused on systematic problem-solving, detailed editing, or healthcare/service mastery."
        },
        "Libra": {
            "title": "The Diplomat",
            "profile": "Centers on high-stakes client relationships, artistic styling, legal mediation, public relations, or design curation."
        },
        "Scorpio": {
            "title": "The Alchemist",
            "profile": "Attracted to deep research, data investigation, crisis management, secrets, or behind-the-scenes psychological power dynamics."
        },
        "Sagittarius": {
            "title": "The Explorer",
            "profile": "Needs continuous freedom, long-distance travel, philosophical publishing, teaching, or a global perspective."
        },
        "Capricorn": {
            "title": "The Executive",
            "profile": "The classic corporate blueprint. Deeply ambitious, focused on structural rules, corporate ladders, and long-term societal status."
        },
        "Aquarius": {
            "title": "The Humanitarian",
            "profile": "Unconventional, community-oriented, or heavy tech tracks (astrology, custom coding, network infrastructure, modern social groups)."
        },
        "Pisces": {
            "title": "The Shapeshifter",
            "profile": "Your true placement! Navigates career fog, intuitive roles, and healing arts. Requires total fluidity over rigid, fixed formatting."
        }
    }

    # Format the input string cleanly to match our database keys
    sign = midheaven_sign.capitalize().strip()

    # Query the database
    if sign in archetype_database:
        return archetype_database[sign]
    else:
        return {
            "title": "Unknown Horizon",
            "profile": "The simulated birth time has pushed the Midheaven into uncalculated boundary degrees."
        }

# --- SPRINT G SYSTEM AUDIT RUN ---
print("--- SPRINT G: CAREER HOOK INTEGRATION TEST ---")

# Let's simulate your app testing two different birth times!
# Test Time 1 results in an Aries MC, Test Time 2 results in your true Pisces MC.
simulated_mc_sign_1 = "Aries"
simulated_mc_sign_2 = "Pisces"

result_1 = fetch_career_archetype(simulated_mc_sign_1)
result_2 = fetch_career_archetype(simulated_mc_sign_2)

print(f"Simulation 1 Cusp Sign: {simulated_mc_sign_1}")
print(f"📊 Dashboard Title Header: {result_1['title']}")
print(f"📝 Appended Profile Text: {result_1['profile']}\n")
print("-" * 50)
print(f"Simulation 2 Cusp Sign: {simulated_mc_sign_2}")
print(f"📊 Dashboard Title Header: {result_2['title']}")
print(f"📝 Appended Profile Text: {result_2['profile']}")
