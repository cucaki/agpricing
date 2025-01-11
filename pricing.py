import streamlit as st

# Language options
LANGUAGES = {
    "Hungarian": {
        "title": "AgroGlance Kalkulátor",
        "num_fields": "Hány földdel rendelkezik, vagy szeretné használni a szolgáltatást?",
        "field_data": "{}. föld adatai",
        "area_size": "Területméret (hektár):",
        "checks_label": "Ellenőrzések / Inspekciók száma:",
        "pricing": "### Árak ellenőrzésenként:",
        "total_price": "**Összesen: {:.2f} EUR**",
        "summary_price": "Összesített ár",
        "final_price": "**Teljes ár: {:.2f} EUR**",
        "total_area": "Teljes terület: {:.2f} hektár",
        "bonuses": "Ellenőrzésenkénti bónuszok (ingyenes)",
        "contact": "Kapcsolat",
        "contact_info": (
            "Ha kérdése van, keressen minket bizalommal:\n"
            "**Imre Gyaraki**\n"
            "📞 +36 30 720 8887\n"
            "📧 imregyaraki@agroglance.com"
        ),
        "checks_labels": ["1× Ellenőrzés", "2× Ellenőrzés", "3× Ellenőrzés"],
        "website": "Látogasson el a weboldalunkra: [agroglance.com/hu](https://agroglance.com/hu)",
        # Updated Hungarian heading for "global passes" => checks/inspections
        "global_passes_title": "Ellenőrzések / Inspekciók számának beállítása az összes földre",
        # Emphasize NEM for VAT
        "prices_excl_vat": "**A feltüntetett árak **NEM** tartalmazzák az ÁFÁt.**",
        "bonuses_dict": {
            1: [
                "Gyomfelismerés és eloszlási térkép (ingyenes)",
                "Térképalapú jelentés (ingyenes)",
                "Gyorsaság (ugyanazon a napon eredmények, ingyenes)",
                "PDF-jelentések (ingyenes)",
                "Vetési hibák feltérképezése (ingyenes)",
                "Útmutató a kijuttatási térkép feltöltéséhez (ingyenes)"
            ],
            2: [
                "Állományfelmérés (ingyenes)",
                "Hozambecslés (ingyenes)",
                "Káresemény jelentés biztosítók felé (ingyenes)"
            ],
            3: [
                "Vízelvezetési problémák feltérképezése (ingyenes)",
                "Komplex jelentéscsomag (ingyenes)",
                "RTK támogatás (ingyenes)",
                "Gyakorlati értelmezési támogatás (ingyenes)"
            ]
        }
    },
    "English": {
        "title": "AgroGlance Calculator",
        "num_fields": "How many fields do you have or want to use the service for?",
        "field_data": "{}. Field Data",
        "area_size": "Field Size (hectares):",
        "checks_label": "Number of Checks/Inspections:",
        "pricing": "### Prices per Check/Inspection:",
        "total_price": "**Total: {:.2f} EUR**",
        "summary_price": "Total Price",
        "final_price": "**Grand Total: {:.2f} EUR**",
        "total_area": "Total Area: {:.2f} hectares",
        "bonuses": "Bonuses by Check/Inspection (Free)",
        "contact": "Contact",
        "contact_info": (
            "If you have any questions, feel free to contact us:\n"
            "**Imre Gyaraki**\n"
            "📞 +36 30 720 8887\n"
            "📧 imregyaraki@agroglance.com"
        ),
        "checks_labels": ["1× Check", "2× Checks", "3× Checks"],
        "website": "Visit our website: [agroglance.com](https://agroglance.com)",
        # Updated English heading
        "global_passes_title": "Set Number of Checks/Inspections for All Fields",
        # Emphasize DO NOT for VAT
        "prices_excl_vat": "**The indicated prices **DO NOT** include VAT.**",
        "bonuses_dict": {
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
    }
}


def calculate_price_per_field(area, checks):
    """
    Calculate the price for each check/inspection on a single field
    and return the detailed breakdown.
    """
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
    
    total_price = sum(prices[:checks])
    return prices[:checks], total_price

# Let user pick language in the sidebar
language_choice = st.sidebar.selectbox("Choose Language / Válasszon nyelvet", ["English", "Hungarian"])
lang = LANGUAGES[language_choice]

# Single main title (language-specific)
st.title(lang["title"])
st.markdown(f"### {lang['website']}")

# Number of fields
num_fields = st.number_input(lang["num_fields"], min_value=1, step=1)

# --- Global Checks/Inspections Selector ---
st.subheader(lang["global_passes_title"])
global_pass_selection = st.radio(
    label=lang["checks_label"],
    options=[1, 2, 3],
    index=2,  # default=3 checks
    horizontal=True,
    key="global_pass_selection"
)
if st.button("Apply to All Fields"):
    for i in range(num_fields):
        st.session_state[f"checks_{i}"] = global_pass_selection
# -----------------------------------------

total_price = 0
total_area = 0

for i in range(num_fields):
    st.subheader(lang["field_data"].format(i + 1))
    
    # Default area = 20 hectares if none set
    if f"area_{i}" not in st.session_state:
        st.session_state[f"area_{i}"] = 20.0
        
    # Default checks/inspections = 3 if none set
    if f"checks_{i}" not in st.session_state:
        st.session_state[f"checks_{i}"] = 3
    
    # Field size
    area = st.number_input(
        lang["area_size"],
        key=f"area_{i}",
        min_value=0.1,
        step=0.1
    )
    
    # Number of checks/inspections
    checks = st.selectbox(
        lang["checks_label"],
        [1, 2, 3],
        key=f"checks_{i}"
    )
    
    # Calculate the price
    prices, field_total = calculate_price_per_field(area, checks)
    
    # Display pricing
    st.write(lang["pricing"])
    for idx, price in enumerate(prices, start=1):
        st.write(f"- {idx}. {lang['checks_labels'][idx-1]}: {price:.2f} EUR")
    
    # Display total cost for this field
    st.write(lang["total_price"].format(field_total))
    
    # Show cost breakdown
    if area > 0:
        cost_per_hectare_total = field_total / area
        cost_per_hectare_per_check = cost_per_hectare_total / checks
        
        if language_choice == "Hungarian":
            # Hungarian version
            # e.g.: 26.11 EUR/hektár ellenőrzésenként (78.33 EUR/hektár összesen)
            st.write(
                f"**{cost_per_hectare_per_check:.2f} EUR/hektár ellenőrzésenként** "
                f"({cost_per_hectare_total:.2f} EUR/hektár összesen)"
            )
        else:
            # English version
            # e.g.: 26.11 EUR/hectare per check (78.33 EUR/hectare total)
            st.write(
                f"**{cost_per_hectare_per_check:.2f} EUR/hectare per check** "
                f"({cost_per_hectare_total:.2f} EUR/hectare total)"
            )
    
    total_price += field_total
    total_area += area

# Summary
st.subheader(lang["summary_price"])
st.write(lang["final_price"].format(total_price))
if total_area > 0:
    # Show average total cost per hectare (we can't strictly do "per check" across fields
    # since each field can have different # checks)
    avg_cost_per_hectare = total_price / total_area
    if language_choice == "Hungarian":
        st.write(f"**{avg_cost_per_hectare:.2f} EUR/hektár összesen**")
    else:
        st.write(f"**{avg_cost_per_hectare:.2f} EUR/hectare total**")

st.write(lang["total_area"].format(total_area))

# Show disclaimer for VAT
st.write(lang["prices_excl_vat"])

# Bonuses Section
st.write("---")
st.subheader(lang["bonuses"])
bonuses = lang["bonuses_dict"]  # Language-specific bonuses
cols = st.columns(3)
for idx, (col, (check_num, bonus_list)) in enumerate(zip(cols, bonuses.items()), start=1):
    with col:
        st.write(f"**{lang['checks_labels'][check_num - 1]}**")
        for bonus in bonus_list:
            st.write(f"- {bonus}")

# Contact
st.write("---")
st.subheader(lang["contact"])
st.write(lang["contact_info"])
