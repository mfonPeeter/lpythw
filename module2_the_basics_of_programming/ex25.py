# Step 1
# def print_number(x):
#     print('NUMBER IS', x)

# rename_print = print_number
# rename_print(100)
# print_number(100)

# Step 2
# color = "Red"
# corvette = {
#     'color': color
# }
# print("LITTLE", corvette['color'], 'CORVETTE')

# Step 3
# def run(): 
#     print('VROOM')

# corvette = {
#     "color": "Red", 
#     "run": run
# }

# print("My", corvette["color"], "can go")
# corvette["run"]()

# Study Drill
def create_car(name, color, speed):
    settings = {
        "name": name,
        "color": color,
        "speed": speed
    }
    return settings

volvo = create_car('Volvo', 'Blue', 200)
camry = create_car('Camry', 'Red', 300)

print(volvo)
print(camry)
