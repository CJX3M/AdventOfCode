import re
from openData import getData

input = getData("day3Input.txt")
matches = re.findall("don't|do|mul\(\d+.\d+\)", "".join(input))

part1result = 0
part2result = 0

do = True

for match in matches:
    if match == "do":
        do = True
    if match == "don't":
        do = False
    if "mul" in match:
        x, y = map(int, match[4:-1].split(","))
        part1result += x * y
        if do:
            part2result += x * y
        

print("\n\rResult: ", part1result)
print("\n\rResult: ", part2result)