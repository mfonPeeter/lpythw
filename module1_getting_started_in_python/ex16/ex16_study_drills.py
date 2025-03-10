from sys import argv

# Study Drill 2
script, file_name = argv

txt = open(file_name)

print(f"Here's your file {file_name}")
print(txt.read())

txt.close()

# Study Drill 3
filename = "test.txt"

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

updated_file_content = "{}\n{}\n{}"
target.write(updated_file_content.format(line1, line2, line3))

print("And finally, we close it.")
target.close()