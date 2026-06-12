class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums

        if len(nums) <= 1:
            return self.nums

        middle = len(self.nums) // 2
        leftArr = self.sortArray(nums[:middle])
        rightArr = self.sortArray(nums[middle:])

        return self.mergeArray(leftArr,rightArr)

    def mergeArray(self,arr1,arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        res = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        res.extend(arr1[i:])
        res.extend(arr2[j:])

        return res
