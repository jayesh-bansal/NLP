from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
 
#read's the text from file
file=open("NLP.txt")
print(text) 

#Sentence Tokenization
text=file.read()
Paragraph_sentence=sent_tokenize(text)
#Print paragraph into sentences. means divide para into sentences 
print(sentence)

#Print Para into Words
Paragaph_word=word_tokenize(text)
print(word)
print(len(word))

#Mostly used Common Words in the Para.
graph=FreqDist(Paragaph_word)
#number indcates no of first occurenece you want to print
print(graph.most_common(10))


#Prints the plot graph for number of (give number in brackets)
common_words.plot(10)


#To remove Punctuation from the paragraph
No_punctuations=[]
for i in Paragaph_word:
    if i.isalpha():
        No_punctuations.append(i.lower())
print(No_punctuations)

#Ploting graph Without Punctuations.
graph=FreqDist(No_punctuations)
print(graph.most_common(10))
graph.plot(10)


stopwords=stopwords.words('english')
print(stopwords)


#Printing Words Without the Stopwords
clean_Words=[]
for i in No_punctuations:
    if i not in stopwords:
        clean_Words.append(i)
print(clean_Words)

graph=FreqDist(clean_Words)
print(graph.most_common(10))
graph.plot(10)
 
