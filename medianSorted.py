 def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # swap to ensure the first array is the     smallest one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m #indices within small array to look for partition

        while left <= right:
            # partition the 1st array, get the floor index
            partition1 = (left + right) // 2
            # partition the second, larger array subtract the smaller portion
            partition2 = (n + m + 1) // 2 - partition1

            # Handle edge cases where partition is at the beginning or end
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # valid partition!
            if max_left1 <= min_right2 and max_left2 <= min_right2:
                # partition valid
                # if length is odd for merged arrays, return median
                if (m + n) % 2 != 0:
                    return max(max_left1, max_left2)
                else:
                    return max(max(max_left1, max_left2) + min(min_right1, min_right2) / 2)
                 # If total length is even, return the average of the middle two elements

