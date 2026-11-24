
import numpy as np
import pandas as pd

# 1. Create a Series with 10 random numbers
def create_random_series(n=10, seed=42):
    rng = np.random.default_rng(seed)
    values = rng.integers(low=1, high=100, size=n)
    return pd.Series(values)


# 2. Create a Series with custom labels
def create_labeled_series(series):
    labels = [f"num_{i+1}" for i in range(len(series))]
    return pd.Series(series.values, index=labels)


# 3. Display Series details
def describe_series(s, title="Series"):
    print(title)
    print(s)
    print("\nData Type:", s.dtype)
    print("Shape:", s.shape)
    print("Size:", s.size)
    print("Index:", list(s.index))


# 4. Main Program
if __name__ == "__main__":

    # Step 1: Create Series
    series = create_random_series()
    print("STEP 1: Series with Default Index")
    describe_series(series)

    # Step 2: Create Labeled Series
    labeled = create_labeled_series(series)
    print("\nSTEP 2: Series with Custom Labels")
    describe_series(labeled, "Labeled Series")

    # Step 3: Statistical Operations
    print("\nSTEP 3: Basic Statistics")
    print("Minimum:", series.min())
    print("Maximum:", series.max())
    print("Mean:", series.mean())
    print("Sum:", series.sum())

    # Step 4: Sorting
    print("\nSTEP 4: Sorted Series")
    print(series.sort_values())

    # Step 5: Indexing and Filtering
    print("\nSTEP 5: Indexing and Filtering")
    print("First Value:", series.iloc[0])

    print("\nValues Greater Than 50:")
    print(series[series > 50])
