import openData

input = openData.getData(2, False)[0].split(',')

invalids = []

for idRange in input:
    ids = list(range(int(idRange.split('-')[0]), int(idRange.split('-')[1]) + 1))

    for id in ids:
        idStr = str(id)

        if idStr[0] == '0':
            invalids.append(id)
            continue

        halfIndex = len(idStr) // 2

        firstHalf = idStr[:halfIndex]
        secondHalf = idStr[halfIndex:]

        if firstHalf == secondHalf:
            invalids.append(id)

        for patternLength in range(1, halfIndex + 1):
            pattern = idStr[:patternLength]
            repeatedPattern = pattern * (len(idStr) // patternLength)

            if repeatedPattern == idStr and invalids.count(id) == 0:
                invalids.append(id)
                break

print("The total of invalids is ", sum(invalids))