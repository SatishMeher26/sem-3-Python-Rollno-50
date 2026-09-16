# 0/1 Knapsack - Top Down and Bottom Up

# ---------------- TOP DOWN ----------------

def knapsack_top_down(weights, values, capacity):

    n = len(weights)
    memo = {}

    def solve(i, cap):

        if i == 0 or cap == 0:
            return 0

        if (i, cap) in memo:
            return memo[(i, cap)]

        # If item cannot fit
        if weights[i - 1] > cap:
            result = solve(i - 1, cap)

        else:
            # Include the item
            include = values[i - 1] + solve(
                i - 1,
                cap - weights[i - 1]
            )

            # Exclude the item
            exclude = solve(i - 1, cap)

            result = max(include, exclude)

        memo[(i, cap)] = result
        return result

    return solve(n, capacity)


# ---------------- BOTTOM UP ----------------

def knapsack_bottom_up(weights, values, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):

        for w in range(capacity + 1):

            if weights[i - 1] > w:
                # Item cannot fit
                dp[i][w] = dp[i - 1][w]

            else:
                # Exclude item
                exclude = dp[i - 1][w]

                # Include item
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]

                dp[i][w] = max(include, exclude)

    return dp[n][capacity]


# ---------------- MAIN PROGRAM ----------------

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Weights:", weights)
print("Values :", values)
print("Capacity:", capacity)

top_down = knapsack_top_down(weights, values, capacity)
bottom_up = knapsack_bottom_up(weights, values, capacity)

print("\nTop-Down Result:", top_down)
print("Bottom-Up Result:", bottom_up)