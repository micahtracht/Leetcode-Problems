class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        binary search the rows then binary search the columns
        '''

        # Step 1: find the right row
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r)//2
            #print(l, r, m, matrix[m][0])
            if matrix[m][0] == target:
                return True
            if matrix[m][0] < target and matrix[m][len(matrix[0]) - 1] >= target:
                break
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        
        toSearch = matrix[m]
        print(toSearch)
        l, r = 0, len(toSearch) - 1
        while l <= r:
            m = (l + r)//2
            if toSearch[m] == target:
                return True
            if toSearch[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False