# | 20 | Chained exception demo – wrap `int("12.5")` (deliberate `ValueError`). 
# In `except`, re-raise `TypeError("Not a number")` and watch the traceback chain.  

# Feedback: Needed help understanding which exception to catch (ValueError vs TypeError)
# and how to use the 'raise' keyword to re-raise a new exception. But got it on the second try
try:
  int("12.5")
except ValueError as e:
  raise TypeError("Not a number")