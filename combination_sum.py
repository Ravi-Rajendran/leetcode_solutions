'''
Combinations Sum
https://leetcode.com/problems/combination-sum/description/
'''

class Solution(object):
	@staticmethod
	def combinationSum(candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		def find_potentials(candidates, target, start, potentials, solution):
			if target < 0:
				return
			if target == 0:
				solution.append(potentials)
				return solution
			for i in range(start, len(candidates)):
				find_potentials(candidates, target-candidates[i], i, potentials+[candidates[i]], solution)

		if candidates == [] or target <=0:
			return []
		potentials = []
		solution = []
		find_potentials(candidates, target, 0, potentials, solution)
		return solution

print(Solution.combinationSum([2, 3, 6, 7], 7))
