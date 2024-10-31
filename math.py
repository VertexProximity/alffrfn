import mpmath

# Set the precision to generate 100 million digits
mpmath.mp.dps = 100_000_000

# Calculate pi
pi_digits = str(mpmath.pi)

# Write pi digits to a file
with open("pi_digits.txt", "w") as file:
    file.write(pi_digits)

