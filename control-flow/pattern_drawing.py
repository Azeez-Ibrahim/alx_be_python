pattern_size = int(input("Enter the size of the pattern: "))
size = pattern_size
while pattern_size > 0:
    row = size
    while row > 0:
        print("*", end="")
        row -= 1
    print()
    pattern_size -= 1
