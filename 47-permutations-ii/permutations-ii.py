class Solution:
    def permuteUnique(self, nums):
        result = []
        temp = []
        used = [False] * len(nums)

        def backtrack():
            if len(temp) == len(nums) and temp not in result:
                result.append(temp.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                temp.append(nums[i])

                backtrack()

                used[i] = False
                temp.pop()

        backtrack()
        return result
