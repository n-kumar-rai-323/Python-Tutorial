# Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15km:Bike, >15km:Car)

distance =5

if distance <3:
    transport = "walk"
elif distance <= 15:
    transport ="bike"
else:
    transport = "car"

print("AI recommends you the transport of :", transport)