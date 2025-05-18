# PCEP §4.1 – recursion
# Recursive Sum of Integers – implement a recursive function recursive_sum(n)
# that calculates the sum of all positive integers from 1 to n.
# Example Calls:
# recursive_sum(3) should return 6
# recursive_sum(5) should return 15
# recursive_sum(1) should return 1

# Feedback: Not sure where to start so had cline provide the solution.
# will continue to understand it deeper and work through more examples
# makes sense once worked through and explained

def recursive_sum(n):
  # Base Case: If n is 1, the sum is 1. This stops the recursion.
  if n == 1:
    return 1
  else:
    # Recursive Step: The sum of 1 to n is n + the sum of 1 to n-1
    return n + recursive_sum(n-1)

# Example Calls (as requested in the problem)
print(f"recursive_sum(3): {recursive_sum(3)}")
print(f"recursive_sum(5): {recursive_sum(5)}")
print(f"recursive_sum(1): {recursive_sum(1)}")
