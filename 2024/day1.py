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

dif = []

for i, item in enumerate(left):
    dif.append(abs(left[i] - right[i]))

distance = sum(dif)

print("\n\rPart 1 Result: ", distance)

sims = []

for item in left:
    amount = right.count(item)
    sims.append(item * amount)

similarity = sum(sims)

print("\n\rPart 2 Result:", similarity)

