from openData import getData
from copy import deepcopy

def genCombinatiosOfN(n, arr, results, i):

    if i == n:
        results.append(deepcopy(arr))
        return
    
    arr[i] = "+"
    genCombinatiosOfN(n, arr, results, i + 1)

    arr[i] = "*"
    genCombinatiosOfN(n, arr, results, i + 1)

if __name__ == "__main__":

    # input = getData("day7TestInput.txt")

    input = getData("day7Input.txt")

    equations =[[int(a), b.strip().split(' ')] for a, b in [e.split(":") for e in input]]

    accepted = []

    maxNumberOperators = max([len(i[1]) for i in equations])

    countEquations = len(equations)

    for index, eq in enumerate(equations):
        result = eq[0]

        operationResult = False

        operations = []

        gaps = len(eq[1]) - 1

        combinations = [None] * gaps
        genCombinatiosOfN(gaps, combinations, operations, 0)

        operationsIndex = 0

        print(f"\rEquation {index+1} of {countEquations}", end="")

        while not operationResult:
            numbers = [int(i) for i in eq[1]]

            total = numbers.pop(0)

            for i in range(len(operations[operationsIndex])):
                if operations[operationsIndex][i] == '+':
                    total += numbers.pop(0)
                elif operations[operationsIndex][i] == '*':
                    total *= numbers.pop(0)

            operationResult = total == result

            operationsIndex += 1

            if operationsIndex == len(operations):
                break


        if operationResult:
            eq.append(operations[operationsIndex - 1])
            accepted.append(eq)

    print("\n\rResult part 1: ", sum([eq[0] for eq in accepted]))

        

