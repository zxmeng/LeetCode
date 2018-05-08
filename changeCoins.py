
def make_change(coins, n):
    counter = [0 for i in range(n+1)]
    counter[0] = 1
    
    for el in coins:
        for i in range(el, n+1):
            counter[i] += counter[i - el]

    return counter[n]

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)