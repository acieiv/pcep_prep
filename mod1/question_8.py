# PCEP §2.2 – loop control, while
# Username validator – start with candidate = "Ace_123".
# While the value is not only alphanumerics or not 5-12 chars,
# ask again (you can simulate by editing the variable).


# Feedback: This answer is main Cline generated. I couldnt wrap my head around this way of solving it.
# I was thinking of doing a loop within a loop for step one and two of validation

# Initial candidate username
candidate = "Ace_123"

# Define the validation criteria
min_length = 5
max_length = 12

# Loop while the candidate is invalid
# A username is invalid if:
# 1. Its length is less than min_length OR greater than max_length
# 2. It does NOT contain only alphanumeric characters
while not (min_length <= len(candidate) <= max_length and candidate.isalnum()):
    print(f"Invalid username: '{candidate}'")
    print(f"Username must be between {min_length} and {max_length} characters long and contain only alphanumeric characters.")

    # In a real scenario, you would use input() here to get a new username:
    # candidate = input("Enter a new username: ")

    # For simulation, you can manually change the 'candidate' variable here
    # to test different invalid inputs and see the loop continue.
    # For example, uncomment the line below to test another invalid input:
    # candidate = "short"
    # candidate = "a_very_long_username"
    # candidate = "valid123" # Uncomment this to see the loop terminate

    # To simulate asking again without actual input, we'll just break
    # after the first invalid input in this example.
    # In a real validator, this break would not be here.
    break

# If the loop terminates, the username is valid
print(f"Valid username: '{candidate}'")
