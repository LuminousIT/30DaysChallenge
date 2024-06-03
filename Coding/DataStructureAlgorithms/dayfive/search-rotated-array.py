class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        mid=l+r //2
        
        """
        # try:
        #      res =  nums.index(target)
        # except ValueError:
        #      return -1
        
        print("let's go")
        
        left = 0
        right= len(nums)-1
        
        while left <= right:
             mid = (left + right) //2

             if target == nums[mid]:
                  return mid

             if nums[left] <= nums[mid]:
                #   if nums[mid] > target:
                #        right = mid - 1
                if target > nums[mid] or target < nums[left]:
                     left = mid + 1
                else:
                     right = mid - 1
                
             else:
                  if target > nums[right] or target < nums[mid]:
                       right = mid - 1
                  else:
                       left = mid + 1

        return -1
                  
        

    
result = Solution().search([1,2,3,4], 2)
print("result is ", result)