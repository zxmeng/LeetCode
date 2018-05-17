
def findSum(used, unused, rest):
    if rest == 0:
        return [used], True
    
    re = []
    found = False
    prev = -1
    for i in range(len(unused)):
        if unused[i] != prev:
            if rest - unused[i] >= 0:
                temp, flag = findSum(used + [unused[i]], unused[i+1:], rest - unused[i])
                if flag:
                    found = True
                    re += temp
            prev = unused[i]
            
    return re, found

def sumSubsets(arr, num):
    if not arr:
        return [[]]
    
    re = []
    prev = -1
    for i in range(len(arr)):
        if arr[i] != prev:  
            if num - arr[i] >= 0:
                temp, flag = findSum([arr[i]], arr[i+1:], num - arr[i])
                if flag:
                    re += temp
            prev = arr[i]

    if re == []:
        return [[]]
    return sorted(re)
            

