import sys

def hvlcs(A, B, value):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = max(dp[i-1][j-1] + value[A[i-1]], dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if A[i-1] == B[j-1] and dp[i][j] == dp[i-1][j-1] + value[A[i-1]]:
            result.append(A[i-1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return dp[m][n], ''.join(result)


def main():
    # Use file argument if provided, else stdin
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = f.read().split()
    else:
        data = sys.stdin.read().split()

    K = int(data[0])
    idx = 1

    value = {}
    for _ in range(K):
        c = data[idx]
        v = int(data[idx + 1])
        value[c] = v
        idx += 2

    A = data[idx]
    B = data[idx + 1]

    max_value, lcs = hvlcs(A, B, value)
    print(max_value)
    print(lcs)


if __name__ == "__main__":
    main()