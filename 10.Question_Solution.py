# Recommend a type of pet food based on the pet't species and age.(e.g., Dog:<2 years-Puppy food, Cat:>5 years- Senior cat food).

animal = "Dog"
year = 1

if (animal == "Dog" and year < 2):
    canGive = "Puppy Food"
elif (animal == "Cat" and year > 5):
    canGive = "Senior Cat Food"
else:
    canGive = "Invalid Data"

print(canGive)