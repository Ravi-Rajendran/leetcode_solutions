'''
Combinations Sum 2
https://leetcode.com/problems/combination-sum-ii/description/
'''

def find_candidates(candidates, target, index, path, solution, negligibles):
	if target < 0:
		return
	if target == 0:
		res = sorted(path)
		if res[0] not in negligibles:
			solution.append(path)
			negligibles[res[0]] = [res[1:]]
		else:
			flag = False
			for vals in negligibles[res[0]]:
				if vals == res[1:]:
					flag = True
					break
			if not flag:
				solution.append(path)
				negligibles[res[0]].append(res[1:])

		return solution

	for i in range(index, len(candidates)):
		find_candidates(candidates, target-candidates[i], i+1, path+[candidates[i]], solution, negligibles)


def combination_sum(candidates, target):
	if candidates == [] or target <= 0:
		return []

	solution = []
	find_candidates(candidates, target, 0, [], solution, {})

	print(solution)

combination_sum([10, 1, 2, 7, 6, 1, 5], 8)
