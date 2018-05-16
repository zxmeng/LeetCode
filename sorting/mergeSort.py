
def mergeSort(arr):
    total = len(arr)
    if total == 0 or total == 1:
        return arr, 0
    if total == 2:
        if arr[0] > arr[1]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            return arr, 1
        else:
            return arr, 0
    
    left = arr[:total/2]
    right = arr[total/2:]
    
    left, count_l = mergeSort(left)
    right, count_r = mergeSort(right)
    
    new = []
    i = 0
    j = 0
    count = count_l + count_r
    while(i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
            count += len(left) - i
    
    while(i < len(left)):
        new.append(left[i])
        i += 1
    while(j < len(right)):
        new.append(right[j])
        j += 1
        
    return new, count

def countInversions(arr):
    _, count = mergeSort(arr)
    return count
        
if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = countInversions(arr)
        print result

