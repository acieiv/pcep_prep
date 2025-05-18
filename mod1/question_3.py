# Float accuracy check – compute x = 0.1 * 10 and compare to y = 1.0;
# print both with repr() plus the Boolean result of x == y.	§1.4

# Feedback: got it right without much of a struggle
# still not understanding the usecase of repr though
# seems like it is only used to take in an object, 
# and turn it into a string to compare two strings

x = 0.1 * 10
y = 1.0

# Print both with repr()
print(f"repr(x): {repr(x)}")
print(f"repr(y): {repr(y)}")

# Print the boolean result of the comparison
print(f"x == y: {x == y}")