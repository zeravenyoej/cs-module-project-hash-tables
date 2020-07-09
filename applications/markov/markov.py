import random

cache = {}

# Read in all the words in one go
with open("./input.txt") as f:
    words = f.read()

words = words.split()

for i in range(len(words)):
    if words[i] not in cache:
        cache[words[i]] = []
    if i+1 < len(words):
        cache[words[i]].append(words[i+1])

start_words = []
stop_words = []

for word in words:
    if (word[0].isupper()):
        start_words.append(word)
    if word.startswith('"') and word[1].isupper():
        start_words.append(word)
    if word[len(word)-1] in ".?!" or word[len(word)-2] in ".?!" and word.endswith('"'):
        stop_words.append(word)


# TODO: construct 5 random sentences

def construct(cache):
    sentence = [random.choice(start_words)]               

    if sentence[0] in stop_words:
        return sentence
    
    while sentence[len(sentence)-1] not in stop_words:                  
        next_word = random.choice(cache[sentence[len(sentence)-1]])
        sentence.append(next_word)
        result = " ".join(sentence)
        
    return result

print("1: ", construct(cache))
print("2: ", construct(cache))
print("3: ", construct(cache))
print("4: ", construct(cache))
print("5: ", construct(cache))