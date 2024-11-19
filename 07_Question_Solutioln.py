# Customize a coffee order: "Small","Medium", or "Large" with an option for "Extra shot" of espresson.

order_size = "Small"

extra_short=True



if extra_short:
    coffee = order_size + "coffee with an extra short"
else:
    coffee = order_size + "coffee"
print("Order:", coffee)