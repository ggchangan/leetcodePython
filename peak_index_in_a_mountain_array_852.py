class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for index in range(1, len(A)):
            if A[index] < A[index-1]:
                return index-1


def main():
    assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 2, 3, 4, 6, 4, 1, 0]) == 4



if __name__ == '__main__':
    main()