class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums.sort()
        #return sum([nums[num] for num in xrange(0, len(nums)) if num % 2 == 0])
        return sum(sorted(nums)[::2])


def main():
    print("test")
    assert Solution().arrayPairSum([1, 4, 3, 2]) == 4
    assert Solution().arrayPairSum([1, 2, 3, 2]) == 3
    assert Solution().arrayPairSum([-1, 1, 4, 3, 2, 7]) == 5



if __name__ == '__main__':
    main()