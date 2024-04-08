items = list(range(1, 101))  # Creating a list of 100 items for demonstration

print(items)
# Printing in five parts
part_size = 4

for i in range(0, len(items), part_size):
    print("Part:")
    for j in range(part_size):
        index = i + j
        if index < len(items):
            print(index)