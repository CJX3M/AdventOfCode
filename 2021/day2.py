from openData import getData

data = getData("day2Input.txt")

# Part 1
forward = sum([int(m.split(' ')[1]) for m in data if "forward" in m])
up = sum([int(m.split(' ')[1]) for m in data if "up" in m])
down = sum([int(m.split(' ')[1]) for m in data if "down" in m])

# forward = sum([int(f.split(' ')[1]) for f in forward])
# up = sum([int(u.split(' ')[1]) for u in up])
# down = sum([int(d.split(' ')[1]) for d in down])

print("horizontal position:", forward)
print("Current depth:", down - up)
print("HPosition times depth:", forward * (down - up))

# Part 2
aim = 0
depth = 0
horPosition = 0

for m in data:
    if "forward" in m:
        horPosition += int(m.split(" ")[1])
        aim += depth*int(m.split(" ")[1])
    elif "up" in m:
        depth -= int(m.split(" ")[1])
    elif "down" in m:
        depth += int(m.split(" ")[1])

print("Current depth:", depth)
print("Current aim:", aim)
print("Horizontal position:", horPosition)
print("HPosition times depth:", horPosition * aim)
