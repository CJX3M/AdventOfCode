import numpy
from openData import getData

def getFuelConsumption(crabs, position):
    for crab in crabs:
        crab["fuel"] = abs(crab["position"] - position)
    return sum([crab["fuel"] for crab in crabs])

def getFuelConsumption2(crabs, position):
    for crab in crabs:
        crab["fuel"] = sum(range(abs(crab["position"] - position)+1))
    return sum([crab["fuel"] for crab in crabs])

numbers = [int(i) for i in getData("day7.txt")[0].split(',')]
#numbers = [16,1,2,0,4,2,7,1,2,14]

median = round(numpy.median([i for i in numbers]))

crabs = [{"position": int(i), "fuel": 0} for i in numbers]

print("Part 1: ", getFuelConsumption(crabs, median))
print("Part 2 Mean Ceil: ", getFuelConsumption2(crabs, round(numpy.mean([i for i in numbers]))))
print("Part 2 Mean Floor: ", getFuelConsumption2(crabs, int(numpy.mean([i for i in numbers]))))