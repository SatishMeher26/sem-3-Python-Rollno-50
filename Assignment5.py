def build_lcs_table(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def find_lcs(dp, seq1, seq2):
    i = len(seq1)
    j = len(seq2)

    result = []

    # Start from bottom-right
    while i > 0 and j > 0:

        if seq1[i - 1] == seq2[j - 1]:
            result.append(seq1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Reverse the result
    result.reverse()

    return "".join(result)


# Main program
seq1 = input("Enter first sequence: ")
seq2 = input("Enter second sequence: ")

dp = build_lcs_table(seq1, seq2)

lcs = find_lcs(dp, seq1, seq2)

print("Longest Common Subsequence:", lcs)
print("Length:", len(lcs))