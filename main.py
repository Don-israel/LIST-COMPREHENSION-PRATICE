# Input from the user
num = int(input("Enter a number: "))

# List of all odd numbers below the input value
odd_numbers_below = [x for x in range(1, num) if x % 2 != 0]

# List of odd numbers starting from 1 up to the input value
odd_numbers_upto = [x for x in range(1, num + 1) if x % 2 != 0]

print("Odd numbers below the input value:", odd_numbers_below)
print("Odd numbers up to the input value:", odd_numbers_upto)
