class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        s = 0
        e = len(A) - 1
        while True:
            if s > e:
                return s
            while A[s] != elem and s != e:
                s += 1
            if s == e:
                if A[s] == elem:
                    return s
                else:
                    return s + 1
            while A[e] == elem and s != e:
                e -= 1
            if s == e:
                if A[s] == elem:
                    return s
                else:
                    return s + 1
            A[s] = A[e]
            s += 1
            e -= 1
