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
