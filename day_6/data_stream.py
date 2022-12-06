import time

def find_marker(data_stream='', distint_char=0):
    packet_market = []
    for i, data in enumerate(data_stream):
        if data not in packet_market and len(packet_market) < distint_char - 1:
            packet_market.append(data)
        elif data not in packet_market and len(packet_market) == distint_char - 1:
            if len(set(data_stream[i-distint_char:i])) == distint_char:
                return i
    return 0

def main():
    data_stream = ''
    with open('input.txt', 'r') as f:
        data_stream = f.readlines()[0].strip('\n')

    char_pos_4 = find_marker(data_stream, 4)
    char_pos_14 = find_marker(data_stream, 14)
    if char_pos_4 == 0:
        print('Nothing found')
    else:
        print('Part 1 marker ', char_pos_4)
    if char_pos_14 == 0:
        print('Nothing found')
    else:
        print('Part 2 marker ', char_pos_14)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))