name = 'Zed A. Shaw'
age = 35 # not a lie
height_in = 74 # inches
height_cm = height_in * 2.54 # cm
weight_lbs = 180 # lbs
weight_kg = weight_lbs * 0.453592 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in} inches tall.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_lbs} pounds heavy.")
print(f"He's {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactl right
total = age + height_in + weight_lbs
print(f"If I add {age}, {height_in}, and {weight_lbs} I get {total}.")