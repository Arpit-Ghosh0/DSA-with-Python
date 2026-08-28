# Linear Search
# What is Linear Search?
# Linear search checks each element of an array/list one by one until it finds the target element.


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

arr = [10,25,30,87]
target = 87

result = linear_search(arr,target)
print(result)