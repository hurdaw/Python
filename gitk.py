# List to be sorted
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Function to get the reference value for sorting


def get_reference_value(item):
    return item


# Sort the list using the reference value
my_list.sort(key=get_reference_value)

# Print the sorted list
print(my_list)
