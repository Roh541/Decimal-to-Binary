# Function to convert decimal to binary
def decimal_to_binary(n):
    # Handle the case where the input is 0
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        # Calculate remainder and quotient
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    
    return binary

# Input from user
decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)

print(f"The binary equivalent of {decimal_number} is {binary_number}")
