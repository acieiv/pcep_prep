# | 15 | Tokenized sentence stats – sample sentence: `"Data beats opinions every single time"`. 
# Split, build list of word lengths, then report the longest word + its length.                                                        | §3.4        |


# Feedback: I managed to get the gist of it and
# was able to print the list of words with length
# but the if condition with in the for loop still remains
# a challenge

sentence = "Data beats opinions every single time"

x = sentence.split()

word_list = []
max_length = 0
longest_word = ""

for current_word in x:
  current_length = len(current_word)
  if current_length > max_length:
    max_length = current_length
    longest_word = current_word

  word_list.append(f"{current_word}: {len(current_word)}")

print(f"word_list: {word_list}")
print(f"The longest word is '{longest_word}' with length {max_length}")