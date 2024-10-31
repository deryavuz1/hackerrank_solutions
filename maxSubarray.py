  def maxSubArray(self, nums: List[int]) -> int:
        # begin from the first element to initialize
        max_sum = current_sum = nums[0]

        #traverse through array
        for n in nums[1:]:
            # update current sum - if max_sum is bigger, it becomes max_sum, else add
            current_sum = max(n, current_sum + n)
            # we only need to add once to current sum. if current sum became bigger, use it
            max_sum = max(current_sum, max_sum)

        return max_sum
