chai_types={"Masala": "Spicy", "Ginger":"Zesty", "Green": "Mild"}
print(chai_types)

print(chai_types["Green"])
print("..............")

print(chai_types.get("Ginger"))
print("..............")
chai_types["Green"]= "Banan"
print(chai_types)

print("..............")

for chai in chai_types:
    print(chai)
    
print("..............")    
for chai in chai_types:
    print(chai, chai_types[chai])
    
    
print("..............")
for key, values in chai_types.items():
    print(key, values)

print("..............")

print(len(chai_types))

print("..............")

chai_types["Earl Grey"]= "citrus"
print(chai_types)

print("..............")

chai_types.pop("Ginger")
print(chai_types)


print("..............")
information={
    "person1":{
        "name":"Nishan Kumar Rai",
        "age":26,
        "gender":"Male",
        "email": "infonkumarrai323@gmail.com",
        "isActive":False
    },
    "person2":{
        "name":"Alisha Gurung",
        "age":26,
        "gender":"Female",
        "email": "alishagrg467@gmail.com",
        "isActive":True
    },
}
print(information["person1"]["email"])
print("..............")


num = {x:x**2 for x in range(6)}
print(num)

print("..............")
keys = ["Name", "Address", "Phone Number", "Country", "isActive"]

default_value ="Enter your info...."

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
