# 13	Immutable coordinates – tuple: pt = (1.0, -2.5, 3.2); try pt[0] = 99 
# (expect TypeError, catch in a comment or try/except), 
# then make pt = (99.0, pt[1], pt[2]).	§3.2


# Feedback: Pretty straight forward but Cline suggested 
# 1. added print statement on error, 
# 2. adding specific error type aka TypeError 
# 3. adding ending print statemnt for confirmation

pt = (1.0, -2.5, 3.2)
print(pt)

try:
  pt[0] = 99
except TypeError:
  print("Caught TypeError: Tuples are immutable.")
  pt = (99.0, pt[1], pt[2])

print(pt)