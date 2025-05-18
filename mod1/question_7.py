# Odd-even batch splitter – 
# loop over hard-coded IDs range(1000, 1016); 
# build odds and evens, then print them.	§2.2

# Feedback: took a few tries but managed to get it 
# without major assistance just a few hints

odds = []
evens = []

for i in range(1000,1016):
  if i % 2 == 0:
    evens.append(i)
  else:
    odds.append(i)

print(f"odds: {odds}")
print(f"evens: {evens}")