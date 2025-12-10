#!/bin/bash

# Check if the argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

# Get the day number from the argument
day_number=$1

# Validate that the argument is a number
if ! [[ "$day_number" =~ ^[0-9]+$ ]]; then
    echo "Error: <day_number> must be an integer."
    exit 1
fi

# Define file names
py_file="day${day_number}.py"
input_file="day${day_number}Input.txt"
test_input_file="day${day_number}InputTest.txt"

# Create and initialize the Python file
cat <<EOL > "$py_file"
import openData

useTest = False
input = openData.getData(${day_number}, useTest)

Part1 = ''
print("Part 1:", Part1)
Part2 = ''
print("Part 2:", Part2)
EOL

# Create empty input files
touch "$input_file"
touch "$test_input_file"

# Print success message
echo "Files created: $py_file, $input_file, $test_input_file"