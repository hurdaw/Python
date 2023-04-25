def digits(n):
    count = 0
    if n == 0:
        count += 1
    while n > 0:  # Complete the while loop condition
        # Complete the body of the while loop. This should include
        # performing a calculation and incrementing a variable in the
        # appropriate order.
        n //= 10
        count += 1
    return count


def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop+1):
        # Complete the inner loop range
        for y in range(start, stop+1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()
    # 1 2 3
    # 2 4 6
    # 3 6 9


def counter(start, stop):
    if start >= stop:
        return_string = "Counting down: "
        while start >= stop:  # Complete the while loop
            # Add the numbers to the "return_string"
            return_string += str(start) + ","
            start -= 1  # Increment the appropriate variable
        return return_string[:-1]
    else:
        return_string = "Counting up: "
        while start <= stop:  # Complete the while loop
            # Add the numbers to the "return_string"
            return_string += str(start) + ","
            start += 1  # Increment the appropriate variable
        return return_string[:-1]

# for left in range(7):
#     for right in range(left, 7):
#         print("["+str(left)+"|"+str(right) + "]", end=" ")
#     print()

# def count_users(group):
#     count = 0
#     for member in get_members(group):
#         count += 1
#         if is_group(member):
#             count += count_users(member)
#     return count


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.
def sum_divisors(number):
    # Initialize the appropriate variables
    divisor = 1
    total = 0
    # Avoid dividing by 0 and negative numbers
    # in the while loop by exiting the function
    # if "number" is less than one
    if number < 1:
        return 0

    # Complete the while loop
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        # Increment the correct variable
        divisor += 1
    # Return the correct variable
    return total


def is_power_of_two(number):
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder. How can you change the while loop to
    # avoid a Python ZeroDivisionError?
    while number % 2 == 0:
        number = number / 2

    # If after dividing by 2 "number" equals 1, then "number" is a power
    # of 2.
    if number == 1:
        return True
    return False


def digits(n):
    count = 0
    if n == 0:
        count += 1
    while n > 0:  # Complete the while loop condition
        # Complete the body of the while loop. This should include
        # performing a calculation and incrementing a variable in the
        # appropriate order.
        n //= 10
        count += 1
    return count


def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop+1):
        # Complete the inner loop range
        for y in range(start, stop+1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()
    # 1 2 3
    # 2 4 6
    # 3 6 9


def counter(start, stop):
    if start >= stop:
        return_string = "Counting down: "
        while start >= stop:  # Complete the while loop
            # Add the numbers to the "return_string"
            return_string += str(start) + ","
            start -= 1  # Increment the appropriate variable
        return return_string[:-1]
    else:
        return_string = "Counting up: "
        while start <= stop:  # Complete the while loop
            # Add the numbers to the "return_string"
            return_string += str(start) + ","
            start += 1  # Increment the appropriate variable
        return return_string[:-1]

# for left in range(7):
#     for right in range(left, 7):
#         print("["+str(left)+"|"+str(right) + "]", end=" ")
#     print()

# def count_users(group):
#     count = 0
#     for member in get_members(group):
#         count += 1
#         if is_group(member):
#             count += count_users(member)
#     return count


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.
def sum_divisors(number):
    # Initialize the appropriate variables
    divisor = 1
    total = 0
    # Avoid dividing by 0 and negative numbers
    # in the while loop by exiting the function
    # if "number" is less than one
    if number < 1:
        return 0

    # Complete the while loop
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        # Increment the correct variable
        divisor += 1
    # Return the correct variable
    return total


def is_power_of_two(number):
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder. How can you change the while loop to
    # avoid a Python ZeroDivisionError?
    while number % 2 == 0:
        number = number / 2

    # If after dividing by 2 "number" equals 1, then "number" is a power
    # of 2.
    if number == 1:
        return True
    return False


def network(servers):
    result = ""
    for host_servers, ip_address in servers.items():
        result += "The IP address of the {} server is {} \n".format(
            host_servers, ip_address)
    return result
# print(network({"Domain Name Server": "8.8.8.8", "Gateway Server": "192.168.1.1",
#       "Print Server": "192.168.1.33", "Mail Server": "192.168.1.190"}))
