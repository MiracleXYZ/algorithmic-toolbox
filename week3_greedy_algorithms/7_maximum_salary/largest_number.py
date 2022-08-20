def largest_number(numbers):
    def is_better(number1, number2):
        # swap and compare
        return (number1 + number2) >= (number2 + number1)

    largest = []

    while numbers:
        max_number = "0"
        for number in numbers:
            if is_better(number, max_number):
                max_number = number
        largest.append(max_number)
        numbers.remove(max_number)

    return int("".join(largest))


if __name__ == "__main__":
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
