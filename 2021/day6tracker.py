def countFishes(fishes, days):
    count = [fishes.count(i) for i in range(9)]
    for day in range(days):
        count[(day + 7) % 9] += count[day % 9]
    return sum(count)

fishes = [int(i) for i in "".split(",")]
print("In 80 days:", countFishes(fishes, 80))
print("In 80 days:", countFishes(fishes, 256))
