from openData import getData

data = getData("day3.txt")

def getPowerConsumption(data):
    dataLen = len(data[0])
    lines = len(data)
    currentIndex = 0
    gamma = ''
    epsilon = ''

    while currentIndex < dataLen:
        ones = 0
        for line in data:
            if line[currentIndex] == "1":            
                ones += 1
        if ones > lines/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        currentIndex += 1

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print("Power consumption", gamma * epsilon)

def getLifeSupportRating(data):
    oxygenGenRating = ""
    co2ScrubberRat = ""

    dataLen = len(data[0])
    currentIndex = 0
    chunk = data

    while currentIndex < dataLen:
        lines = len(chunk)
        ones = 0
        for line in chunk:
            if line[currentIndex] == "1":            
                ones += 1
        chunk = [f for f in chunk if f[currentIndex] == ("1" if ones >= lines/2 else "0")]
        currentIndex += 1
        if len(chunk) == 1:
            break

    oxygenGenRating = int(chunk[0], 2)

    dataLen = len(data[0])
    currentIndex = 0
    chunk = data

    while currentIndex < dataLen:
        lines = len(chunk)
        ones = 0
        for line in chunk:
            if line[currentIndex] == "1":            
                ones += 1
        chunk = [f for f in chunk if f[currentIndex] == ("1" if ones < lines/2 else "0")]
        currentIndex += 1
        if len(chunk) == 1:
            break

    co2ScrubberRat = int(chunk[0], 2)

    print("Oxygen Gen Rating", oxygenGenRating)
    print("co2 Scrubber Rating", co2ScrubberRat)
    print("Life Support rating", oxygenGenRating * co2ScrubberRat)

getPowerConsumption(data)
getLifeSupportRating(data)