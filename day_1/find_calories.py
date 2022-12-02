with open('input.txt', 'r') as f:
    calories = 0
    elves = []
    for line in f.readlines():
        if line.strip('\n').isnumeric():
            calories += int(line.strip('\n'))
        else:
            elves.append(calories)
            calories = 0

elves = sorted(elves, reverse=True)
max_cal = elves[0]
print('Highest calories: ', max_cal)
tot_cal = sum(elves[0:3])
print('Sum of Highest 3 calories: ', tot_cal)