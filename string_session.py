from collections import Counter

str1 = "Prjectpro has a good mentor platform. Projectpro is a good company."

res1 = str1.split(" ")
res1
res2 = Counter(res1)
res2

##############################

# Sample string
text = "the quick brown fox jumps over the lazy dog the quick brown dog"

# Count word frequencies
word_freq = {}
words = text.split(" ")
for word in words:
    print(word_freq.get(word, 0))
    word_freq[word] = word_freq.get(word, 0) + 1
    print(word,word_freq[word],word_freq.get(word, 0))
print(word_freq)
# Sort words by frequency in descending order
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Display words in descending order of frequency
for word, freq in sorted_words:
    print(word, freq)

# Sample string
text = "the quick brown fox jumps over the lazy dog the quick brown dog"

# Count word frequencies
word_freq = {}
words = text.split()
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Sort words by frequency in descending order
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Display words in descending order of frequency
for word, freq in sorted_words:
    print(word, freq)


text = "the quick brown fox jumps over the lazy dog the quick brown dog"

text_split = text.split(" ")
a = text_split[0].lower()
b = "".join(word.capitalize() for word in text_split[1:])
c = a+b
c
text_resverse = text_split[ : : -1]
text_resverse

word1 = "ate"
word2  = "eat"

word1_counter =  Counter(word1)
word2_counter = Counter(word2)
print(word1_counter==word2_counter)

s1_sorted = ''.join(sorted(word1))
s2_sorted = ''.join(sorted(word2))
s1_sorted
s2_sorted

# x = "jjjaacccc"
# 3j2a4c


