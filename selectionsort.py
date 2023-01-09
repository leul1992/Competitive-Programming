#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        return arr[i]
        
    
    def selectionSort(self, arr,n):
        #code here
        for index in range(n - 1):
            selected = self.select(arr, index)
            for i in range(index + 1, n):
                if arr[index] > arr[i]:
                    arr[index], arr[i] = arr[i], arr[index]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends