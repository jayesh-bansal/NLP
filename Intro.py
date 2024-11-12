import nltk
sentence = ''' today's lab is Natural Language Processing and this ia test case''' #Example sentence
ans=nltk.word_tokenize(sentence)
print(ans)
tag=nltk.pos_tag(ans)
print(tag[0:6])
entities = nltk.chunk.ne_chunk(tag)
print(entities)
