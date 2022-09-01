word = input('Word = ')
import random
for i in range(5):
    def word_gen(size=len(word), chars=word):
            return ''.join(random.choice(chars) for _ in range(size))
    print(word_gen(), end=' ')
