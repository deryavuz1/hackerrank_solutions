def search(self, nums: List[int], target: int) -> int:

        # initialize left and right pointer for binary search
        left, right = 0, len(nums) -1

        # not starting exactly from the center
        while left <= right:
            mid = (left + right) // 2

            # if we have found the target in the middle
            if nums[mid] == target:
                return mid
            
            # check the left side of the array if it's sorted
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]: #target is in the left portion
                    right = mid - 1
                else:
                    #target is not in the left but left is sorted
                    left = mid + 1
            else:
                # right is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 # target is in the right
                else:
                    right = mid -1
        
        return -1

        

