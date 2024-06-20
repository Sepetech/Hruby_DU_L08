def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    for i in range(max(len(lines1), len(lines2))):
        line1 = lines1[i].strip() if i < len(lines1) else ''
        line2 = lines2[i].strip() if i < len(lines2) else ''

        if line1 != line2:
            print(f"File 1 (line {i+1}): {line1}")
            print(f"File 2 (line {i+1}): {line2}")
            print()

compare_files('file1.txt', 'file2.txt')
