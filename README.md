# Pattern Matching Script

This Python script is designed to match patterns in a given text document. It offers three modes of matching:

1. Mode 1: Output lines from input.txt that match exactly any pattern in patterns.txt.
2. Mode 2: Output lines from input.txt that contain a match with any pattern in patterns.txt somewhere in the line.
3. Mode 3: Output lines from input.txt that match with any pattern in patterns.txt with an edit distance <= 1.

## How to Run

1. Ensure that you have Python 3.x installed on your system.
2. Place the input text in a file named "input.txt" and place the patterns in a file named "patterns.txt". Make sure both files are in the same directory as the script.
3. Open a command prompt or terminal and navigate to the directory containing the script.
4. Run the script by executing the command: `python pattern_matching.py`
5. The output for each mode will be displayed in the console.

## Description

The script is divided into several functions:

- `read_file(file_path)`: Reads the contents of a file and returns a list of lines.
- `mode_1(input_lines, pattern_lines)`: Matches exact patterns from patterns.txt in input.txt and returns the matching lines.
- `mode_2(input_lines, pattern_lines)`: Matches patterns as substrings in input.txt and returns the lines containing the matches.
- `mode_3(input_lines, pattern_lines)`: Matches patterns with an edit distance <= 1 in input.txt and returns the matching lines.
- `main()`: The main function that reads the input files, calls the mode functions, and displays the results.

The implementation uses the difflib library for fuzzy matching with a sequence matcher and the re module for regular expression matching.

The script provides flexibility in choosing different matching modes based on your requirements. You can modify the input.txt and patterns.txt files to customize the input and pattern matching scenarios.

This implementation allows for easy extension or modification of the matching logic, making it adaptable to different use cases.

Please note that the matching algorithms and thresholds used in the script can be adjusted to suit specific needs by modifying the code.

Feel free to explore and modify the script to match your specific pattern matching requirements.

