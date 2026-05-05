"""
Docstring for Backtracking.t
"""

def comb_sum(array, target):

    """
    Searches all possible combination sums for some sequence which matches the target

    Example:
    array = [2, 3, 7], target = 7
    result = [[2, 2, 3], [7]]

    """

    result = []

    def helper(index, subarray, s = 0):
        if s == target:
            result.append(subarray)
            return

        if index > len(array) or s > target:
            return

        helper(index, subarray + [array[index]], s + array[index])
        helper(index + 1, subarray, s)

    helper(0, [], 0)
    return result
