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
        ints = re.findall("-?\\d+", match)
        if len(ints) == 2:
            part1result += int(ints[0]) * int(ints[1])
            if do:
                part2result += int(ints[0]) * int(ints[1])
        

print("\n\rResult: ", part1result)
print("\n\rResult: ", part2result)