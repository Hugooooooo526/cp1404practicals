"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""
# string
text = input("Text: ")
#list
words = text.split()
#new a dictiory
word_frequency = {}

for word in words:
    if word in word_frequency:
        #give the keys and value. key element is word 
        word_frequency[word] += 1
    else:
        #first time than value it 1
        word_frequency[word] = 1

#base on value to sort "x:x[1]"
sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

for word, frequency in sorted_word_frequency:
    print(f"{word:15}: {frequency}")