'''
Convert the binary search tree into bigger Tree
https://leetcode.com/contest/leetcode-weekly-contest-24/problems/convert-bst-to-greater-tree/
'''

class Tree:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right

def convert_tree(tree, right_sum=None):
    if right_sum is None:
        right_sum = [0]
    if tree is not None:
        convert_tree(tree.right, right_sum)
        right_sum[0] += tree.node
        tree.node = right_sum[0]
        convert_tree(tree.left, right_sum)

def inorder(tree, path=None):
    if path is None:
        path = []
    if tree is not None:
        inorder(tree.left, path)
        path.append(tree.node)
        inorder(tree.right, path)
    return path

def make_tree(index=0):
    if index == 1:
        return Tree(5, None, Tree(13))
    else:
        return Tree(5, Tree(2), Tree(13))

def main():
    tree = make_tree()
    print(inorder(tree))
    convert_tree(tree)
    print(inorder(tree))

if __name__ == '__main__':
    main()
