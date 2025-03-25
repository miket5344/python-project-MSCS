import math
from itertools import permutations

def factorial(n):
    return math.factorial(n)

def arrangements_of_multisets(subset_sizes, k):
    n = sum(subset_sizes)
    if k > n:
        return 0
    return factorial(n) // factorial(n - k)

def main():
    # Ask the user for the number of subsets
    while True:
        j = int(input("Enter the number of subsets (between 3 and 8): "))
        if 3 <= j <= 8:
            break
        else:
            print("Please enter a number between 3 and 8.")

    # Ask the user for the size of each subset
    subset_sizes = []
    for i in range(j):
        while True:
            mi = int(input(f"Enter the size of subset {i+1} (between 1 and 5): "))
            if 1 <= mi <= 5:
                subset_sizes.append(mi)
                break
            else:
                print("Please enter a size between 1 and 5.")

    # Calculate the total number of elements
    n = sum(subset_sizes)

    # Ask the user for the total number of the arrangement
    while True:
        k = int(input(f"Enter the total number of the arrangement (less than {n}): "))
        if k < n:
            break
        else:
            print(f"Please enter a number less than {n}.")

    # Compute and print the number of arrangements
    num_arrangements = arrangements_of_multisets(subset_sizes, k)
    print(f"The number of arrangements of {k} elements out of {n} is: {num_arrangements}")

if __name__ == "__main__":
    main()
