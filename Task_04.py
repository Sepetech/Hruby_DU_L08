def nejdelsi_radek(filename):
    max_length = 0
    with open(filename, 'r') as f:
        for line in f:
            length = len(line.strip())
            if length > max_length:
                max_length = length
    return max_length

filename = 'zdroj_dat.txt'
print("Delka nejdelsiho radku je:", nejdelsi_radek(filename))
