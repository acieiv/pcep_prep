# 14	Lookup table – start dict: prices = {"AAA": 2.50, "BBB": 1.75, "CCC": 3.20}.
# Add "DDD": 4.00, raise "AAA" to 2.75, then loop through items() printing CODE → $PRICE.	§3.3

# Feedback: Reasearch how to add, update and loop their dics using .items() on W3

prices = {"AAA": 2.50, "BBB": 1.75, "CCC": 3.20}

prices["DDD"] = 4.00
prices["AAA"] = 2.75

# for x, y in prices.items():
#   print(x, y)
for code, price in prices.items(): # Using more descriptive variable names
  print(f"{code} → ${price}") # Format the output string
