from collections import Counter

class Solution:
    def permuteUnique(self, nums):
        result = []
        temp = []

        # count tells us how many times each number is available to pick
        count = Counter(nums)

        def backtrack():
            # if we have used up all the numbers, we formed one complete permutation
            if len(temp) == len(nums):
                result.append(temp.copy())
                return

            # try to pick any number that is still left
            for num in count:
                # if this number is still available to use
                if count[num] > 0:
                    # choose it
                    temp.append(num)
                    count[num] -= 1

                    # go ahead and try to build the rest
                    backtrack()

                    # undo the choose step
                    temp.pop()
                    count[num] += 1

        backtrack()
        return result
