from dis import dis

def generate_numbers(limit, step): 
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += step

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

 
    return numbers



numbers = generate_numbers(6, 2)
print("The numbers: ")
for num in numbers: 
    print(num)

# dis('''
# i = 0
# while i < 6:
#     i = i + 1
# ''')

# Study Drills
