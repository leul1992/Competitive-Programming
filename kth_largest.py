class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = map(int, nums)
        nums = sorted(nums, reverse=True)
        return str(nums[k-1])