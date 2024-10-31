import decimal
import multiprocessing

def calculate_part_pi(start, end):
    part_pi = decimal.Decimal(0)
    for k in range(start, end):
        part_pi += (decimal.Decimal(-1) ** k) / (1024 ** k) * (
            decimal.Decimal(256) / (10 * k + 1) +
            decimal.Decimal(1) / (10 * k + 9) -
            decimal.Decimal(64) / (10 * k + 3) -
            decimal.Decimal(32) / (4 * k + 1) -
            decimal.Decimal(4) / (10 * k + 5) -
            decimal.Decimal(4) / (10 * k + 7) -
            decimal.Decimal(1) / (4 * k + 3)
        )
    return part_pi

def calculate_pi(digits):
    decimal.getcontext().prec = digits + 2  # Set precision to digits + 2
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(calculate_part_pi, [(i*digits//num_processes, (i+1)*digits//num_processes) for i in range(num_processes)])
    pi = sum(results)
    return pi

if __name__ == "__main__":
    while True:
        try:
            digits = int(input("Enter the number of digits of pi to calculate: "))
            if digits <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    pi = calculate_pi(digits)
    print(f"Pi calculated to {digits} digits is:\n{pi}")
import decimal

def calculate_pi(digits):
    decimal.getcontext().prec = digits + 2  # Set precision to digits + 2
    pi = decimal.Decimal(0)
    for k in range(digits + 2):
        pi += (decimal.Decimal(-1) ** k) / (1024 ** k) * (
            decimal.Decimal(256) / (10 * k + 1) +
            decimal.Decimal(1) / (10 * k + 9) -
            decimal.Decimal(64) / (10 * k + 3) -
            decimal.Decimal(32) / (4 * k + 1) -
            decimal.Decimal(4) / (10 * k + 5) -
            decimal.Decimal(4) / (10 * k + 7) -
            decimal.Decimal(1) / (4 * k + 3)
        )
    return pi

if __name__ == "__main__":
    while True:
        try:
            digits = int(input("Enter the number of digits of pi to calculate: "))
            if digits <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    pi = calculate_pi(digits)
    print(f"Pi calculated to {digits} digits is:\n{pi}")

