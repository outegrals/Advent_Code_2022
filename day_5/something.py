import time

def main():

    part1_message = ''
    box_queue = {}
    for i in range(1,10):
        box_queue[i] = []
    instruct_list = []
    MAP_SEPERATOR = " 1   2   3   4   5   6   7   8   9 "
    box_indexes = {}
    num = 1
    for s in MAP_SEPERATOR:
        if s.isdigit():
            box_indexes[MAP_SEPERATOR.index(s)] = num
            num += 1

    with open('input.txt', 'r') as f:
        for i in range(0,8):
            l = next(f).strip('\n')
            num = 0
            for s in l:
                if s.isalpha():
                    box_queue[box_indexes[l.index(s, num)]].append(s)
                num += 1
        #discard the following 2 lines
        next(f)
        next(f)
        while(True):
            try:
                l = next(f).strip('\n')
                instruct = [int(s) for s in l.split() if s.isdigit()]
                instruct_list.append(tuple(instruct))
            except:
                break

    for move, box_start, box_end in instruct_list:
        #if part 2
        box_queue[box_end][0:0] = box_queue[box_start][0:move]
        #if part 1
        #box_queue[box_end][0:0] = box_queue[box_start][0:move][::-1]
        del box_queue[box_start][0:move]

    for i in range(1, 10):
        part1_message += box_queue[i][0]

    print(part1_message)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))