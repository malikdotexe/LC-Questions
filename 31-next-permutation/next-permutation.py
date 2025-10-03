class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        a = len(nums)

        # Step 1: find pivot
        for i in range(a-1, 0, -1):
            if nums[i] > nums[i-1]:
                p = i-1

                # Step 2: find rightmost element > nums[p]
                for j in range(a-1, p, -1):
                    if nums[j] > nums[p]:
                        nums[p], nums[j] = nums[j], nums[p]
                        break

                # Step 3: reverse suffix
                nums[p+1:] = reversed(nums[p+1:])
                return

        # Step 4: if no pivot found we reverse whole array
        nums.reverse()