import openData

input = openData.getData(5, False)

ingredients = []
ranges = []
freshIngredient = 0
uniqueFreshIds = 0

for line in input:
    if line == "":
        continue
    if '-' in line:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

        uniqueFreshIds += end - start + 1
    else:
        ingredients.append(int(line))

ranges.sort()
mergedRanges = []

for start, end in ranges:
    if not mergedRanges or mergedRanges[-1][1] < start - 1:
        mergedRanges.append((start, end))
    else:
        mergedRanges[-1] = (mergedRanges[-1][0], max(mergedRanges[-1][1], end))

uniqueFreshIds = sum(end - start + 1 for start, end in mergedRanges)

for ingredient in ingredients:
    fresh = False
    for start, end in ranges:
        if start <= ingredient <= end:
            fresh = True
            break
    if fresh:
        freshIngredient += 1

print('Part 1: ', freshIngredient)
print('Part 2: ', uniqueFreshIds)