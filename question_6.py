# Graded KPI alert – given sample KPI on_time_pct = 83.7,
# use if-elif-else to classify: ≥95 → Excellent,
# 90-94 → Acceptable, 80-89 → Warning, else → Critical.	§2.1


# Feedback: Got it first try but added unnessary conditions

# Original:
on_time_pct = 83.7

if on_time_pct >= 95:
  print("Excellent")
elif on_time_pct <= 94 and on_time_pct >= 90:
  print("Acceptable") 
elif on_time_pct <= 89 and on_time_pct >= 80:
  print("Warning") 
else:
  print("Critical") 


# refined version: 
# on_time_pct = 83.7

# if on_time_pct >= 95:
#     print("Excellent")
# elif on_time_pct >= 90:
#     print("Acceptable")
# elif on_time_pct >= 80:
#     print("Warning")
# else:
#     print("Critical")