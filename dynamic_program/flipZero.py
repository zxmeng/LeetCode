import numpy as np

arr=[1, 0, 0, 1, 1, 1, 0, 1, 0, 0]

N = 2
M = len(arr)

dp = [[0 for i in range(N+1)] for j  in range(M)]

if arr[0] == 1:
	for i in range(N+1):
		dp[0][i] = 1

count = 0
for i in range(M):
  if arr[i] == 1:
    count += 1
  else:
    count = 0
  dp[i][0] = count

for j in range(1, N+1):
  for i in range(1, M):
    if arr[i] == 1:
      dp[i][j] = dp[i-1][j] + 1
    else:
      dp[i][j] = dp[i-1][j-1] + 1

print(np.max(dp))



