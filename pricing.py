import streamlit as st

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
            "Gyomfelismerés és gyom eloszlási térkép",
            "Térképes jelentés",
            "Gyorsaság (eredmények a repülés napján)",
            "PDF-riportok",
            "Vetési hibák feltérképezése",
            "Útmutató Prescription Map feltöltéséhez"
        ],
        2: [
            "Tőszámlálás",
            "Terméshozam-előrejelzés",
            "Kárjelentés biztosítóknak"
        ],
        3: [
            "Vízelvezetési problémák feltérképezése",
            "Komplex riport csomag",
            "RTK-támogatás",
            "Értelmezési támogatás a gyakorlatban"
        ]
    }
    return bonuses

st.title("AgroGlance Kalkulátor")

num_fields = st.number_input("Hány földdel rendelkezik, vagy szeretné használni a szolgáltatást?", min_value=1, step=1)
total_price = 0

for i in range(num_fields):
    st.subheader(f"{i+1}. föld adatai")
    area = st.number_input(f"Területméret (hektár):", key=f"area_{i}", min_value=0.1, step=0.1)
    passes = st.selectbox("Átjárások száma:", [1, 2, 3], key=f"passes_{i}")
    
    # Calculate price for this field
    prices, field_total = calculate_price_per_field(area, passes)
    
    # Display detailed pricing
    st.write("### Árak átjárásonként:")
    for idx, price in enumerate(prices, start=1):
        st.write(f"- {idx}. átjárás: {price:.2f} EUR")
    st.write(f"**Összesen: {field_total:.2f} EUR**")
    total_price += field_total

st.subheader("Összesített ár")
st.write(f"**Teljes ár: {total_price:.2f} EUR**")

# Add main service
st.write("---")
st.subheader("Fő Szolgáltatás")
st.write("**Kihagyott címerek felismerése** minden átjárással!")

# Add bonuses as a separate section
st.write("---")
st.subheader("Átjárásonkénti Bónuszok")
bonuses = get_bonuses()
cols = st.columns(3)  # Create 3 columns for the bonuses
for idx, (col, (pass_num, bonus_list)) in enumerate(zip(cols, bonuses.items()), start=1):
    with col:
        st.write(f"**{pass_num}× Átjárás**")
        if pass_num > 1:
            st.write("Minden korábbi bónusz +")
        for bonus in bonus_list:
            st.write(f"- {bonus}")

# Contact information
st.write("---")
st.subheader("Kapcsolat")
st.write(
    "Ha kérdése van, keressen minket bizalommal:\n"
    "**Imre Gyaraki**\n"
    "📞 +36 30 720 8887\n"
    "📧 imregyaraki@agroglance.com"
)
