def missingNumber(self, nums: List[int]) -> int:
        s = sorted(nums)
        for index in range(0, len(nums)):
            if s[index] != index:
                return index
        return len(nums)
