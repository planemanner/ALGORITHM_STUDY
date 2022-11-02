"""
Given n non-negative integers representing

an elevation map where the width of each bar is 1,

compute how much water it can trap after raining.

"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 양 끝은 흐른다고 생각하면 됨.
        pass


# Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output : 6