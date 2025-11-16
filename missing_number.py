#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(self, nums: List[int]) -> int:
    for i in range(0, len(nums) + 1):
        if not i in nums:
            return i