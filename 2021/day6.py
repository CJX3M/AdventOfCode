states = [int(i) for i in "".split(",")]
#states = [int(i) for i in "".split(',')]
currentDay = 0

while currentDay < 256:
    currentLen = range(len(states))
    for i in currentLen:
        if states[i] == 0:
            states[i] = 6
            states.append(8)
        else:
            states[i] -= 1
    currentDay += 1
    
print(len(states))
