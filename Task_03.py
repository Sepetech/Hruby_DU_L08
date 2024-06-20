with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

with open("output.txt", "w") as output_file:
    for i, line in enumerate(lines):
        if i < len(lines) - 1:  # don't write the last line
            output_file.write(line)
