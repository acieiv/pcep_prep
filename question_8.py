#	Username validator – start with candidate = "Ace_123". 
# While the value is not only alphanumerics or not 5-12 chars, 
# ask again (you can simulate by editing the variable).	§2.2

candidate = "Ace_123"

if candidate.isalnum():
  print("True")
else:
  print("False")

