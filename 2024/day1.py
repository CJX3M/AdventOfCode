from openData import getData

input = getData("day1Input.txt")

left = []
right = []

for pair in input:
    pair = pair.split("   ")
    left.append(int(pair[0]))
    right.append(int(pair[1]))

left.sort()
right.sort()

dif = 0

for i, item in enumerate(left):
    dif += abs(left[i] - right[i])

print("\n\rPart 1 Result: ", dif)

similarity = 0

for item in left:
    amount = right.count(item)
    similarity += item * amount

print("\n\rPart 2 Result:", similarity)

