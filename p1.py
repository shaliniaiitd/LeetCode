# class Solution:
#     def merge(self, nums1, m: int, nums2, n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:m + n] = nums2
#         nums1.sort()
#
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# Solution().merge(nums1, 3, nums2, 3)
# print(nums1)
#
#
# def removeDuplicates(nums) -> int:
#     setnum = set(nums)
#     print(setnum)
#     return len(setnum)
#
# num = [1,1,2]
# print(removeDuplicates(num))
#
# def majorityElement(nums):
#     n = len(nums)
#     for num in nums:
#         if nums.count(num) > n // 2:
#             return num
#         else:
#             continue
# print(majorityElement([]))
#
#
# def maxProfit(prices) -> int:
#     profit= {}
#     # Initialize the first day's profit as 0profit= {}'
#     for day in range(len(prices)):
#         profit[day] = 0
#         for i in range(day + 1, len(prices)):
#             if prices[i] - prices[day] > profit[day]:
#                 profit[day] = prices[i] - prices[day]
#
#     max_p = 0
#     for day,p in profit.items():
#         if p >max_p:
#             max_p = p
#     return (max_p)
#
# print(maxProfit([7,1,5,3,6,4]))

list1 = ['a', 'b', 'c']
list2 = [1,2,3]

result = {key:value for key,value in zip(list1,list2)}

print(result)