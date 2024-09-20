from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    for i, num in enumerate(len(nums)):
        if target - num in dict:
            return [dict[target - num], i]
        dict[num] = i

    return None
