tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
for token2 in tokens:
print(token1.text, token2.text, token1.similarity(token2))


"""
After running the code, I found that the similarity between "cat" and "monkey" is higher than the similarity between "cat" and "banana". This is interesting because both cats and monkeys are animals, while bananas are not. However, the word "monkey" shares some letters with the word "donkey", which is another animal, so it is possible that this could contribute to the higher similarity score.

As for my own example, I decided to compare the similarity between different programming languages. When I ran the code with the input "Python Java C++ JavaScript", I found that the similarity scores between each pair of languages were relatively high, with the highest score being between "Python" and "JavaScript". This could be because both languages are commonly used for web development and have similar syntax.

When I ran the code with the simpler language model 'en_core_web_sm', I noticed that the similarity scores were generally lower than with the larger model 'en_core_web_md'. This is likely because the smaller model has a more limited vocabulary and may not be able to capture the nuances of language as well as the larger model. However, the relative similarities between the words were still consistent with the larger model, which is promising.

"""