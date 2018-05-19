def findLongestSubarrayBySum(s, arr):
    start = 0
    longest = -1
    re = [-1]
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        while sum > s:
            sum -= arr[start]
            start += 1
        if sum == s:
            if longest < i - start:
                longest = i - start
                re = [start+1, i+1]

    return re