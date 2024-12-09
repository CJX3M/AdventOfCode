from openData import getData
from copy import deepcopy

def genCombinatiosOfN(n, arr, results, i, part2 = False):

    if i == n:
        results.append(deepcopy(arr))
        return
    
    arr[i] = "+"
    genCombinatiosOfN(n, arr, results, i + 1, part2)

    arr[i] = "*"
    genCombinatiosOfN(n, arr, results, i + 1, part2)

    if not part2:
        return
    
    arr[i] = "||"
    genCombinatiosOfN(n, arr, results, i + 1, part2)

def performCalc(eq, operations, part2 = False):
    result = eq[0]

    operationsIndex = 0
    while True:
        numbers = [int(i) for i in eq[1]]

        total = numbers.pop(0)

        for i in range(len(operations[operationsIndex])):
            if operations[operationsIndex][i] == '+':
                total += numbers.pop(0)
            elif operations[operationsIndex][i] == '*':
                total *= numbers.pop(0)
            elif operations[operationsIndex][i] == "||" and part2:
                nextNumber = numbers.pop(0)
                newNumber = str(total) + str(nextNumber)
                total = int(newNumber)

        if total == result:
            return True

        operationsIndex += 1

        if operationsIndex == len(operations):
            return False
        
def execute(equations, part2 = False):
    accepted = []

    notAccepted = []

    countEquations = len(equations)

    for index, eq in enumerate(equations):
        operations = []

        gaps = len(eq[1]) - 1

        combinations = [None] * gaps
        genCombinatiosOfN(gaps, combinations, operations, 0, part2)

        print(f"\rEquation {index+1} of {countEquations}", end="")

        if performCalc(eq, operations, part2):
            accepted.append(eq[0])
        else:
            notAccepted.append(eq)

    return (accepted, notAccepted)

if __name__ == "__main__":

    #input = getData("day7TestInput.txt")

    input = getData("day7Input.txt")

    equations =[[int(a), b.strip().split(' ')] for a, b in [e.split(":") for e in input]]

    (accepted, notAccepted) = execute(equations)

    print("\n\rResult part 1: ", sum(accepted))

    countEquations = len(notAccepted)

    (acceptedPart2, rejected) = execute(notAccepted, True)

    print("\n\rResult part 2: ", sum(accepted) + sum(acceptedPart2))
        

