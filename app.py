import streamlit as st

# 📱 Page config
st.set_page_config(page_title="MET Calculator", layout="centered")

# 🔥 FULL + EXTENDED MET DATABASE
MET_VALUES = {
    "sleeping": 0.9,
    "watching_tv": 1.0,
    "sitting": 1.5,
    "typing": 1.8,
    "standing": 2.0,

    "walking_slow": 2.0,
    "walking_normal": 3.5,
    "walking_brisk": 5.0,

    "running_8kmh": 8.0,
    "running_10kmh": 10.0,
    "running_12kmh": 12.5,

    "cycling_light": 4.0,
    "cycling_moderate": 6.0,
    "cycling_fast": 8.5,

    "swimming_light": 6.0,
    "swimming_moderate": 8.0,
    "swimming_vigorous": 10.0,

    "football_casual": 7.0,
    "football_competitive": 10.0,

    "basketball": 8.0,
    "badminton": 5.5,
    "tennis": 7.0,

    "weight_light": 3.0,
    "weight_moderate": 5.0,
    "weight_heavy": 6.0,

    "yoga": 2.5,
    "stretching": 2.3,

    "cleaning": 3.5,
    "cooking": 2.5,
    "gardening": 4.0,

    "stairs": 8.0,
    "jump_rope": 10.0,

    "dancing": 6.0,
    "hiking": 6.0,
    "rowing": 7.0
}

# 🧠 Normalize
def normalize_input(x):
    return x.strip().lower().replace(" ", "_")

# 🎨 Convert to friendly names automatically
def make_friendly(name):
    return name.replace("_", " ").title()

friendly_map = {make_friendly(k): k for k in MET_VALUES.keys()}

# 🎯 UI
st.title("🔥 MET Calories Calculator")
st.markdown("### 📱 Mobile Friendly & Easy to Use")

# 🔽 Dropdown (auto-generated)
selected_label = st.selectbox(
    "Choose Activity",
    list(friendly_map.keys())
)

# ✍️ Optional manual input
manual_input = st.text_input("Or type activity manually")

# 📱 Inputs
weight = st.number_input("Weight (kg)", min_value=1.0, step=1.0)
time = st.number_input("Time (minutes)", min_value=1.0, step=1.0)

# 🚀 Button
if st.button("🚀 Calculate Calories", use_container_width=True):

    if manual_input:
        activity = normalize_input(manual_input)
        display_name = manual_input
    else:
        activity = friendly_map[selected_label]
        display_name = selected_label

    if activity in MET_VALUES:
        calories = MET_VALUES[activity] * weight * (time / 60)

        st.success(f"🔥 Activity: {display_name}")
        st.success(f"💪 Calories Burned: {calories:.2f} kcal")
    else:
        st.error(f"❌ Invalid activity: {activity}")
