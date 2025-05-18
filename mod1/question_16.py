# | 16 | Reusable `mean()` – implement, then call:
# ① `mean([2, 4, 6])` expected 4.0;
# ② `mean([3])` expected 3.0.
# | §4.1        |

# Feedback: Remember to use assignment operators (like = or +=) 
# to update variable values within loops or calculations.

list1 = [2, 4, 6]
list2 = [3]

def reusable_mean(number_list):
  list_len = len(number_list)
  total = 0
  for num in number_list:
    total += num
  print(f"total: {total}")
  print(f"list_len: {list_len}")
  return total / list_len

mean1 = reusable_mean(list1)
print(mean1)

mean2 = reusable_mean(list2)
print(mean2)