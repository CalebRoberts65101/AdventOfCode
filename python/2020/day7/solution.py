
with open('python\\2020\day7\data.txt') as f:
    lines = f.readlines()

class graphNode():
    def __init__(self):
        self.color = ''
        self.children = dict()
        self.children_count = dict()
        self.parents = dict() 

    def __str__(self):
        return self.color

# for each line, build directed graph
graph = dict()
for line in lines:
    # light red bags contain 1 bright white bag, 2 muted yellow bags.
    parts = line.split(' contain ')
    bag_color = parts[0].replace('bags','').strip()
    # temp create node
    node = ''
    if bag_color in graph:
        node = graph[bag_color]
    else:
        node = graphNode()
        node.color = bag_color
        graph[bag_color] = node
    
    children = parts[1].split(',')
    for kid in children:
        if kid.strip() == 'no other bags.':
            break
        parts = kid.strip().split(' ')
        count = parts[0]
        color = parts[1] + ' ' + parts[2]
        node.children_count[color] = int(count)
        # if kid doesn't exist create it
        if color not in graph:
            kid_node = graphNode()
            kid_node.color = color
            graph[color] = kid_node

        # make link from kid to current
        graph[color].parents[bag_color] = node

        # make link from parent to kid
        node.children[color] = graph[color]


# given graph, start at "shiny gold" and find all colors reachable
found_bags = dict()

def findAllParents(found_bags, current_bag, graph):
    current_node = graph[current_bag]
    for key in current_node.parents.keys():
        if key not in found_bags:
            found_bags[key] = 1
            findAllParents(found_bags, key, graph)

    return found_bags

# commented out solution to part 1
# findAllParents(found_bags, 'shiny gold', graph)

# for key in found_bags.keys():
#     print(key)

# print('number of found bags: ', len(found_bags.keys()))

def findChildrenCount(bag_color):
    count = 0
    node = graph[bag_color]
    if len(node.children) == 0:
        return 0
    else:
        for color in node.children.keys():
            print(color)
            count += node.children_count[color]
            count += findChildrenCount(color) * node.children_count[color]
            print(color, count)
    return count

print(findChildrenCount('shiny gold'))
