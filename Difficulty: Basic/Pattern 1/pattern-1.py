#User function Template for python3

class Solution:
    def printSquare(self, N):
        for i in range (1, N+1):
            for j in range (1, N+1):
                print("*", end=" ")
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printSquare(N)
# } Driver Code Ends