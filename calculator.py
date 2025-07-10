def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calories_burned(bmr, activity_level):
    return bmr * activity_level

def water_intake(weight):
    return round(weight * 0.033, 2)  # Liters

def exercise_plan(age):
    if age < 30:
        return "HIIT, Strength Training, Cardio"
    elif age < 50:
        return "Moderate Cardio, Weight Lifting"
    else:
        return "Walking, Yoga, Light Cardio"