class Solution:
    def rob(self, nums: list[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def helperRob(start:int,end:int)->int:

            p2 = p1 = 0

            for i in range(start,end):

                curr = max(p2+nums[i],p1)
                p2 = p1
                p1 = curr

            return p1

        
        return max(helperRob(0,n-1),helperRob(1,n))

