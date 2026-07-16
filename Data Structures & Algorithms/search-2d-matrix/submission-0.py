class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on rows then within row
        # time O(log m + log n) = O(logmn) space O(1)
        top = 0
        bot = len(matrix) - 1
        targetRow = -1

        # binary search to find row 
        while top <= bot:
            m = top + ((bot-top)//2)
            # target smaller than first num in row
            if matrix[m][0] > target:
                bot = m-1
            # target larger than last num in row
            elif matrix[m][-1] < target:
                top = m+1
            else: 
                targetRow = m
                break

        # binary search in row
        start = 0
        end = len(matrix[targetRow])-1
        while start <= end:
            mid = start + ((end-start)//2)
            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] > target:
                end = mid-1
            else:
                start = mid+1
        return False