class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        def can_split(max_sum):
            count = 1
            current = 0
            for x in nums:
                if current + x <= max_sum:
                    current += x
                else:
                    count += 1
                    current = x
                    if count > k:
                        return False
            return True

        while low < high:
            mid = (low + high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid + 1

        return low