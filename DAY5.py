class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = -1
        
        # Step 1: Find the pivot
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        
        # If no pivot, array is in descending order, reverse to smallest permutation
        if pivot == -1:
            arr.reverse()
            return
        
        # Step 2: Find the next greater element from the end
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break   # ✅ Important: break after swap
        
        # Step 3: Reverse the suffix
        left, right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
