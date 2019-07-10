

class Solution(object):
	"""
	"""
	def duplicateZeros(self, arg):
		arr_copy = arr[:]
		index, n = 0, len(arr_copy)
		for elem in arr_copy:
			arr[index] = elem
			index += 1
			if index >= n:
				break
			if elem == 0:
				arr[index] = elem
				index += 1
				if index >= n:
					break