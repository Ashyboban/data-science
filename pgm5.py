print("\nGeorge Scaria SJC23MCA030")
print("MCA 2023-2025\n")

def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum

def main():
    try:
        num = int(input("Enter a positive number: "))
        if num <= 0:
            print("Please enter a positive number.")
            return
        while num > 0:
            current_sum = sum_of_digits(num)
            print(f"{num} - {current_sum} =", num - current_sum)
            num -= current_sum
    except ValueError:
        print("Invalid input. Please enter a valid positive number.")

if __name__ == "__main__":
    main()
