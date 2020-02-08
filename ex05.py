name = 'Moosedemeanor'
age = 30
height = 69 # inches
height_cm = float(round(height / 2.54, 2))
weight = 175 # lbs
weight_kg = float(round(weight / 2.205, 2))
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
