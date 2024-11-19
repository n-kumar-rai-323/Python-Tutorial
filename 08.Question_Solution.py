# check if a password is "weak", "Medium", or "Strong". Criteria:<6 chares(Weak), 6-10 chars (Medium),>10 chars(Strong)

password = "Secure234"

if len(password) < 6:
    strength = "week"
elif len(password) <=10:
    strength = "medium"
else:
    strength = "strong"

print("Paassword strength is : ", strength)