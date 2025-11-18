import streamlit as st
import random
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="Tivmir NPC Forge",
    page_icon="🎭",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    .stButton>button {
        background: linear-gradient(135deg, #22c55e, #22d3ee);
        color: #0b1120;
        font-weight: 600;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        border: none;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    .stButton>button:hover {
        box-shadow: 0 8px 16px rgba(34, 211, 238, 0.4);
        transform: translateY(-2px);
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.2rem;
    }
    .npc-card {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(148, 163, 184, 0.3);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    .npc-name {
        font-size: 2rem;
        font-weight: 700;
        color: #e5e7eb;
        margin-bottom: 0.5rem;
        font-family: 'Georgia', serif;
    }
    .npc-subtitle {
        font-size: 0.9rem;
        color: #9ca3af;
        margin-bottom: 1rem;
    }
    .info-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #9ca3af;
        font-weight: 600;
    }
    .info-value {
        font-size: 1rem;
        color: #e5e7eb;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #cbd5f5;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
        border-bottom: 2px solid rgba(56, 189, 248, 0.3);
        padding-bottom: 0.5rem;
    }
    .pill {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .pill-race {
        background: rgba(56, 189, 248, 0.2);
        border: 1px solid rgba(56, 189, 248, 0.5);
        color: #7dd3fc;
    }
    .pill-gender {
        background: rgba(244, 114, 182, 0.2);
        border: 1px solid rgba(244, 114, 182, 0.5);
        color: #f9a8d4;
    }
    .pill-occupation {
        background: rgba(52, 211, 153, 0.2);
        border: 1px solid rgba(52, 211, 153, 0.5);
        color: #bbf7d0;
    }
    .pill-deity {
        background: rgba(168, 85, 247, 0.2);
        border: 1px solid rgba(168, 85, 247, 0.5);
        color: #c084fc;
    }
</style>
""", unsafe_allow_html=True)

# Tivmir Pantheon Data
DEITIES = {
    "Light": [
        {"name": "Jaydis", "title": "God of Harmony and Balance", "flavor": "They seek balance in all things and mediate conflicts whenever possible."},
        {"name": "Maya", "title": "Goddess of Day and Light", "flavor": "They embrace optimism and find hope even in dark times."},
        {"name": "Solaren", "title": "Goddess of Truth and Clarity", "flavor": "They value honesty above all and cannot abide deception."},
        {"name": "Vivarakan", "title": "Lord of Beginning and Vitality", "flavor": "They celebrate new ventures and fresh starts with infectious enthusiasm."},
        {"name": "Zithra", "title": "God of Warmth and Pleasure", "flavor": "They enjoy life's comforts and encourage others to find joy in simple things."},
    ],
    "Neutral": [
        {"name": "Apsen", "title": "Goddess of Travel and Crossroads", "flavor": "They are restless by nature and feel most at home on the road."},
        {"name": "Auroris", "title": "Deity of Nature and Weather", "flavor": "They speak of natural cycles with reverence and track weather patterns obsessively."},
        {"name": "Julevir", "title": "God of Inspiration and Creativity", "flavor": "They see art in unexpected places and encourage creative expression."},
        {"name": "Jun", "title": "Deity of Dreams and Illusions", "flavor": "They speak in dreamy metaphors and seem to exist slightly out of phase with reality."},
        {"name": "Mabu", "title": "Entity of Chaos and Entropy", "flavor": "They embrace unpredictability and find order stifling."},
        {"name": "Ocea", "title": "Goddess of the Seas and Tides", "flavor": "They are drawn to water and feel uneasy when far from rivers or coast."},
    ],
    "Dark": [
        {"name": "Alfind", "title": "Deity of Ending and Closure", "flavor": "They speak calmly of death and believe all things must eventually end."},
        {"name": "Defenestria", "title": "Goddess of Frost and Pain", "flavor": "They have a cold demeanor and believe suffering strengthens the spirit."},
        {"name": "Lolth", "title": "Lady of Trickery and War", "flavor": "They weigh relationships like webs of obligation and are quick to spot deception."},
        {"name": "Noxtum", "title": "Lord of the Night and Shadows", "flavor": "They are most comfortable in darkness and speak in hushed tones."},
        {"name": "Sable", "title": "Lady of Silence and Reflection", "flavor": "They value quiet contemplation and grow uncomfortable with excessive noise."},
    ]
}

# Tivmir Races with weights
RACES = {
    "Common": {
        "races": ["Aarakocra", "Drow", "Elf", "Goblin", "Human", "Orc", "Tabaxi"],
        "weight": 50
    },
    "Uncommon": {
        "races": ["Goliath", "Halfling", "Half-Orc", "Kenku", "Leonin", "Lizardfolk", "Owlin", "Tortle"],
        "weight": 30
    },
    "Rare": {
        "races": ["Bugbear", "Dragonborn", "Half-Elf", "Harengon", "Loxodon", "Minotaur", "Tiefling", "Yuan-ti"],
        "weight": 15
    },
    "Very Rare": {
        "races": ["Aasimar", "Eladrin (Spring)", "Eladrin (Summer)", "Eladrin (Fall)", "Eladrin (Winter)",
                  "Genasi (Air)", "Genasi (Earth)", "Genasi (Fire)", "Genasi (Water)",
                  "Githyanki", "Gnome", "Shifter", "Triton"],
        "weight": 5
    }
}

GENDERS = ["Woman", "Man", "Nonbinary", "Genderfluid", "Agender"]

# Occupation pools by region
OCCUPATIONS = {
    "any": [
        "innkeeper", "wandering bard", "city guard", "street vendor", "scholar", "archivist",
        "blacksmith", "apothecary", "hunter", "cartographer", "courier", "fence",
        "steward", "sage", "monster scout", "village elder", "mercenary captain", "scribe",
        "artisan", "shipwright", "coach driver", "herbalist", "fortune-teller", "diplomat",
        "gravekeeper", "arena promoter", "temple acolyte", "librarian", "jeweler"
    ],
    "urban": [
        "guild factor", "moneylender", "dock foreman", "thieves' guild contact", "street preacher",
        "city official", "tavern owner", "pawnbroker", "messenger"
    ],
    "rural": [
        "farmer", "mill worker", "shepherd", "beekeeper", "woodcutter", "village herbalist",
        "brewer", "trapper", "weaver", "tinker", "midwife"
    ],
    "frontier": [
        "monster hunter", "scout", "ranger guide", "camp quartermaster", "prospector",
        "border guard", "smuggler", "beast wrangler", "wilderness tracker"
    ],
    "underdark": [
        "mushroom farmer", "underground guide", "information broker", "poisoner",
        "house retainer", "spore druid", "tunnel mapper", "crystal miner"
    ],
    "seafaring": [
        "sailor", "ship's quartermaster", "harbormaster", "smuggler", "dockside bartender",
        "navigator", "shipwright", "whaler", "net mender"
    ],
    "desert": [
        "caravan master", "nomad scout", "oasis keeper", "sand mage", "spice merchant",
        "camel handler", "ruin delver", "water diviner"
    ],
    "arctic": [
        "trapper", "ice fisher", "sled driver", "whaler", "glacier guide",
        "aurora mystic", "frontier priest", "fur trader"
    ],
    "religious": [
        "temple acolyte", "high priest's aide", "choir leader", "itinerant preacher",
        "scribe of holy texts", "relic keeper", "pilgrim guide", "shrine keeper"
    ]
}

# Personality traits by tone
PERSONALITIES = {
    "any": [
        "Warm and quick to laugh, but carefully watches what others reveal before sharing much.",
        "Soft-spoken and courteous, with a habit of apologizing even when they've done nothing wrong.",
        "Blunt and practical, more comfortable with tasks than with small talk.",
        "Inquisitive to a fault, constantly asking how things work and why people made certain choices.",
        "Charming and theatrical, treating even mundane events as if they were on stage.",
        "Stoic and difficult to read, but observant of small details others miss.",
        "Optimistic and energetic, always convinced the next opportunity will be the big one.",
        "Dryly sarcastic, using humor to deflect when conversation gets too personal.",
        "Methodical and precise, keeping everything in order and anxious when plans change.",
        "Secretly sentimental, collecting small trinkets that remind them of places and people."
    ],
    "light": [
        "Playfully dramatic, turning every story into an entertaining exaggeration.",
        "Earnest and friendly, always eager to help and quick to trust.",
        "A bit scatterbrained but endlessly enthusiastic about new ideas.",
        "Loves gossip and rumors, but rarely repeats anything truly hurtful."
    ],
    "grim": [
        "World-weary and guarded, assuming the worst to avoid disappointment.",
        "Pragmatic to the point of cynicism, willing to make hard choices for survival.",
        "Haunted by old mistakes and determined not to repeat them, even if it seems harsh."
    ],
    "mysterious": [
        "Speaks in half-answers and parables, as if seeing patterns others cannot.",
        "Calm and distant, studying others with the patience of a scribe reading ancient texts.",
        "Occasionally uses terminology suggesting secret affiliations or forbidden knowledge."
    ]
}

# Goals by tone
GOALS = {
    "any": [
        "Wants to secure enough coin to retire somewhere quiet, away from conflict.",
        "Hopes to prove themselves worthy of a mentor who once dismissed them.",
        "Quietly gathering information about adventurers for a risky venture.",
        "Aims to restore a damaged reputation after being blamed for someone else's failure.",
        "Wants to map a forgotten route that would cut days off a common journey.",
        "Searching for someone who disappeared years ago, following any rumor."
    ],
    "light": [
        "Dreams of opening a small tavern that becomes the heart of their neighborhood.",
        "Wants to organize a grand festival remembered for generations.",
        "Hopes to collect travelers' stories and compile them into a book of legends."
    ],
    "grim": [
        "Seeks leverage over a cruel authority figure who harmed their family.",
        "Plans to pay off a dangerous debt before becoming an example to others.",
        "Wants to expose corruption within a respected institution, whatever the cost."
    ],
    "mysterious": [
        "Following cryptic prophecies suggesting their actions will influence distant events.",
        "Hunts for an artifact they refuse to name, claiming too many ears are listening.",
        "Needs specific information from travelers about distant lands, but never explains why."
    ]
}

# Secrets by tone
SECRETS = {
    "any": [
        "Once stole a minor relic from a temple, quietly returned it years later, but still fears discovery.",
        "Connected by blood or oath to a powerful figure and hides their true surname.",
        "Has a hidden stash of coin or contraband that even close friends know nothing about.",
        "Quietly communicates with a rival faction, passing information for small favors.",
        "Accidentally caused a tragedy in youth and has spent years making amends from the shadows.",
        "Knows the location of a forgotten tunnel that bypasses a heavily guarded area.",
        "Far more skilled than they pretend, using a humble role as convenient disguise.",
        "Carries a token marking them as part of a secret society most assume is only rumor."
    ],
    "light": [
        "Secretly writes romantic ballads about local adventurers under a pseudonym.",
        "Has been feeding a stray magical creature that has started following them around town.",
        "Keeps a detailed, mildly embarrassing scrapbook of heroes and villains passing through."
    ],
    "grim": [
        "Once accepted payment to look the other way during a crime and has been blackmailed since.",
        "Smuggles medicine and supplies to a forbidden group authorities consider dangerous.",
        "Knows a respected local leader is involved in something foul—but confronting them alone would be fatal."
    ],
    "mysterious": [
        "Has dreams that sometimes show real events from far away, though they don't understand why.",
        "Carries a sealed letter to deliver only to someone matching a vague description—which fits one of the party.",
        "Can see faint ghostlike figures in mirrors and still water, and tries hard to pretend they cannot."
    ]
}

# Appearance descriptions
APPEARANCE_BASE = [
    "Their hair is carefully braided with colored thread, adding warmth to practical attire.",
    "Their armor bears scuffs and dents of real use, but is polished with obvious pride.",
    "They smell faintly of incense and parchment, with ink stains on their fingers.",
    "A streak of silver runs through their hair despite relatively young features.",
    "Their clothes are a patchwork of careful repairs, suggesting sentimentality or frugality.",
    "They favor layered, flowing fabrics with patterns echoing their homeland.",
    "A small charm hangs from their neck or belt, worn smooth by anxious fingers.",
    "Their boots are sturdy and travel-worn, but their hands are surprisingly soft.",
    "They carry themselves with straight-backed discipline, even when trying to stay unnoticed.",
    "Their eyes are alert and restless, tracking exits and faces almost unconsciously."
]

APPEARANCE_FEATURES = [
    "A visible scar along the jaw, softened by a friendly expression.",
    "Eyes that catch light in an unusual hue, suggesting distant bloodlines or subtle magic.",
    "Elaborate tattoos peek from beneath sleeves, hinting at cultural significance.",
    "A missing or prosthetic finger, compensated for with clever adjustments.",
    "An ever-present smudge of soot, ink, or dust, no matter how often they clean.",
    "Jewelry that is inexpensive but obviously well cared for, perhaps a family heirloom.",
    "A subtle limp that only appears when tired or distracted.",
    "A voice that is unexpectedly melodic, with a lilting cadence.",
    "A laugh that comes suddenly and fully, often startling quieter patrons.",
    "A gaze that lingers a heartbeat too long, weighing the truth of every word."
]

def generate_name():
    """Generate a random fantasy name"""
    starts = ["Al", "Ba", "Bel", "Cal", "Da", "El", "Fa", "Gal", "Ka", "La", "Ma", "Na", "Or", "Per", 
              "Ra", "Sa", "Sha", "Ta", "Ther", "Va", "Vor", "Za", "Zel", "Kor", "Jun", "Eri", "Lio", 
              "Syl", "Thal", "Xan"]
    mids = ["a", "e", "i", "o", "u", "ae", "ia", "ai", "ea", "ou", "ar", "ir", "or", "ur", 
            "an", "en", "in", "on", "el", "il", "as", "is", "os"]
    ends = ["n", "s", "th", "r", "nd", "l", "mir", "dor", "drim", "zor", "thar", "das", "ric", 
            "mon", "var", "gorn", "dil", "morn", "viel", "non", "dris", "vash", "dane", "riel", "thor"]
    surnames = ["Amberfall", "Blackwater", "Stormwind", "Duskhollow", "Brightshield", "Ironvein",
                "Thornbriar", "Nightbloom", "Riversong", "Stonebrook", "Highspire", "Ashwillow",
                "Silverstring", "Glimmerforge", "Frostglen", "Shadowfen", "Goldmantle", "Oakensong",
                "Moonridge", "Cinderstep", "Hawkspear", "Deepcurrent", "Starwatch", "Windrider"]
    
    syllables = random.choice([2, 3])
    first = random.choice(starts)
    if syllables == 3:
        first += random.choice(mids)
    first += random.choice(ends)
    
    if random.random() < 0.75:
        return f"{first} {random.choice(surnames)}"
    return first

def pick_race(region):
    """Pick a race based on region, weighted by rarity"""
    base_races = []
    
    # Build weighted list
    for rarity, data in RACES.items():
        base_races.extend([(race, data["weight"]) for race in data["races"]])
    
    # Regional modifications
    if region == "urban":
        base_races.extend([("Human", 30), ("Half-Elf", 20), ("Tiefling", 15)])
    elif region == "rural":
        base_races.extend([("Human", 40), ("Halfling", 25), ("Dwarf", 15)])
    elif region == "underdark":
        base_races.extend([("Drow", 50), ("Drow", 50)])
    
    races, weights = zip(*base_races)
    return random.choices(races, weights=weights)[0]

def pick_deity(region):
    """Pick a deity or None"""
    no_deity_chance = 0.18 if region != "religious" else 0.05
    
    if random.random() < no_deity_chance:
        return None
    
    # Randomly pick from all pantheons
    all_deities = DEITIES["Light"] + DEITIES["Neutral"] + DEITIES["Dark"]
    return random.choice(all_deities)

def pick_from_tone(pool, tone):
    """Pick from pool considering tone"""
    if tone == "any" or tone not in pool:
        return random.choice(pool["any"])
    # Merge any + specific tone
    merged = pool["any"] + pool[tone]
    return random.choice(merged)

def pick_occupation(region):
    """Pick occupation based on region"""
    base = OCCUPATIONS["any"]
    regional = OCCUPATIONS.get(region, [])
    return random.choice(base + regional)

def generate_appearance():
    """Generate appearance description"""
    base = random.choice(APPEARANCE_BASE)
    feature = random.choice(APPEARANCE_FEATURES)
    return f"{base} {feature}"

def generate_npc(region, tone):
    """Generate complete NPC"""
    npc = {
        "name": generate_name(),
        "race": pick_race(region),
        "gender": random.choice(GENDERS),
        "occupation": pick_occupation(region),
        "deity": pick_deity(region),
        "personality": pick_from_tone(PERSONALITIES, tone),
        "goal": pick_from_tone(GOALS, tone),
        "secret": pick_from_tone(SECRETS, tone),
        "appearance": generate_appearance(),
        "region": region,
        "tone": tone
    }
    return npc

def format_npc_text(npc):
    """Format NPC as plain text for copying"""
    deity_text = "None / no fixed patron"
    if npc["deity"]:
        deity_text = f"{npc['deity']['name']}, {npc['deity']['title']}"
    
    text = f"""NPC: {npc['name']}
Race: {npc['race']}
Gender: {npc['gender']}
Occupation: {npc['occupation'].title()}
Deity: {deity_text}

APPEARANCE:
{npc['appearance']}

PERSONALITY:
{npc['personality']}

GOAL:
{npc['goal']}

SECRET:
{npc['secret']}
"""
    return text

# Initialize session state
if 'npc' not in st.session_state:
    st.session_state.npc = None

# Header
st.markdown("# 🎭 NPC FORGE")
st.markdown("### *Generate flavorful NPCs for your Tivmir campaign*")
st.markdown("---")

# Controls
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    region = st.selectbox(
        "Region Flavor",
        ["any", "urban", "rural", "frontier", "underdark", "seafaring", "desert", "arctic", "religious"],
        format_func=lambda x: x.replace("_", " ").title() if x != "any" else "Any"
    )

with col2:
    tone = st.selectbox(
        "Tone",
        ["any", "light", "grim", "mysterious"],
        format_func=lambda x: x.replace("_", " ").title() if x != "any" else "Any"
    )

with col3:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ GENERATE", use_container_width=True):
        st.session_state.npc = generate_npc(region, tone)
        st.rerun()

st.markdown("---")

# Display NPC
if st.session_state.npc:
    npc = st.session_state.npc
    
    # Main columns
    col_left, col_right = st.columns([1.5, 1])
    
    with col_left:
        # Identity Card
        st.markdown(f"<div class='npc-name'>{npc['name']}</div>", unsafe_allow_html=True)
        
        pills = f"""
        <div>
            <span class='pill pill-race'>{npc['race']}</span>
            <span class='pill pill-gender'>{npc['gender']}</span>
            <span class='pill pill-occupation'>{npc['occupation'].title()}</span>
        </div>
        """
        st.markdown(pills, unsafe_allow_html=True)
        
        st.markdown("<div class='section-header'>📋 Identity</div>", unsafe_allow_html=True)
        
        id_col1, id_col2 = st.columns(2)
        with id_col1:
            st.markdown(f"<div class='info-label'>Race</div><div class='info-value'>{npc['race']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='info-label'>Gender</div><div class='info-value'>{npc['gender']}</div>", unsafe_allow_html=True)
        with id_col2:
            st.markdown(f"<div class='info-label'>Occupation</div><div class='info-value'>{npc['occupation'].title()}</div>", unsafe_allow_html=True)
            deity_text = "None / no patron"
            if npc['deity']:
                deity_text = npc['deity']['name']
            st.markdown(f"<div class='info-label'>Deity</div><div class='info-value'>{deity_text}</div>", unsafe_allow_html=True)
        
        # Personality & Hooks
        st.markdown("<div class='section-header'>🧠 Personality & Hooks</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-label'>Personality</div><div class='info-value'>{npc['personality']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-label'>Goal</div><div class='info-value'>{npc['goal']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-label'>Secret</div><div class='info-value'>{npc['secret']}</div>", unsafe_allow_html=True)
    
    with col_right:
        # Appearance
        st.markdown("<div class='section-header'>👁️ Appearance</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-value'>{npc['appearance']}</div>", unsafe_allow_html=True)
        
        # Deity Details
        if npc['deity']:
            st.markdown("<div class='section-header'>⚜️ Deity Details</div>", unsafe_allow_html=True)
            deity_pill = f"<span class='pill pill-deity'>{npc['deity']['name']}</span>"
            st.markdown(deity_pill, unsafe_allow_html=True)
            st.markdown(f"<div class='info-label'>{npc['deity']['title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='info-value'>{npc['deity']['flavor']}</div>", unsafe_allow_html=True)
        
        # DM Notes
        st.markdown("<div class='section-header'>✍️ DM Notes</div>", unsafe_allow_html=True)
        dm_notes = st.text_area("Your notes", height=100, 
                                placeholder="Add relationships, plot hooks, or how this NPC connects to your campaign...")
        
        # Copy button
        npc_text = format_npc_text(npc)
        if st.button("📋 Copy NPC as Text", use_container_width=True):
            st.code(npc_text, language=None)
            st.success("✅ NPC details shown above - copy to clipboard manually")
    
    st.markdown("---")
    st.markdown("*Tip: Click Generate again for a new NPC • Built for Tivmir homebrew 5e*")

else:
    st.info("👆 Click **Generate** to create your first NPC!")
    st.markdown("""
    This generator creates complete NPCs for your Tivmir campaign:
    - **Identity**: Name, race, gender, occupation, deity
    - **Personality**: Traits, goals, and secrets
    - **Appearance**: Physical description
    - **Customization**: Filter by region and tone
    """)
