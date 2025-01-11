import streamlit as st

# Language options
LANGUAGES = {
    "Hungarian": {
        "title": "AgroGlance Kalkulátor",
        "num_fields": "Hány földdel rendelkezik, vagy szeretné használni a szolgáltatást?",
        "field_data": "{}. föld adatai",
        "area_size": "Területméret (hektár):",
        "passes": "Átjárások száma:",
        "pricing": "### Árak átjárásonként:",
        "total_price": "**Összesen: {:.2f} EUR**",
        "summary_price": "Összesített ár",
        "final_price": "**Teljes ár: {:.2f} EUR**",
        "total_area": "Teljes terület: {:.2f} hektár",
        "bonuses": "Átjárásonkénti Bónuszok (Ingyenes)",
        "contact": "Kapcsolat",
        "contact_info": (
            "Ha kérdése van, keressen minket bizalommal:\n"
            "**Imre Gyaraki**\n"
            "📞 +36 30 720 8887\n"
            "📧 imregyaraki@agroglance.com"
        ),
        "passes_labels": ["1× Átjárás", "2× Átjárás", "3× Átjárás"],
        "website": "Látogasson el a weboldalunkra: [agroglance.com/hu](https://agroglance.com/hu)"
    },
    "English": {
        "title": "AgroGlance Calculator",
        "num_fields": "How many fields do you have or want to use the service for?",
        "field_data": "{}. Field Data",
        "area_size": "Field Size (hectares):",
        "passes": "Number of Passes:",
        "pricing": "### Prices per Pass:",
        "total_price": "**Total: {:.2f} EUR**",
        "summary_price": "Total Price",
        "final_price": "**Grand Total: {:.2f} EUR**",
        "total_area": "Total Area: {:.2f} hectares",
        "bonuses": "Bonuses by Pass (Free)",
        "contact": "Contact",
        "contact_info": (
            "If you have any questions, feel free to contact us:\n"
            "**Imre Gyaraki**\n"
            "📞 +36 30 720 8887\n"
            "📧 imregyaraki@agroglance.com"
        ),
        "passes_labels": ["1× Pass", "2× Passes", "3× Passes"],
        "website": "Visit our website: [agroglance.com](https://agroglance.com)"
    }
}

# Select language
language = st.sidebar.selectbox("Choose Language / Válasszon nyelvet", ["English", "Hungarian"])
lang = LANGUAGES[language]

def calculate_price_per_field(area, passes):
    """Calculate the price for each pass on a single field and return the detailed breakdown."""
    prices = [0, 0, 0]
    
    if area <= 3:
        prices = [300, 180, 70]
    elif area <= 5:
        prices = [300 + (area - 3) * 100, 180 + (area - 3) * 30, 70 + (area - 3) * 20]
    elif area <= 10:
        prices = [500 + (area - 5) * 50, 240 + (area - 5) * 24, 110 + (area - 5) * 6]
    else:
        prices = [
            750 + (area - 10) * 30, 
            360 + (area - 10) * 18, 
            140 + (area - 10) * 7
        ]
    
    total_price = sum(prices[:passes])
    return prices[:passes], total_price

def get_bonuses():
    """Return the bonuses for all passes."""
    bonuses = {
        1: [
            "Weed detection and distribution map (free)",
            "Map-based report (free)",
            "Speed (results on the same day, free)",
            "PDF reports (free)",
            "Sowing error mapping (free)",
            "Guide for uploading Prescription Map (free)"
        ],
        2: [
            "Stand count (free)",
            "Yield forecasting (free)",
            "Damage report for insurers (free)"
        ],
        3: [
            "Mapping drainage issues (free)",
            "Complex report package (free)",
            "RTK support (free)",
            "Interpretation support in practice (free)"
        ]
    }
    return bonuses

st.title(lang["title"])
# Display website link prominently
st.markdown(f"### {lang['website']}")

num_fields = st.number_input(lang["num_fields"], min_value=1, step=1)

# --- ADD THIS SECTION FOR A "GLOBAL PASSES" SELECTOR ---
st.subheader("Set Number of Passes (Átjárások) for All Fields at Once")
global_pass_selection = st.radio(
    label=lang["passes"], 
    options=[1, 2, 3], 
    horizontal=True,
    key="global_pass_selection"
)
if st.button("Apply Passes to All Fields"):
    # Once clicked, store the selected value in each field's session state
    for i in range(num_fields):
        st.session_state[f"passes_{i}"] = global_pass_selection
# --------------------------------------------------------

total_price = 0
total_area = 0

# Main loop through fields
for i in range(num_fields):
    st.subheader(lang["field_data"].format(i + 1))
    
    # Field area
    area = st.number_input(lang["area_size"], key=f"area_{i}", min_value=0.1, step=0.1)
    
    # Field passes (read from session_state if it’s there, otherwise default = 1)
    default_passes = st.session_state.get(f"passes_{i}", 1)
    passes = st.selectbox(
        lang["passes"], 
        [1, 2, 3],
        index=[1,2,3].index(default_passes),  # ensures the selectbox shows the correct default
        key=f"passes_{i}"
    )
    
    # Calculate price for this field
    prices, field_total = calculate_price_per_field(area, passes)
    
    # Display detailed pricing
    st.write(lang["pricing"])
    for idx, price in enumerate(prices, start=1):
        st.write(f"- {idx}. {lang['passes_labels'][idx-1]}: {price:.2f} EUR")
    st.write(lang["total_price"].format(field_total))
    
    total_price += field_total
    total_area += area

# Summary
st.subheader(lang["summary_price"])
st.write(lang["final_price"].format(total_price))
st.write(lang["total_area"].format(total_area))

# Bonuses section
st.write("---")
st.subheader(lang["bonuses"])
bonuses = get_bonuses()
cols = st.columns(3)  # Create 3 columns for the bonuses
for idx, (col, (pass_num, bonus_list)) in enumerate(zip(cols, bonuses.items()), start=1):
    with col:
        st.write(f"**{lang['passes_labels'][pass_num - 1]}**")
        for bonus in bonus_list:
            st.write(f"- {bonus}")

# Contact information
st.write("---")
st.subheader(lang["contact"])
st.write(lang["contact_info"])
