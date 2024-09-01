from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()
words=['rain','raining','faith','faithful','are','is','care','caring']
for word in words:
  print(word+'->'+ stemmer.stem(word))