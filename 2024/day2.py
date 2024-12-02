from openData import getData

input = getData("day2Input.txt")

def checkReport(data):
    decreasing = False
    increasing = False
    for index in range(len(data) - 1):
        diff = data[index] - data[index+1]
        if diff > 0:
            increasing = diff > 0
        if diff < 0:
            decreasing = diff < 0  
        if increasing and decreasing or not (0 < abs(diff) < 4):
            return False
    return True

safeReport = 0
for line in input:
    report = [int(i) for i in line.strip().split()]
    if checkReport(report):
        safeReport += 1

print("\nPart 1 Result: ", safeReport)

safeReport = 0
for line in input:
    report = [int(i) for i in line.strip().split()]
    check = checkReport(report)
    if not check:        
        for i in range(len(report)):
            temp = report.pop(i)
            check = checkReport(report)
            if check:
                break
            report.insert(i, temp)
    if check:
        safeReport += 1

print("\nPart 2 Result: ", safeReport)
