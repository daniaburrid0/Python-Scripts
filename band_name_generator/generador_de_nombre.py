import random

# Ask the user for some information
genre = input("What genre of music do you like? ")
adjective = input("Give me an adjective to describe the band: ")
animal = input("What's your favorite animal? ")

# Generate a random band name
band_name = f"The {adjective.capitalize()} {animal.capitalize()}s"

# Print the band name
print(f"Your band name is: {band_name}")

# Generate a few more band names
for i in range(3):
    adjective = random.choice(["Electric", "Funky", "Psychedelic", "Soulful"])
    animal = random.choice(["Lions", "Tigers", "Bears", "Wolves"])
    band_name = f"The {adjective} {animal}"
    print(f"Another band name: {band_name}")