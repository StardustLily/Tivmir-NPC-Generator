import streamlit as st
import random

# ==========================================
# 1. CONFIGURATION & CSS
# ==========================================
st.set_page_config(page_title="D&D 5e NPC Generator", page_icon="🎲", layout="centered")

# Custom CSS to make the NPC card look like a D&D stat block
st.markdown("""
<style>
    .npc-card {
        background-color: #fdf6e3; /* Parchment color */
        border: 2px solid #8b0000; /* Dark Red border */
        border-radius: 10px;
        padding: 20px;
        color: #333;
        font-family: 'Georgia', serif;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
    }
    .npc-name {
        font-size: 28px;
        font-weight: bold;
        color: #8b0000;
        border-bottom: 2px solid #8b0000;
        margin-bottom: 10px;
    }
    .npc-subhead {
        font-size: 18px;
        font-style: italic;
        color: #555;
        margin-bottom: 20px;
    }
    .npc-section {
        font-weight: bold;
        color: #8b0000;
        margin-top: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #8b0000;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA LISTS (The "Brain" of the Randomness)
# ==========================================

races = [
    "Human", "Elf", "Dwarf", "Halfling", "Gnome", 
    "Tiefling", "Dragonborn", "Half-Orc", "Half-Elf", 
    "Tabaxi", "Aarakocra", "Genasi", "Goliath", "Changeling"
]

genders = ["Male", "Female", "Non-Binary"]

occupations = {
    "Commoner": ["Farmer", "Blacksmith", "Innkeeper", "Stablehand", "Cook", "Tailor", "Carpenter", "Miner"],
    "Merchant": ["Traveling Merchant", "Jeweler", "Potion Seller", "Bookkeeper", "Art Dealer", "Smuggler"],
    "Noble/Official": ["Town Guard", "Magistrate", "Noble Scion", "Tax Collector", "Diplomat", "Knight"],
    "Specialized": ["Alchemist", "Wizard's Apprentice", "Bardic Performer", "Bounty Hunter", "Cultist", "Grave Digger"],
    "Criminal": ["Thief", "Bandit", "Spy", "Fence", "Forger"]
}

# Domains for deities to keep it setting-agnostic but flavorful
domains = [
    "War", "Life", "Light", "Nature", "Tempest", "Trickery", "Knowledge", 
    "Death", "Forge", "Grave", "Order", "Peace", "Twilight", "Arcana"
]

personalities = [
    "Anxious and jittery", "Boisterous and loud", "Stoic and unreadable", "Charming and flirtatious",
    "Grumpy and cynical", "Optimistic and naive", "Arrogant and condensation", "Quiet and observant",
    "Scatterbrained", "Suspicious of everyone", "Generous to a fault", "Cowardly but boastful"
]

appearances_build = ["Lanky", "Muscular", "Portly", "Petite", "Towering", "Wiry", "Stocky", "Elegant"]
appearances_quirk = [
    "missing a tooth", "has a jagged scar across the cheek", "wears too much perfume", 
    "has heterochromia (different colored eyes)", "is constantly fidgeting with a coin",
    "wears an eyepatch", "has intricate tattoos", "smells faintly of sulfur",
    "has very long, unkempt hair", "wears impeccably clean clothes", "is covered in flour/dust"
]

goals = [
    "To clear their family name", "To earn enough gold to buy a ship", "To find a cure for a sick relative",
    "To get revenge on a rival", "To become the mayor of this town", "To hide from their dark past",
    "To find the best ale in the realm", "To prove they are not a coward", "To interpret a strange dream",
    "To pay off a debt to a crime lord"
]

secrets = [
    "Is actually a silver dragon in disguise (or thinks they are)", "Murdered the previous shop owner",
    "Is a spy for a neighboring kingdom", "Worships a banned dark deity in secret",
    "Has a stash of stolen goods under the floorboards", "Is a lycanthrope trying to control it",
    "Is actually two goblins in a trench coat", "Knows the location of a lost artifact",
    "Is having an affair with the local noble", "Is currently possessed by a minor ghost"
]

# Name components for procedural generation
syllables_start = ["Ad", "Ae", "Ara", "Bal", "Be", "Car", "Da", "El", "Fa", "Gil", "Hro", "Ia", "Ka", "Lor", "Mar", "Nor", "O", "Pa", "Qu", "Ri", "Sha", "Tho", "Ul", "Val", "Xan", "Za"]
syllables_end = ["bar", "ced", "dall", "fal", "gorn", "hian", "ius", "jo", "kell", "las", "mor", "nai", "orin", "par", "quen", "rath", "stus", "th", "und", "var", "wyn", "xis", "yark", "zen"]
surnames = ["Lightfoot", "Ironfist", "Stormwind", "Oakenheart", "Shadowwalker", "Brightwood", "Goldseeker", "Swiftfoot", "Moonwhisper", "Stoutshield", "Duskbreaker", "Fireforge"]

# ==========================================
# 3. LOGIC FUNCTIONS
# ==========================================

def generate_name(race):
    # Simple name generator (expandable based on race logic if desired)
    # For a simple script, we mix syllables.
    first = random.choice(syllables_start) + random.choice(syllables_end)
    last = random.choice(surnames)
    
    # Racial tweaks (Optional flavor)
    if race in ["Dwarf", "Orc", "Half-Orc"]:
        first = random.choice(["Grum", "Thar", "Bor", "Hul", "Krag", "Mag"]) + random.choice(["dar", "gorn", "ak", "uk", "tar"])
    elif race in ["Elf", "Half-Elf"]:
        first = random.choice(["Ael", "Eri", "Lia", "The", "Val", "Xil"]) + random.choice(["thir", "wyn", "ian", "ora", "sar"])
        
    return f"{first.capitalize()} {last}"

def get_deity_string(domain):
    # Generates a deity string that fits homebrew
    generic_titles = ["The Watcher", "The All-Father", "The Silver Lady", "The Storm King", "The Judge", "The Whisperer"]
    return f"{random.choice(generic_titles)} (God of {domain})"

def generate_npc(filters):
    # 1. Race
    race = filters['race'] if filters['race'] != "Random" else random.choice(races)
    
    # 2. Gender
    gender = filters['gender'] if filters['gender'] != "Random" else random.choice(genders)
    
    # 3. Occupation
    if filters['occupation'] != "Random":
        # User picked a category (e.g., "Merchant")
        # We pick a specific job from that category
        job = random.choice(occupations[filters['occupation']])
    else:
        # Pick a random category then a random job
        cat = random.choice(list(occupations.keys()))
        job = random.choice(occupations[cat])

    # 4. Name
    name = generate_name(race)

    # 5. Appearance
    app_str = f"{random.choice(appearances_build)} build. Distinctive feature: {random.choice(appearances_quirk)}."

    # 6. Deity
    worships = "None/Atheist"
    if random.random() > 0.15: # 85% chance to worship someone
        worships = get_deity_string(random.choice(domains))

    return {
        "Name": name,
        "Race": race,
        "Gender": gender,
        "Occupation": job,
        "Appearance": app_str,
        "Personality": random.choice(personalities),
        "Deity": worships,
        "Goal": random.choice(goals),
        "Secret": random.choice(secrets)
    }

# ==========================================
# 4. STREAMLIT UI LAYOUT
# ==========================================

st.title("🐉 Homebrew NPC Generator")
st.write("Generate unique NPCs for your D&D 5e campaign instantly.")

# --- Sidebar Filters ---
st.sidebar.header("⚙️ Configuration")
st.sidebar.write("Lock specific attributes or leave them random.")

sel_race = st.sidebar.selectbox("Race", ["Random"] + races)
sel_gender = st.sidebar.selectbox("Gender", ["Random"] + genders)
sel_job = st.sidebar.selectbox("Occupation Category", ["Random"] + list(occupations.keys()))

if st.sidebar.button("Generate New NPC"):
    st.session_state['npc'] = generate_npc({
        "race": sel_race,
        "gender": sel_gender,
        "occupation": sel_job
    })

# --- Main Display ---

# Initialize session state if first load
if 'npc' not in st.session_state:
    st.session_state['npc'] = generate_npc({
        "race": "Random",
        "gender": "Random",
        "occupation": "Random"
    })

npc = st.session_state['npc']

# Display the "Card"
st.markdown(f"""
<div class="npc-card">
    <div class="npc-name">{npc['Name']}</div>
    <div class="npc-subhead">{npc['Gender']} {npc['Race']} {npc['Occupation']}</div>
    
    <hr style="border-color: #8b0000; opacity: 0.3;">

    <div style="display: flex; flex-wrap: wrap;">
        <div style="flex: 50%; padding-right: 10px;">
            <div class="npc-section">👀 Appearance</div>
            <div>{npc['Appearance']}</div>
            
            <div class="npc-section">🧠 Personality</div>
            <div>{npc['Personality']}</div>
            
            <div class="npc-section">🙏 Worships</div>
            <div>{npc['Deity']}</div>
        </div>
        <div style="flex: 50%;">
            <div class="npc-section">🎯 Current Goal</div>
            <div>{npc['Goal']}</div>
            
            <div class="npc-section">🤫 Secret</div>
            <div>{npc['Secret']}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Export Option (Simple Copy) ---
st.markdown("###") # Spacer
with st.expander("📋 Copy Text Format"):
    st.text(f"""
    Name: {npc['Name']}
    Race/Gender: {npc['Race']} {npc['Gender']}
    Occupation: {npc['Occupation']}
    Appearance: {npc['Appearance']}
    Personality: {npc['Personality']}
    Deity: {npc['Deity']}
    Goal: {npc['Goal']}
    Secret: {npc['Secret']}
    """)
