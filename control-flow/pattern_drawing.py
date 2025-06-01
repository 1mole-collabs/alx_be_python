# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the square pattern using a while loop
while row < size:
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
    row += 1
