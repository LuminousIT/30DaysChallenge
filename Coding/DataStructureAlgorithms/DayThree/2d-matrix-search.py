class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Question
        You are given an m x n integer matrix matrix with the following two properties:
        Each row is sorted in non-decreasing order.
        The first integer of each row is greater than the last integer of the previous row.
        Given an integer target, return true if target is in matrix or false otherwise.

        You must write a solution in O(log(m * n)) time complexity.

        EXample:
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true

        ==
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        Output: false

        ==
        solution

        use binary search on all the rows, initialize the toprow and bottomrow, get midpoint 
                check if the target > the last value of the currentrow, the new top = midpoint+1
                if the target < the first value of the currentrow, the new bottomrow = midpoint-1
                else (ie equal) break
        now the toprow and bottomrow should point to the row with the target value by doing => rowWithValue = toprow+bottomrow//2
        
        initialize the left=0 and right=len(matrix[0])-1
        (run binary seach)
        while l<=r
        get the mid = left+right //2
        ....

        
        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        Output: true
        """
        rows, cols = len(matrix), len(matrix[0])

        toprow = 0
        bottomrow = rows - 1
        # print(toprow,bottomrow)

        while toprow <= bottomrow:
            midRow = (toprow + bottomrow) // 2
        #     print("midrow", midRow)
            if target > matrix[midRow][-1]:
                toprow = midRow + 1
            elif target < matrix[midRow][0]:
                bottomrow = midRow - 1
            else:
                break
        # print(toprow, bottomrow)
        

        # Edge case, after first binary search, if toprow (left) is not <= bottomrow (right), return False immediately. 
        # because left should always be <= right for binary search 
        # This edge case can exist it is the base condition the while loop depends on. and at some point, it'll be true for the while loop to finish.
        # and since we still have to do another binary search, we must first check the validity before we proceed.
        # as in the case of matrix = [[1]] and target = 2
        if not (toprow <= bottomrow):
            return False
        
        # Note: brackets are important.
        rowWithValue = (toprow + bottomrow) // 2 

        left = 0
        right = cols - 1 # len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if target > matrix[rowWithValue][mid]:
                left = mid + 1
            elif target < matrix[rowWithValue][mid]:
                right = mid - 1
            else:
                return True
            
        return False
    

# result = Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)

result = Solution().searchMatrix([[1]], 2)
print(result)