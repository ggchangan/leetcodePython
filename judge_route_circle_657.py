class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        return moves.count('R') == moves.count("L") and moves.count("U") == moves.count("D")


def main():
    assert Solution().judgeCircle("UD")
    assert Solution().judgeCircle("LL") == False
    assert Solution().judgeCircle("LLRR")


if __name__ == '__main__':
    main()