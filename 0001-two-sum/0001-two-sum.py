class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        explored = dict()

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in explored:
                return [explored[diff], i]
            
            else:
                explored[nums[i]] = i