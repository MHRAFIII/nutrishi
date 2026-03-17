import streamlit as st

MET_VALUES = {
    "walking_slow": 2.0,
    "walking_normal": 3.5,
    "walking_brisk": 5.0,
    "running_8kmh": 8.0,
    "running_10kmh": 10.0,
    "cycling_moderate": 6.0,
    "yoga": 2.5,
    "cleaning": 3.5,
    "stairs": 8.0,
}

def normalize_input(user_input):
    return user_input.strip().lower().replace(" ", "_")

st.title("🔥 MET Calories Calculator")

activity_input = st.text_input("Enter Activity (e.g. walking slow)")
weight = st.number_input("Enter Weight (kg)", min_value=1.0)
time = st.number_input("Enter Time (minutes)", min_value=1.0)

if st.button("Calculate"):
    activity = normalize_input(activity_input)

    if activity in MET_VALUES:
        calories = MET_VALUES[activity] * weight * (time / 60)
        st.success(f"Calories Burned: {calories:.2f} kcal")
    else:
        st.error(f"❌ Invalid activity: {activity}")
