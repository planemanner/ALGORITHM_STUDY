

def factorial(N):
    # Time Complexity : O(N)
    if N == 1:
        return 1
    else:
        return N * factorial(N-1)