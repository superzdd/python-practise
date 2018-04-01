def create_groups(items, num_groups):
    groups = []
    try:
        size = len(items) // num_groups
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
    except ZeroDivisionError:
        print('WARNING: Returning empty list. Please use a nonzero number.')

    print("{} groups returned.".format(num_groups))
    return groups

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))
