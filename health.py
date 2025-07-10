def calculate_bmi(weight, height):
    if height == 0:
        return 0
    return round(weight / ((height / 100) ** 2), 2)

def calculate_water(weight):
    return round(weight * 0.033, 2)

def calculate_calories(weight, age):
    return round((10 * weight + 6.25 * 170 - 5 * age + 5), 2)

def recommend_exercise(age):
    if age < 30:
        return ["Running", "HIIT", "Swimming"]
    elif age < 50:
        return ["Jogging", "Yoga", "Cycling"]
    else:
        return ["Walking", "Stretching", "Water aerobics"]