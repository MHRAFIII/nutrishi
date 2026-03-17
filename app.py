import streamlit as st

# 📱 Page config (important for mobile)
st.set_page_config(
    page_title="MET Calculator",
    layout="centered"
)

# 🔥 MET values
MET_VALUES = {
    "walking_slow": 2.0,
    "walking_normal": 3.5,
    "walking_brisk": 5.0,
    "running_8kmh": 8.0,
    "cycling_moderate": 6.0,
    "yoga": 2.5,
    "cleaning": 3.5,
    "stairs": 8.0,
    "jump_rope": 10.0,
    "football_casual": 7.0,
    "basketball": 8.0
}

# 🧠 Normalize
def normalize_input(x):
    return x.strip().lower().replace(" ", "_")

# 🎨 Title
st.title("🔥 MET Calories Calculator")

st.markdown("### 📱 Simple & Mobile Friendly")

# 🔽 Friendly dropdown labels
friendly_names = {
    "Walking (Slow)": "walking_slow",
    "Walking (Normal)": "walking_normal",
    "Walking (Brisk)": "walking_brisk",
    "Running (8 km/h)": "running_8kmh",
    "Cycling (Moderate)": "cycling_moderate",
    "Yoga": "yoga",
    "Cleaning": "cleaning",
    "Stairs": "stairs",
    "Jump Rope": "jump_rope",
    "Football": "football_casual",
    "Basketball": "basketball"
}

# 📱 Big dropdown
selected_label = st.selectbox(
    "Choose Activity",
    list(friendly_names.keys())
)

# ✍️ Optional manual input
manual_input = st.text_input("Or type activity (optional)")

# 📱 Bigger inputs
weight = st.number_input("Weight (kg)", min_value=1.0, step=1.0)
time = st.number_input("Time (minutes)", min_value=1.0, step=1.0)

# 🚀 Calculate button
if st.button("🚀 Calculate Calories", use_container_width=True):

    if manual_input:
        activity = normalize_input(manual_input)
    else:
        activity = friendly_names[selected_label]

    if activity in MET_VALUES:
        calories = MET_VALUES[activity] * weight * (time / 60)

        st.success(f"🔥 {selected_label}")
        st.success(f"💪 {calories:.2f} kcal burned")
    else:
        st.error("❌ Activity not found")
