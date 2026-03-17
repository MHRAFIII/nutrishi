#!/usr/bin/env python3

# MET values dictionary
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

    "weight_light": 3.0,
    "weight_moderate": 5.0,
    "weight_heavy": 6.0,

    "yoga": 2.5,
    "cleaning": 3.5,
    "cooking": 2.5,
    "gardening": 4.0,
    "stairs": 8.0,
    "jump_rope": 10.0
}


def normalize_input(user_input):
    """
    Normalize user input:
    - Convert to lowercase
    - Replace spaces with underscores
    """
    return user_input.strip().lower().replace(" ", "_")


def calculate_calories(met, weight, time_hours):
    return met * weight * time_hours


def get_valid_activity():
    """
    Keep asking until user enters a valid activity
    """
    while True:
        raw_activity = input("\nEnter activity: ")
        activity = normalize_input(raw_activity)

        if activity in MET_VALUES:
            return raw_activity, activity
        else:
            print("\n❌ Invalid activity.")
            print(f"👉 You entered: '{raw_activity}' → normalized to: '{activity}'")
            print("🔁 Please try again.")


def get_valid_number(prompt):
    """
    Keep asking until user enters a valid number
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid number. Please try again.")


def main():
    print("\n==== MET Calculator ====\n")

    print("Available activities:")
    for activity in MET_VALUES:
        print(f" - {activity}")

    # 🔁 Activity loop
    raw_activity, activity = get_valid_activity()

    # 🔁 Input loops for numbers
    weight = get_valid_number("Enter weight (kg): ")
    time_minutes = get_valid_number("Enter time (minutes): ")
    time_hours = time_minutes / 60

    met = MET_VALUES[activity]
    calories = calculate_calories(met, weight, time_hours)

    print("\n==== Result ====")
    print(f"Original Input: {raw_activity}")
    print(f"Normalized Input: {activity}")
    print(f"MET: {met}")
    print(f"Calories burned: {calories:.2f} kcal\n")


if __name__ == "__main__":
    main()
