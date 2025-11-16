#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            print(f"i = {i}, j = {j}, abs(i-j) = {abs(i - j)}")
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    else:
        return False