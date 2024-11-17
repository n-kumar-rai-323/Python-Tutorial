tea = ["black","green", "Masala", "white"]

for teas in tea:
    print(teas, end="s, ")

tea.append("yellow")
print(tea)

tea.remove("white")

tea.insert(0,"blue")

print(tea)
if "yellow" in tea:
    print("i have yellow color")
    
    
    
squared_nums =[x ** 2 for x in range(10)]
print(squared_nums)