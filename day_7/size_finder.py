import time

def commands(mode, node=None, size=0, name='', file=''):
    if mode == "cd":
        if name == '/':
            return Node(name)
        elif name == '..':
            return node.get_parent()
        return node.get_child(name)
    elif mode == "dir":
        child = Node(name, node)
        node.add_child(child)
    elif mode != "ls":
        node.add_to_size(size, file)
    return node

class Node():

    def __init__(self, name, parent=None):
        self.size = 0
        self.name = name
        self.parent = parent
        self.child = {}
        self.files = {}

    def add_to_size(self, num, file=None):
        self.size += num
        if file:
            self.files[file] = num

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_child(self, name):
        return self.child[name]

    def add_child(self, node):
        self.child[node.get_name()] = node

    def add_child_size(self):
        if self.child:
            for child in self.child.values():
                self.add_to_size(child.get_size())

    def update(self):
        for child in self.child.values():
            child.update()
        self.add_child_size()

    def print_num_child(self):
        print(len(self.child))

    def count(self):
        total = self.get_size() if self.get_size() < 100000 else 0
        for child in self.child.values():
            total += child.count()
        return total
    
    def print_tree(self, level=0):
        dash = ''
        next_level = level + 1
        dash = '+' + dash.join([dash.join(['\t']) for i in range(level)])
        star = '*' if self.get_size() < 100000 else ''
        print('{} {} (dir, size={} {})\n'.format(dash, self.get_name(), str(self.get_size()), star))
        for child in self.child.values():
            child.print_tree(level=next_level)
        for file in self.files:
            print('{} {} (file, size={})\n'.format(dash, file, str(self.files[file])))

    def find_small_dir(self, size):
        dirs = [self.get_size()]
        for child in self.child.values():
            if child.get_size() + size >= 30000000:
                dirs.append(child.find_small_dir(size))
        return min(dirs)

def main():

    curr_node = None
    with open('input.txt', 'r') as f:
        for line in f.readlines():

            cmd = line.strip('\n')
            if cmd[0:4] == "$ cd":
                curr_node = commands(mode="cd", node=curr_node, name=cmd.split(' ')[-1])
            elif cmd[0:4] == "$ ls":
                continue
            elif cmd[0:3] == "dir":
                curr_node = commands(mode="dir", node=curr_node, name=cmd.split(' ')[-1])
            else:
                curr_node = commands(mode="file", node=curr_node, name=cmd.split(' ')[-1], size=int(cmd.split(' ')[0]))

    while(curr_node.get_parent()):
        curr_node = curr_node.get_parent()

    curr_node.update()
    num_nodes = curr_node.count()
    print('Part 1: ', num_nodes)

    used_space = curr_node.get_size()
    unused_space = 70000000 - used_space
    min_size = curr_node.find_small_dir(unused_space)
    print('Part 2: ', min_size)

    #curr_node.print_tree()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))