from collections import Counter
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_dict = Counter(nums)
        for el in nums:
            if count_dict[el] >n/2:
                return el