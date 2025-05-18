# PEP-8 Lint – start with “bad” names:
# Clicks_today = 3580
# TOTAL_sales = 97150
# AvgResponseTIME = 1.73
# Create PEP-8 versions (clicks_today, total_sales, etc.) and print both columns.


# Feedback: Originally got it wrong with 
# tot_sales = TOTAL_sales
# avgresponsetime = AvgResponseTIME


Clicks_today = 3580
TOTAL_sales = 97150
AvgResponseTIME = 1.73

clicks_today = Clicks_today
total_sales = TOTAL_sales
avg_response_time = AvgResponseTIME


# Print both columns side-by-side
print(f"Original: Clicks_today = {Clicks_today}, PEP-8: clicks_today = {clicks_today}")
print(f"Original: TOTAL_sales = {TOTAL_sales}, PEP-8: total_sales = {total_sales}")
print(f"Original: AvgResponseTIME = {AvgResponseTIME}, PEP-8: avg_response_time = {avg_response_time}")