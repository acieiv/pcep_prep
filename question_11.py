# Daily sales vector: 
# Given a list [120, 310, 98, 215, 180, 330, 260] (Mon-Sun), 
# slice out the weekday sales, compute min/mean/max manually, and print summary.

# Feedback: mostly got it. Cline offered output improvements

sales = [120, 310, 98, 215, 180, 330, 260]

wkday_sales = sales[:5]
# wkend_sales = sales[5:]  # Saturday and Sunday
min_sales = min(wkday_sales)
mean_sales = sum(wkday_sales) / len(wkday_sales)
max_sales = max(wkday_sales)

print(f"""Output Summary: 
        
sales list: {sales}
wkday sales list: {wkday_sales}
min sales: {min_sales}
mean sales: {mean_sales}
max sales: {max_sales} 
""")