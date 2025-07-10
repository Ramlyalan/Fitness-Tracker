def analyze_fitness(height, weight, age):
    bmi = weight / ((height / 100) ** 2)
    water_intake = weight * 0.033  # in liters

    if bmi < 18.5:
        status = "lean"
        advice = "Eat more calorie-dense foods and strength-train to gain muscle."
        exercise = "Moderate weight training, yoga, and calorie surplus diet."
    elif 18.5 <= bmi <= 24.9:
        status = "fit"
        advice = "Maintain your current lifestyle and diet."
        exercise = "Cardio + strength training 3–4 times a week."
    else:
        status = "overweight"
        advice = "Follow a calorie-deficit diet and increase physical activity."
        exercise = "Daily walking, HIIT, and portion-controlled meals."

    return {
        "bmi": round(bmi, 2),
        "water_intake": round(water_intake, 2),
        "status": status,
        "advice": advice,
        "exercise": exercise
    }