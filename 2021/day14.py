from openData import getData
from collections import Counter, defaultdict

def applyStepsBF(polymer, steps):
    for step in range(steps):
        newPolymer = ""
        index = 0
        while True:
            subStr = polymer[index:index+2]
            template = [t for t in templates if t["pair"] == subStr][0]
            newPolymer += template["insertion"][0]
            index += 1
            if index >= len(polymer)-1:
                break
        polymer = newPolymer + polymer[-1]
        print("Step", step, end="\r")
    return polymer

def applySteps(polymers, steps):
    for step in range(steps):
        stepPolymers = polymers.copy()
        for pol in [p for p in stepPolymers.items() if p[1] > 0]:
            template = [t for t in templates if t["pair"] == pol[0]][0]
            polymers[template["insertion"][0]] += pol[1]
            polymers[template["insertion"][1]] += pol[1]
            polymers[pol[0]] -= pol[1]
    singles = defaultdict(list)

    for pol in polymers.items():
        key, value = pol
        if not key[0] in singles:
            singles[key[0]] = 0
        singles[key[0]] += value
        if not key[1] in singles:
            singles[key[1]] = 0
        singles[key[1]] += value
        if key[0] == key[1]:
            singles[key[0]] += 1
    singles[polymer[0]] += 1
    singles[polymer[-1]] += 1

    mostCommon = max(singles.values())
    leastCommon = min(singles.values())
    print((mostCommon - leastCommon)//2)
    return polymers

data = getData("day14.txt")

polymer = data[0]

templates = [{"pair": p[0].strip(), "insertion": [p[0][0] + p[1].strip(), p[1].strip() + p[0][1]]} for p in [i.split('->') for i in data if '->' in i]]
polymers = defaultdict(list)
for template in templates:
    polymers[template["pair"]] = 0

for index in range(len(polymer)-1):
    polymers[polymer[index:index+2]] += 1

# Part 1
polymers = applySteps(polymers, 10)
# Part 2
applySteps(polymers, 30)

