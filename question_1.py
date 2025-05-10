# Binary dashboard – yesterday’s hits are already in a list:
# hits = [127, 512, 95, 8192, 42]
# Print a table showing DEC, BIN, OCT, HEX for each value.	§1.3, §1.4

# Feedback: Originally didnt know the ask based on the question
# hits list wasnt provided leading me to be confused
# ultimately wont have been able to come up with this solution 
# due to lack of experience with DEC, BIN, OCT, and HEX

# Yesterday’s raw hit counts
hits = [127, 512, 95, 8_192, 42]      # plain integers, underscores just aid readability

# Column headers
print(f"{'DEC':>10}  {'BIN':>12}  {'OCT':>8}  {'HEX':>6}")
print("-" * 42)

for n in hits:
    print(f"{n:>10d}  {bin(n):>12}  {oct(n):>8}  {hex(n):>6}")
