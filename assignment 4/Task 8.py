user_input = input("Enter something: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
