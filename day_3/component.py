import string

def main():
    num = 1
    char_map = {}
    for char in string.ascii_lowercase:
        char_map[char] = num
        num += 1
    for char in string.ascii_uppercase:
        char_map[char] = num
        num += 1

    total = 0
    input_txt = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            input_txt.append(line.strip('\n'))

    for word in input_txt:
        word_part_1 = word[0:int(len(word)/2)]
        word_part_1 = set(word_part_1)
        word_part_2 = word[int(len(word)/2):int(len(word))]
        word_part_2 = set(word_part_2)
        matching_char = list(word_part_1 & word_part_2)
        total += char_map[matching_char[0]]

    print('Total sum of part 1: ', total)

    total = 0
    for i in range(0, int(len(input_txt)), 3):
        group = input_txt[i:i+3]
        word_1 = set(group[0])
        word_2 = set(group[1])
        word_3 = set(group[2])
        matching_char = list(word_1 & word_2 & word_3)
        total += char_map[matching_char[0]]
    print('Total sum of part 2: ', total)
if __name__ == "__main__":
    main()