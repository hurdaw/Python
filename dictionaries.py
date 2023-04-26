# file_count = {"jpg": [10], "exe": 5, "txt": 3}
# print(file_count)
# i = file_count["exe"]
# file_count["csv"] = 9
# del file_count["csv"]
# print(file_count)


def items():
    file_count = {"jpg": 10, "exe": 5, "txt": 3, "py": 243, "mp3": 5}
    for extension in file_count:
        print(extension)
    for ext, amount in file_count.items():
        print("there are {} files with the .{} extension".format(amount, ext))
    print(file_count.keys())
    print(file_count.values())
    for value in file_count.keys():
        print(value)


# items()

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
# print(count_letters("teanant"))


def sum_server_use(server):
    total = 0.0
    for key, value in server.items():
        if isinstance(value, list):
            total += sum(server[key])
        else:
            total += server[key]
    return total
# server = {"EndUser1": [2.25, 5.2], "EndUser2": 4.5, "EndUser3": 1,
#           "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
# print(sum_server_use(server))


def list_full_names(employee):
    full_names = []
    for last_name, first_names in employee.items():
        for first_name in first_names:
            full_names.append(first_name + " " + last_name)
    return (full_names)


# print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": [
#       "Ram", "Amaira"], "Chen": ["Feng", "Li"]}))

# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#         "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}


def invert_resource_dict(pc):
    new_resource = {}
    for resource_key, resource_value in pc.items():
        for source in resource_value:
            if source in new_resource:
                new_resource[source].append(resource_key)
            else:
                new_resource[source] = [resource_key]
    return new_resource


# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#                             "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))

def email_list(domains):
    emails = []
    for domain_name, users in domains.items():
        for user in users:
            emails.append(user+"@"+domain_name)
    return (emails)


# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
#       "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group_name, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user in user_groups:
                user_groups[user].append(group_name)
            else:
                user_groups[user] = [group_name]
    return (user_groups)


# print(groups_per_user({"local": ["admin", "userA"],
#                        "public":  ["admin", "userB"],
#                        "administrator": ["admin"]}))
def sales_prices(item_and_price):
    items = ""
    price = ""
    item_or_price = item_and_price.split()
    for i in item_or_price:
        if i.isalpha():
            items += i+" "
        else:
            price = i
    items = items.strip()

    return "{} are on sale {}".format(items, price)
# print(sales_prices("Winter fleece jackets 49.99"))


def network(servers):
    result = ""
    for host_servers, ip_address in servers.items():
        result += "The IP address of the {} server is {} \n".format(
            host_servers, ip_address)
    return result


# print(network({"Domain Name Server": "8.8.8.8", "Gateway Server": "192.168.1.1",
#       "Print Server": "192.168.1.33", "Mail Server": "192.168.1.190"}))
# file_count = {"jpg": [10], "exe": 5, "txt": 3}
# print(file_count)
# i = file_count["exe"]
# file_count["csv"] = 9
# del file_count["csv"]
# print(file_count)


def items():
    file_count = {"jpg": 10, "exe": 5, "txt": 3, "py": 243, "mp3": 5}
    for extension in file_count:
        print(extension)
    for ext, amount in file_count.items():
        print("there are {} files with the .{} extension".format(amount, ext))
    print(file_count.keys())
    print(file_count.values())
    for value in file_count.keys():
        print(value)


# items()

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
# print(count_letters("teanant"))


def sum_server_use(server):
    total = 0.0
    for key, value in server.items():
        if isinstance(value, list):
            total += sum(server[key])
        else:
            total += server[key]
    return total
# server = {"EndUser1": [2.25, 5.2], "EndUser2": 4.5, "EndUser3": 1,
#           "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
# print(sum_server_use(server))


def list_full_names(employee):
    full_names = []
    for last_name, first_names in employee.items():
        for first_name in first_names:
            full_names.append(first_name + " " + last_name)
    return (full_names)


# print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": [
#       "Ram", "Amaira"], "Chen": ["Feng", "Li"]}))

# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#         "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}


def invert_resource_dict(pc):
    new_resource = {}
    for resource_key, resource_value in pc.items():
        for source in resource_value:
            if source in new_resource:
                new_resource[source].append(resource_key)
            else:
                new_resource[source] = [resource_key]
    return new_resource


# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#                             "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))

def email_list(domains):
    emails = []
    for domain_name, users in domains.items():
        for user in users:
            emails.append(user+"@"+domain_name)
    return (emails)


# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
#       "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group_name, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user in user_groups:
                user_groups[user].append(group_name)
            else:
                user_groups[user] = [group_name]
    return (user_groups)


# print(groups_per_user({"local": ["admin", "userA"],
#                        "public":  ["admin", "userB"],
#                        "administrator": ["admin"]}))
def sales_prices(item_and_price):
    items = ""
    price = ""
    item_or_price = item_and_price.split()
    for i in item_or_price:
        if i.isalpha():
            items += i+" "
        else:
            price = i
    items = items.strip()

    return "{} are on sale {}".format(items, price)
# print(sales_prices("Winter fleece jackets 49.99"))


def network(servers):
    result = ""
    for host_servers, ip_address in servers.items():
        result += "The IP address of the {} server is {} \n".format(
            host_servers, ip_address)
    return result


# print(network({"Domain Name Server": "8.8.8.8", "Gateway Server": "192.168.1.1",
#       "Print Server": "192.168.1.33", "Mail Server": "192.168.1.190"}))

def format_address(address_string):

    house_number = ""
    street_name = ""

    # Separate the house number from the street name.
    address_parts = address_string.split()

    for address_part in address_parts:
        # Complete the if-statement with a string method.
        if address_part.isnumeric():
            house_number = address_part
        else:
            street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = "House number {} on a street name {} ".format(
        house_number, street_name)

    # Use a string method to return the required formatted string.
    return street_name


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"
