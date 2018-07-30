class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #return [self.flipAndInvertRow(row, len(row)) for row in A]
        l = len(A[0])
        for row in A:
            for i in xrange(0, (l+1)/2):
                if row[i] == row[~i]:
                    row[i] = row[~i] = row[i] ^ 1
        return A

def main():
    A = [[1,1,0],[1,0,1],[0,0,0]]
    B = [[1,0,0],[0,1,0],[1,1,1]]
    print(Solution().flipAndInvertImage(A))
    #assert ''.join(Solution().flipAndInvertImage(A)) == ''.join(B)

    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    B = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    print(Solution().flipAndInvertImage(A))
    #assert ''.join(Solution().flipAndInvertImage(A)) == ''.join(B)
    print(Solution().flipAndInvertImage([[0]]))
    print(Solution().flipAndInvertImage([[1, 1]]))
    print(Solution().flipAndInvertImage([[0, 1]]))
    print(Solution().flipAndInvertImage([[1, 0]]))
    print(Solution().flipAndInvertImage([[0, 0]]))

if __name__ == '__main__':
    main()