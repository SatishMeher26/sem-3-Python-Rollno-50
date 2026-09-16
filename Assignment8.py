# Assignment 8 - File Handling

def count_lines(filename):
    with open(filename, "r") as f:
        count = 0
        for line in f:
            count += 1
    return count


def first_two_lines(filename):
    lines = []

    with open(filename, "r") as f:
        for i, line in enumerate(f):
            if i >= 2:
                break
            lines.append(line)

    return lines


def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)


# Creating input file
with open("input.txt", "w") as f:
    f.write("Hello, this is first line.\n")
    f.write("This is the second line.\n")
    f.write("This is the third line.\n")
    f.write("This is the fourth line.\n")
    f.write("This is the fifth line.\n")


# Count lines
total = count_lines("input.txt")
print("Total number of lines:", total)

# Get first two lines
lines = first_two_lines("input.txt")

print("\nFirst two lines:")
for line in lines:
    print(line.strip())

# Write them into new file
write_file("output.txt", lines)

print("\nFirst two lines written to output.txt")