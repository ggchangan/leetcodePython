class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


def main():
    assert bin(7).count('1') == 3
    assert bin(1).count('1') == 1
    assert Solution().hammingDistance(1, 4) == 2
    assert Solution().hammingDistance(11, 4) == 4


if __name__ == '__main__':
    main()
