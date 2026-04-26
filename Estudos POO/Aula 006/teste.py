class Solution(object):
    def pa(self, arr):
        self.arr = arr
        self.arr.sort()
        if (self.arr[0] - self.arr[1]) == (self.arr[1] - self.arr[2]):
            return True
        else:
            return False
a1 = Solution()