class Solution(object):

    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


def main():
    assert Solution().toLowerCase("Hello") == "hello"
    assert Solution().toLowerCase("here") == "here"
    assert Solution().toLowerCase("LOVELY") == "lovely"


if __name__ == "__main__":
    main()
