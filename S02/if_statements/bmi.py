mass = float(input("mass (kg)"))
height = float(input("height (m)"))



if height > 10:
    height = height / 100


body_mass_index = mass / height ** 2
print(body_mass_index)


if body_mass_index < 18:
    print("Underweight")
elif body_mass_index < 25:
    print("Normal")
elif body_mass_index < 30:
    print("Overweight")
else:
    print("Obese")

