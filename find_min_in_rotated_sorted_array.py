import doctest


def find_min(nums, low=None, high=None):
	"""
	Testing finding minimum in rotated array
	>>> nums = [4, 5, 6, 7, 0, 1, 2]
	>>> print(find_min(nums))
	0
	"""
	if low is None and high is None:
		low, high = 0, len(nums)-1

	if low > high:
		return 0
	if low == high:
		return arr[low]

	mid = (low + high) // 2

	if mid > low and nums[mid-1] > nums[mid]:
		return nums[mid]
	if mid < high and nums[mid+1] < nums[mid]:
		return nums[mid+1]

	if nums[mid] > nums[high]:
		return find_min(nums, mid+1, high)
	return find_min(nums, low, mid-1)


# run python -m doctest -v find_min_in_rotated_sorted_array.py 
# or
# run from main function
if __name__ == '__main__':
	doctest.testmod(verbose=True)

