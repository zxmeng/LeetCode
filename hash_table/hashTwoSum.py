def solve(arr, money):
    # Complete this function
    dict = {}
    for i in range(len(arr)):
        el = arr[i]
        if money - el in dict:
            print dict[money-el], i+1
            return
        else:
            dict[el] = i+1

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        money = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        solve(arr, money)