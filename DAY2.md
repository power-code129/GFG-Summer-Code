# Move all zeros to end of array

Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

### Examples: 

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: arr[] = [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: arr[] = [0, 0]
Explanation: No change in array as there are all 0s.

## Table of Content

[Naive Approach] Using Temporary Array - O(n) Time and O(n) Space
[Better Approach] Two Traversals
[Expected Approach] One Traversal
[Another Approach] Using Library Methods
[Naive Approach] Using Temporary Array - O(n) Time and O(n) Space
The idea is to create a temporary array of same size as the input array arr[].

First, copy all non-zero elements from arr[] to the temporary array.
Then, fill all the remaining positions in temporary array with 0.
Finally, copy all the elements from temporary array to arr[].
Working:

Move-all-zeros-to-end-using-Temporary-Array.webpMove-all-zeros-to-end-using-Temporary-Array.webp



### Python Program to move all zeros to the endfunction to move all zeroes to the end
    def pushZerosToEnd(arr):
    n = len(arr)
    temp = [0] * n  
    
    # to keep track of the index in temp[]
    j = 0

    # Copy non-zero elements to temp[]
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    # Fill remaining positions in temp[] with zeros
    while j < n:
        temp[j] = 0
        j += 1

    # Copy all the elements from temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]

    if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)

    # Print the modified array
    for num in arr:
        print(num, end=" ")

Output
1 2 4 3 5 0 0 0 
[Better Approach] Two Traversals
The idea is to move all the zeros by traversing the array twice.

### First Traversal: Shift non-zero elements

Traverse the array and maintain the count of non-zero elements. This count is initialized with 0 and keeps track of where the next non-zero element should be placed in the array.
If the element is non-zero, place it at arr[count] and increment count by 1.
After traversing all the elements, all non-zero elements will be shifted to the front while maintaining their original order.
Second Traversal: Fill remaining positions with zeros

After the first traversal, all non-zero elements will be at the start of the array and count will store the index where the first zero should be placed.
Iterate from count to the end of array and fill all indices with 0.
Working:

Move-all-zeros-to-end-using-Two-Traversals-1-copy.webpMove-all-zeros-to-end-using-Two-Traversals-1-copy.webp



# Python Program to move all zeros to end using two traversals

# Function which pushes all zeros to end
    def pushZerosToEnd(arr):
    
    # Count of non-zero elements
    count = 0  

    # If the element is non-zero, replace the element at
    # index 'count' with this element and increment count
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to
    # the front. Make all elements 0 from count to end.
    while count < len(arr):
        arr[count] = 0
        count += 1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")

Output
1 2 4 3 5 0 0 0 
Time Complexity: O(n), as we are traversing the array only twice.
Auxiliary Space: O(1)

## [Expected Approach] One Traversal
The idea is similar to the previous approach where we took a pointer, say count to track where the next non-zero element should be placed. However, on encountering a non-zero element, instead of directly placing the non-zero element at arr[count], we will swap the non-zero element with arr[count]. This will ensure that if there is any zero present at arr[count], it is pushed towards the end of array and is not overwritten.

Working:

Move-all-zeros-to-end-using-One-Traversal-copy.webpMove-all-zeros-to-end-using-One-Traversal-copy.webp



### Python Program to move all zeros to end using one traversalFunction which pushes all zeros to end of array
    def pushZerosToEnd(arr):
    
    # Pointer to track the position for next non-zero element
    count = 0
    
    for i in range(len(arr)):
        
        # If the current element is non-zero
        if arr[i] != 0:
            
            # Swap the current element with the 0 at index 'count'
            arr[i], arr[count] = arr[count], arr[i]
            
            # Move 'count' pointer to the next position
            count += 1

    if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")

Output
1 2 4 3 5 0 0 0 
Time Complexity: O(n), as we are traversing the array only once.
Auxiliary Space: O(1)

### [Another Approach] Using Library Methods
In C++, there exists a method stable_parition() that we can directly use here to implement the above method.




### // C++ Program to move zeros to the end using Library Methods

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void pushZerosToEnd(vector<int> &arr) {
    stable_partition(arr.begin(), arr.end(), [](int n) { 
                                       return n != 0; });
}

int main() {
    vector<int> arr = {1, 2, 0, 4, 3, 0, 5, 0};
    pushZerosToEnd(arr);
    for (int i : arr)
        cout << i << ' ';
    return 0;
}

Output
1 2 4 3 5 0 0 0 
