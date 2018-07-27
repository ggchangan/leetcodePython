
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")
        codes = [''.join([MORSE[ord(c)-97] for c in word]) for word in set(words)]
        return len(set(codes))

def main():
    assert Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2
    assert Solution().uniqueMorseRepresentations([]) == 0

    return 0


if __name__ == '__main__':
    main()