# Prompt user for pattern size
length = int(input("Enter the size of the pattern: "))

# Draw the pattern
i = 0
while i < length:
    for j in range(length):
        print("*", end="")
    print()  # Move to the next line after completing a row
    i += 1  # Increment the while loop counter



