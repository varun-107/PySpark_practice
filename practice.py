# Find the second largest element in an array
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        maxi = float('-inf')
        ans = -1
        
        for val in arr:
            if val > maxi:
                ans = maxi
                maxi = val
            
            elif val<maxi and val>ans:
                ans=val
        
        if ans<0:
            return -1
            
        return ans

# Check if the array is sorted
class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        
        return True

# Remove duplicates from sorted array
class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        i=0
        
        for j in range(1,len(arr)):
            if arr[i]==arr[j]:
                pass
            
            else:
                arr[i+1], arr[j] = arr[j], arr[i+1]
                i+=1
            
        return i+1      

# Left rotate an array by one
class Solution:
    def rotate(self, arr):
        x=arr[len(arr)-1]
        
        for i in range(len(arr)-1,0,-1):
            arr[i] = arr[i-1]
            
        arr[0] = x

# Rotate an array by d - counterclockwise
class Solution: 
    def rotateArr(self, arr, d):
        left = 0
        right = len(arr)
        
        d=d%len(arr)
        
        arr[left:d] = arr[left:d][::-1]
        arr[d:right] = arr[d:right][::-1]
        arr.reverse()

# Move all zeroes to end
# class Solution:
# 	def pushZerosToEnd(self,arr):
#     	i=0
#     	j=len(arr)-1
    	
#     	while i<=j:
#     	    if arr[i]==0:
#     	       x=i+1
#     	       while x<=j and arr[x]==0:
#     	           x+=1
    	       
#     	       if x>j:
#     	           return
    	       
#     	       arr[i], arr[x] = arr[x], arr[i]
    	   
#     	    i+=1
    	 

# Find the missing number
class Solution:
    def missingNum(self, arr):
        sum = 0
        list_sum=0
        
        for i in range(0,len(arr)):
            list_sum+=arr[i]
            sum+=i+1
        
        sum+=len(arr)+1
        
        return sum-list_sum
    
# Find the maximum consecutive one or zero
class Solution:
    def maxConsecutiveCount(self, arr):
        ans=0
        count_one=0
        count_zero=0
        
        for val in arr:
            if val==1:
                count_one+=1
                ans=max(max(count_one,count_zero),ans)
                count_zero=0
                
            else:
                count_zero+=1
                ans=max(max(count_one,count_zero),ans)
                count_one = 0
        
        return ans
    
# Find the unique number
class Solution:
    def findUnique(self, arr):
        # code here 
        
        nums = 0
        
        for val in arr:
            nums^=val
        
        return nums

# Longest subarray with sum k
class Solution:
    def longestSubarray(self, arr, k):  
        i=0
        j=0
        sum=0
        ans=0
        
        while i<len(arr) and j<len(arr):
            sum+=arr[j]
            
            if sum==k:
                ans=max(ans,j-i+1)
            
            while sum>k and i<=j:
                sum-=arr[i]
                i+=1
            
            j+=1    
        return ans
    
# Two sum - pair with given sum
class Solution:
    def twoSum(self, arr, target):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    return True
        return False  
    
# Two sum - optimised solution
class Solution:
    def twoSum(self, arr, target):
        # code here
        myset=set()
        for i in arr:
            if (target -i) in myset:
                return True
            else:
                myset.add(i)
        return False
    
#sort 0s, 1s, and 2s
class Solution:
    def sort012(self, arr):
        left=-1
        right=len(arr)
        j=0
        
        while left<right and j<right:
            if arr[j]==2:
                arr[right-1], arr[j] = arr[j], arr[right-1]
                right-=1
            
            elif arr[j]==0:
                arr[left+1], arr[j] = arr[j], arr[left+1]
                left+=1
                j+=1
            
            else:
                j+=1
            
# Majority element
class Solution:
    def majorityElement(self, arr):
        arr.sort()
        N=len(arr)
        if arr.count(arr[N//2])>N//2:
           return arr[N//2]
        return -1
