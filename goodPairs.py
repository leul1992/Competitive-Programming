class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counting = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j and nums[i] == nums[j]:
                    counting += 1
        return counting