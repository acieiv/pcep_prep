# PCEP §2.2 – for-else, break
# Prime ⇄ Composite tracer – iterate 2-30;
# nested loop tests divisors;
# use for-else to announce “prime” when no divisor found.
# No user input needed.


# Feedback: Completed the first loop successfully but
# the inner loop "for j in range (2,i) followed by the
# conditional statement I couldnt figure out"

for i in range(2, 31):
    # Assume the number is prime initially
    # We check for divisors from 2 up to i-1
    for j in range(2, i):
        # If i is divisible by j, it's not prime
        if i % j == 0:
            # Print that it's composite (optional, but good for tracing)
            print(f"{i} is composite (divisible by {j})")
            break  # Exit the inner loop

    # This else block is paired with the inner for loop
    # It executes if the inner loop completed without hitting a break
    else:
        # If no divisors were found, the number is prime
        print(f"{i} is prime")
