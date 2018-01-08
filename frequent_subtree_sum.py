'''
Most Frequent Subtree sum
https://leetcode.com/problems/most-frequent-subtree-sum/description/
'''

class Tree:
	def __init__(self, data, left=None, right=None):
		self.node = data
		self.left = left
		self.right = right

def make_tree(index=0):
	if index == 1:
		t = Tree(5, Tree(2), Tree(-3))
		return t
	if index == 2:
		t1 = Tree(2, Tree(1), Tree(3, Tree(4), Tree(5)))
		t = Tree(5, t1, Tree(-5))
		return t
	else:
		return Tree(5, Tree(2), Tree(-5))

def find_subtree_sum(tree, d):
	if tree is None:
		return 0
	temp = tree.node + find_subtree_sum(tree.left, d) + find_subtree_sum(tree.right, d)
	d[temp] = d.get(temp, 0) +1
	return temp

tree = make_tree(1)
d = {}
find_subtree_sum(tree, d)
print(d)
i = max(d.values())
print([x for x in d if d[x] == i])
