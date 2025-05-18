# | 18 | Flexible `hist()` – sample list `data = [3, 1, 4]`.
# <br> Call `hist(data)` and `hist(data, char='*')` 
# to show default vs. keyword-arg override. 


# Feedback: got it the first time but needed to get
# an hint for string multiplication and googled how to do it 

data = [3, 1, 4]

def hist(data, char='*'):
  for x in data:
    print(char*x)

hist(data)