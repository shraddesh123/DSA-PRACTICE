class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arrs = []
        for arr in matrix:
            for i in arr:
                arrs.append(i)
                
        l = 0
        r = len(arrs) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if arrs[mid] == target:
                return True

            elif arrs[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False
