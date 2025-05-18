# | 19 | Index-safe fetcher – list `letters = ['a', 'b', 'c']`; 
# print `safe_get(letters, 1)` → `'b'` 
# and `safe_get(letters, 5)` → `"Index error"`.  

# Feedback: originally did listdata[:index] which 
# is slicing not indexing. Other than that got it mostly right

letters = ['a', 'b', 'c']

def safe_get(listdata, index):
  try:
    print(listdata[index])
  except IndexError:
    print(f"Index Error")

safe_get(letters,5)

