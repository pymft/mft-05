# bmi= mass / (height * height)
mass = input("mass (kg)")
height = input("height (m)")

mass = float(mass)
height = float(height)

body_mass_index = mass / height ** 2

print(body_mass_index)
