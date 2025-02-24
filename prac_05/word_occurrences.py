"""
Word Occurrences
Estimate: 20 minutes
Actual:   27 minutes
"""

text = input("Text: ").lower()
word_counts = {}
words = text.split()

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_word_counts = sorted(word_counts.items())

max_word_length = max(len(word) for word in word_counts)

for word, count in sorted_word_counts:
    print(f"{word:{max_word_length}} : {count}")
