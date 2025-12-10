import openData
import numpy as np
import math

def parse_input(use_test=False):
    raw = openData.getData(6, use_test)
    return [list(filter(None, line.split(" "))) for line in raw]

def part1(input_data):
    arr = np.array(input_data)
    arr = arr.T  # Transpose the matrix
    results = []
    for row in arr:
        *vals, op = row
        vals = list(map(int, vals))
        if op == "+":
            results.append(sum(vals))
        elif op == "*":
            results.append(math.prod(vals))
    return sum(results)

def part2(input_data):    
    # Transpose input to get columns
    columns = list(map(list, zip(*input_data)))
    results = []
    numbers = []
    operator = None

    for col_index, col in enumerate(columns):
        digits = [c for c in col if c != " "]
        if not digits or col_index == len(columns) - 1:
            if digits:
                numbers.append(int(''.join(digits)))
            if operator and numbers:
                if operator == "+":
                    results.append(sum(numbers))
                elif operator == "*":
                    results.append(math.prod(numbers))
            numbers = []
            operator = None
            continue
        if digits[-1] in ["+", "*"]:
            operator = digits[-1]
            digits = digits[:-1]
        if digits:
            numbers.append(int(''.join(digits)))
    return sum(results)

def main():
    use_test = False
    input_data = parse_input(use_test)
    print("Part 1:", part1(input_data))
    # For part 2, you may need to adjust parsing based on your actual input structure
    raw_input = openData.getData(6, use_test)
    print("Part 2:", part2(raw_input))

if __name__ == "__main__":
    main()