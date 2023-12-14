from bigtree import Node, list_to_tree

print(f"\n{'=' * 70}")
print(f"\t\t\tFINAL LAB EXAM \n\t\t     Jann Nicole San Jose \n\t\t\t    BCS22")
print(f"{'=' * 70}")


print(f"\n{'-' * 70}")
print("\t\t\t\tTREE")
print(f"{'-' * 70}")
path_dict = {
    "1": {"name": "1"},
    "1/2": {"name": "2"},
    "1/3": {"name": "3"},
    "1/2/4": {"name": "4"},
    "1/2/5": {"name": "5"},
    "1/3/6": {"name": "6"},
    "1/3/7": {"name": "7"},
    "1/6/8": {"name": "8"},
    "1/7/9": {"name": "9"}

    }
created_nodes = {"1": Node("1", data = path_dict["1"] )}

for path, node_data in path_dict.items():
    if path != "1":
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[node] = Node(node_data["name"], parent = current_node, data = path_dict[path])
            current_node = created_nodes[node]
created_nodes["1"].show(attr_list = ["name"])


class Node:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

def getVerticalOrder(root, hd, m):
    if root is None:
        return
    try:
        m[hd].append(root.node)
    except:
        m[hd] = [root.node]
    getVerticalOrder(root.left, hd - 1, m)
    getVerticalOrder(root.right, hd + 1, m)

def printVerticalOrder(root):
    m = dict()
    hd = 0
    getVerticalOrder(root, hd, m)

    result = [str(val) for node in sorted(m) for val in m[node]]
    original_output = " ".join(map(str, result))
    desired_output = " ".join(map(str, result[::-1]))

    print(f"\n{'-' * 70}")
    print("\t\t\tVERTICAL TRAVERSAL")
    print(f"{'-' * 70}")
    print("Vertical order traversal is:", original_output)
    print("Output:", desired_output)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    printVerticalOrder(root)
    print("")
