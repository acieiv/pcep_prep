# 9	Triangular heat-map indices – for rows 1-5 print * pyramid:
# *
# **
# ***
# ****
# *****	§2.2


# Feedback: Definitely need to work on control flow and loops
# Commented out solution I tried is below
# star = "*"

# for i in range(1,6):
#   row = print(i)
  
#   for x in row:
#     print(star)
   
# Outer loop for each row (from 1 to 5)
for row_num in range(1, 6): 
  # Inner loop for printing asterisks in the current row
  # The range goes from 0 up to (but not including) row_num 
  # This means for row_num 1, it runs 1 time; for row_num 2, it runs 2 times, etc. 
  for _ in range(row_num): 
    # Print a single asterisk 
    # Use end="" to print the asterisk without a newline, 
    # so subsequent asterisks in the same row stay on the same line 
    print("*", end="") 
  # After the inner loop finishes for a row, print a newline character 
  # to move to the next line for the next row. 
  # An empty print() call by default prints a newline. 
  print()