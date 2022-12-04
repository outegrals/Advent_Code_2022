import time
def main():

    part1_total = 0
    part2_total = 0
    elf_pair = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            elves = line.strip('\n').split(',')
            tmp1 = [int(x) for x in elves[0].split('-')]
            tmp2 = [int(x) for x in elves[1].split('-')]
            elv1 = set([x for x in range(tmp1[0], tmp1[1] + 1)])
            elv2 = set([x for x in range(tmp2[0], tmp2[1] + 1)])
            elf_pair.append((elv1, elv2))

    for e1, e2 in elf_pair:

        if len(e1 & e2) >= 1:
            part2_total += 1
            if (e1 - e2) == set() or (e2 - e1) == set():
                part1_total += 1
    print('Total for part 1', part1_total)
    print('Total for part 2', part2_total)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))