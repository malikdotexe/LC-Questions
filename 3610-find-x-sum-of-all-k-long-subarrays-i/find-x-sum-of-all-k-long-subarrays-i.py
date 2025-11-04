import heapq
from collections import Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k > n:
            return []

        window = Counter(nums[:k])
        heap = [(-freq, -num) for num, freq in window.items()]
        heapq.heapify(heap)

        def get_x_sum():
            seen = set()
            total = 0
            temp = []
            while heap and len(seen) < x:
                freq, num = heapq.heappop(heap)
                freq, num = -freq, -num
                # only use if it's still valid in current window
                if window.get(num, 0) == freq and num not in seen:
                    total += freq * num
                    seen.add(num)
                temp.append((-freq, -num))
            for item in temp:
                heapq.heappush(heap, item)
            return total

        result = [get_x_sum()]

        for i in range(k, n):
            out_val, in_val = nums[i - k], nums[i]

            # update outgoing
            window[out_val] -= 1
            if window[out_val] == 0:
                del window[out_val]

            # update incoming
            window[in_val] += 1

            # push updated frequencies for affected numbers
            heapq.heappush(heap, (-window[in_val], -in_val))
            if out_val in window:
                heapq.heappush(heap, (-window[out_val], -out_val))

            result.append(get_x_sum())

        return result
