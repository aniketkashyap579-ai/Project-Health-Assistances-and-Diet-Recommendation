def bmi_calculator(weight, height):
    bmi = weight / ((height/100) ** 2)
    return round(bmi, 2)

def bmr_calculator(gender, age, weight, height):
    if gender== "Male":
        bmr=(10*weight)+(6.25*height)-(5*age)+5
        return bmr
    elif gender== "Female":
        bmr=(10*weight)+(6.25*height)-(5*age)-161
        return bmr


def tdee_calculator(bmr, activity):
          activity_factors={"Sedentary":1.20,
                            "Lightly active":1.375,
                            "Moderately active":1.55,
                            "Very active":1.725,
                            "Extra active":1.90}

          tdee=bmr*activity_factors[activity]
          return round(tdee,2)
def calorie_target(tdee,aim):
     if aim == "Weight maintain":
          calorie=tdee
     elif aim == "Weight loss":
          calorie=tdee-400
     elif aim == "Weight gain":
          calorie=tdee+300
     return round(calorie,2)

# print(bmi_calculator(60,150))
# bmr=bmr_calculator("male", 25, 60, 150)
# tdee=tdee_calculator(bmr,"Very active")
# print(calorie_target(tdee,"Weight loss"))