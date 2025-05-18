# Friendly I/O header – prompt with three fixed 
# sample answers (name → “Casey”, team → “DataOps”, goal → “ship dashboard v2”). 
# Echo them using print(sep=' • ', end='🚀\n').	§1.5

name = "Casey"
team = "DataOps"
goal = "ship dashboard v2"

# Feedback: Initially tried to use f strings here but
# ofc you need to use multiple args since f string 
# passing in one

# print(f"name = {name}")
# print(f"team = {team}")
# print(f"goal = {goal}")
print(name, team, goal, sep=' • ', end='🚀\n')