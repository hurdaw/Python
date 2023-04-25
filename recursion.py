def printFun(test):
    if (test < 1):
        return
    else:
        print(test, end=" ")
        printFun(test-1)  # statement 2
        print(test, end=" ")
        return


def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number/base, base)


def sum_positive_numbers(n):
    if n < 1:
        return 0
    return n + sum_positive_numbers(n-1)
