'''
Construct a string from binary tree
https://leetcode.com/problems/construct-string-from-binary-tree/description/
'''


class Tree:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right


def make_tree(index=0):
    if index == 1:
        '''
              1
             /  \
            2    3
           /
          4
        '''
        t = Tree(1, Tree(2, Tree(4)), Tree(3))
        return t

    elif index == 2:
        '''
              1
             /  \
            2    3
           /       \
          4         5
        '''
        t = Tree(1, Tree(2, Tree(4)), Tree(3, None, Tree(5)))
        return t

    elif index == 3:
        '''
              1
             /  \
            2    3
               /   \
              4     5
        '''
        t = Tree(1, Tree(2), Tree(3, Tree(4), Tree(5)))
        return t

    elif index == 4:
        '''
              1
             /
            2
           /
          4
        '''
        t = Tree(1, Tree(2, Tree(4)))
        return t

    elif index == 5:
        '''
              1
                \
                 3
                   \
                    5
        '''
        t = Tree(1, None, Tree(3, None, Tree(5)))
        return t


    else:
        '''
              1
             /  \
            2    3
             \
              4
        '''
        t = Tree(1, Tree(2, None, Tree(4)), Tree(3))
        return t


def serialize(tree):
    if tree is None:
        return ''

    if tree.left is not None or tree.right is not None:
        l = '(' + str(serialize(tree.left)) + ')'
    else:
        l = ''

    if tree.right is not None:
        r = '(' + str(serialize(tree.right)) + ')'
    else:
        r = ''

    return str(tree.node) + l + r


for index in range(6):
    tree = make_tree(index)
    print(index, serialize(tree))
