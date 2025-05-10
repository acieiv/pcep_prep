Below is a self-contained revision of the 20-exercise “problem bank.”
Every task now ships with built-in sample data (or a concrete input prompt) so you can drop each snippet into a fresh file and run it immediately—no guesswork about what the variables should look like.

Section 1 • Computer Programming & Python Fundamentals
(Problems 1 – 5)

#	Hands-on exercise (ready-to-run context)	PCEP link
1	Binary dashboard – yesterday’s hits are already in a list:
hits = [127, 512, 95, 8192, 42]
Print a table showing DEC, BIN, OCT, HEX for each value.	§1.3, §1.4
2	PEP-8 Lint – start with “bad” names:
Clicks_today = 3580
TOTAL_sales = 97150
AvgResponseTIME = 1.73
Create PEP-8 versions (clicks_today, total_sales, etc.) and print both columns.	§1.2, §1.3
3	Float accuracy check – compute x = 0.1 * 10 and compare to y = 1.0; print both with repr() plus the Boolean result of x == y.	§1.4
4	Bit-mask flagging – sample packed flag: packed = 0b1101 (13). Unpack four 1-bit sensors A-D and report which fired.	§1.4
5	Friendly I/O header – prompt with three fixed sample answers (name → “Casey”, team → “DataOps”, goal → “ship dashboard v2”). Echo them using print(sep=' • ', end='🚀\n').	§1.5

Section 2 • Control Flow
(Problems 6 – 10)

#	Exercise (context baked in)	PCEP link
6	Graded KPI alert – given sample KPI on_time_pct = 83.7, use if-elif-else to classify: ≥95 → Excellent, 90-94 → Acceptable, 80-89 → Warning, else → Critical.	§2.1
7	Odd-even batch splitter – loop over hard-coded IDs range(1000, 1016); build odds and evens, then print them.	§2.2
8	Username validator – start with candidate = "Ace_123". While the value is not only alphanumerics or not 5-12 chars, ask again (you can simulate by editing the variable).	§2.2
9	Triangular heat-map indices – for rows 1-5 print * pyramid:
*
**
***
****
*****	§2.2
10	Prime ⇄ Composite tracer – iterate 2-30; nested loop tests divisors; use for-else to announce “prime” when no divisor found.
No user input needed.	§2.2

Section 3 • Data Collections
(Problems 11 – 15)

#	Exercise (with sample structures)	PCEP link
11	Daily sales vector – list provided: sales = [120, 310, 98, 215, 180, 330, 260] (Mon-Sun). Slice weekend (sales[5:]), then print min/mean/max of those two days.	§3.1
12	One-liner %-change – on the same sales list, build pct_change = [(sales[i]-sales[i-1])/sales[i-1]*100 for i in range(1, len(sales))] and print it.	§3.1
13	Immutable coordinates – tuple: pt = (1.0, -2.5, 3.2); try pt[0] = 99 (expect TypeError, catch in a comment or try/except), then make pt = (99.0, pt[1], pt[2]).	§3.2
14	Lookup table – start dict: prices = {"AAA": 2.50, "BBB": 1.75, "CCC": 3.20}. Add "DDD": 4.00, raise "AAA" to 2.75, then loop through items() printing CODE → $PRICE.	§3.3
15	Tokenized sentence stats – sample sentence: "Data beats opinions every single time". Split, build list of word lengths, then print longest word + its length.	§3.4

Section 4 • Functions & Exceptions
(Problems 16 – 20)

#	Exercise (sample calls included)	PCEP link
16	Reusable mean() – implement, then call: ① mean([2, 4, 6]) expected 4.0; ② mean([3]) expected 3.0.	§4.1
17	Recursive factorial – define factorial(n); print factorial(5) (should be 120).	§4.1
18	Flexible histogram – sample list data = [3, 1, 4].
Call hist(data) and hist(data, char='*') to show default vs. keyword-arg override.	§4.2
19	Index-safe fetcher – list letters = ['a', 'b', 'c']; print safe_get(letters, 1) → 'b' and safe_get(letters, 5) → "Index error".	§4.3, §4.4
20	Chained exception demo – wrap int("12.5") (deliberate ValueError). In except, re-raise TypeError("Not a number") and watch the traceback chain.	§4.3, §4.4

How to drill efficiently ✔️
Copy just the “context” snippet into a fresh file, then code the logic underneath.

Comment the top line of each script with its syllabus reference, e.g.
# PCEP §3.1 – lists / slicing / len()

Time yourself—aim for < 6 minutes per exercise to simulate exam pressure.

Tweak the sample data once you’re done (change numbers, add edge cases) to prove your code is general.

Happy coding, and may the 🎖 PCEP badge be yours soon!
