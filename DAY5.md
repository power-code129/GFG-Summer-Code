# Next Permutation

Given an array arr[] of size n, the task is to print the lexicographically next greater permutation of the given array. If there does not exist any greater permutation, then find the lexicographically smallest permutation of the given array.

Let us understand the problem better by writing all permutations of [1, 2, 4] in lexicographical order: [1, 2, 4], [1, 4, 2], [2, 1, 4], [2, 4, 1], [4, 1, 2] and [4, 2, 1]. If we give any of the above (except the last) as input, we need to find the next one in sequence. If we give last as input, we need to return the first one.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is 2 4 5 0 1 7

Input: arr = {3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation. So, the next permutation is the lowest one.

Input: arr = [1, 3, 5, 4, 2]
Output: [1, 4, 2, 3, 5]
Explanation: The next permutation of the given array is found by rearranging the elements in the next lexicographical order.

Table of Content

[Naive Approach] Generating All - O(n!*n*log(n!)) Time and Space
[Expected Approach] Generating Only Next - O(n) Time and O(1) Space
Using C++ in-built function
[Naive Approach] Generating All Permutations - O(n!*n*log(n!)) Time and O(n!) Space
The very basic idea that comes to our mind is that we would first generate all possible permutations of a given array and sort them. Once sorted, we locate the current permutation within this list. The next permutation is simply the next arrangement in the sorted order. If the current arrangement is the last in the list then display the first permutation (smallest permutation).

Note: This approach will work only when there are no duplicated in the input array. Please refer the expected approach to handle duplicates.




### Python Program to find the next permutation by generating all permutations

    #Generates all permutations
    def permutations(res, arr, idx):
    
    # Base case: if idx reaches the end of the list
    if idx == len(arr) - 1:
        res.append(arr[:])
        return

    # Generate permutations by swapping each
    # element starting from index `idx`
    for i in range(idx, len(arr)):
        
        # Swapping
        arr[idx], arr[i] = arr[i], arr[idx]

        # Recursive call to create permutations 
        # for the next element
        permutations(res, arr, idx + 1)

        # Backtracking
        arr[idx], arr[i] = arr[i], arr[idx]


    def next_permutation(arr):
    
    # Begin with the smallest permutation
    curr = arr[:]

    # Generate all permutations and store in res
    res = []
    permutations(res, curr, 0)
    res.sort()

    # Traverse through res and print the next permutation
    for i in range(len(res)):
        
        # Found a match
        if res[i] == arr:
            
            # Print next
            if i < len(res) - 1:
                arr[:] = res[i + 1]
                
            else:
                
                # If the given permutation is 
                # the last
                arr[:] = res[0]
            
            break


    if __name__ == "__main__":
    arr = [2, 4, 1, 7, 5, 0]
    next_permutation(arr)
    print(" ".join(map(str, arr)))

Output
2 4 5 0 1 7 
Time Complexity: O(n!*n*log(n!)), n represents the number of elements present in the input sequence represent all possible permutation.
Auxiliary Space: O(n!), for storing the permutations

### [Expected Approach] Generating Only Next - O(n) Time and O(1) Space
Let's try some examples to see if we can recognize some patterns. 

[1, 2, 3, 4, 5]: next is [1, 2, 3, 5, 4]
Observation: 4 moves and 5 comes in place of it

[1, 2, 3, 5, 4]: next is [1, 2, 4, 3, 5]
Observation: 3 moves, 4 comes in place of it. 3 comes before 5 (mainly 3 and 5 are in sorted order)

[1, 2, 3, 6, 5, 4]: next is [1, 2, 4, 3, 5, 6]
Observation: 3 moves, 4 comes in place of it. [3, 5 and 6 are placed in sorted order]

[3, 2, 1]: next is [1, 2, 3]
Observation: All elements are reverse sorted. Result is whole array sorted.

[1, 2, 3, 6, 4, 5]: next is [1, 2, 3, 6, 5, 4]
Observation: 4 moves and 5 comes in place of it

Observations of Next permutation: 

To get the next permutation we change the number in a position which is as right as possible.
The first number to be moved is the rightmost number smaller than its next.
The number to come in-place is the rightmost greater number on right side of the pivot.
Each permutation (except the very first) has an increasing suffix. Now if we change the pattern from the pivot point (where the increasing suffix breaks) to its next possible lexicographic representation we will get the next greater permutation.

To understand how to change the pattern from pivot, see the below image:

Next-permutation.webpNext-permutation.webp

Follow the steps below to implement the above observation:

Iterate over the given array from end and find the first index (pivot) which doesn't follow property of non-increasing suffix, (i.e,  arr[i] < arr[i + 1]).
If pivot index does not exist, then the given sequence in the array is the largest as possible. So, reverse the complete array. For example, for [3, 2, 1], the output would be [1, 2, 3]
Otherwise, Iterate the array from the end and find for the successor (rightmost greater element) of pivot in suffix.
Swap the pivot and successor
Minimize the suffix part by reversing the array from pivot + 1 till n.



### Python Program to find the next permutation by generating only next

    def next_permutation(arr):
    n = len(arr)
    
    # Find the pivot index
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    
    # If pivot point does not exist, 
    # reverse the whole array
    if pivot == -1:
        arr.reverse()
        return

    # Find the element from the right 
    # that is greater than pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reverse the elements from pivot + 1 to the end in place
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


    arr = [ 2, 4, 1, 7, 5, 0 ]
    next_permutation(arr)
    print(" ".join(map(str, arr)))

Output
2 4 5 0 1 7 
Time Complexity: O(n), where n is the size of the given array.
Auxiliary Space: O(1), The algorithm performs in-place operations (modifying the array directly) without using extra space proportional to the input size.

## Using C++ in-built function
C++ provides an in-built function called next_permutation(), that return directly lexicographically in the next greater permutation of the input.




    #include <algorithm>
    #include <iostream>
    #include <vector>
    using namespace std;

    int main()
    {
    vector<int> arr = { 2,4,1,7,5,0 };
    next_permutation(arr.begin(), arr.end());
    for (int num : arr)
        cout << num << " ";
    return 0;
    }

Output
2 4 5 0 1 7 
Time Complexity: O(n), as all operations are linear with respect to the array's size.
Auxiliary Space: O(1), The algorithm performs in-place operations (modifying the array directly) without using extra space proportional to the input size
