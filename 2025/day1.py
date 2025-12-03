import openData

numbers = list(range(0, 100))
current_index = 50

times_dial_at_0 = 0
times_clicked_at_0 = 0

input = openData.getData(1, False)

for line in input:
    
    direction = line[0]
    number = int(line[1:])

    for i in range(number):
        if direction == 'L':
            current_index -= 1
        elif direction == 'R':
            current_index += 1
        
        current_index = current_index % len(numbers)

        if numbers[current_index] == 0:
            times_clicked_at_0 += 1

    print("Dial moved", direction, number, "to", numbers[current_index % len(numbers)])

    if numbers[current_index] == 0:
        times_dial_at_0 += 1

print("Part 1")
print("The dial was at 0 a total of", times_dial_at_0, "times.")

print("Part 2")
print("The dial clicked past 0 a total of", times_clicked_at_0, "times.")


