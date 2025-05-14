# 12	One-liner %-change – on the same sales list, build 
# pct_change = [(sales[i]-sales[i-1])/sales[i-1]*100 for i in range(1, len(sales))] 
# and print it.	§3.1

sales = [120, 310, 98, 215, 180, 330, 260]

pct_change = [(sales[i]-sales[i-1])/sales[i-1]*100 for i in range(1, len(sales))] 

print(pct_change)