import difflib  # Importing the difflib module for sequence matching


def read_file(file_path):
    # Read the contents of a file and return a list of lines
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def mode_1(input_lines, pattern_lines):
    # Mode 1: Output lines from input.txt that match exactly any pattern in patterns.txt
    return [line for line in input_lines if line in pattern_lines]


def mode_2(input_lines, pattern_lines):
    # Mode 2: Output lines from input.txt that contain a match with any pattern in patterns.txt somewhere in the line
    matches = []
    for line in input_lines:
        if any(pattern in line for pattern in pattern_lines):
            matches.append(line)
    return matches


def mode_3(input_lines, pattern_lines):
    # Mode 3: Output lines from input.txt that match with any pattern in patterns.txt with edit distance <= 1
    matches = []
    for line in input_lines:
        for pattern in pattern_lines:
            s = difflib.SequenceMatcher(None, line, pattern)
            if s.ratio() > 0.95:  # Adjust the value for different levels of matching
                matches.append(line)
                break
    return matches


def main():
    # Read the input and pattern files
    input_lines = read_file("input.txt")
    pattern_lines = read_file("patterns.txt")

    print("Mode 1 output:")
    for line in mode_1(input_lines, pattern_lines):
        if line != "":
            print(line)

    print("\nMode 2 output:")
    for line in mode_2(input_lines, pattern_lines):
        if line != "":
            print(line)

    print("\nMode 3 output:")
    for line in mode_3(input_lines, pattern_lines):
        if line != "":
            print(line)


if __name__ == "__main__":
    main()
