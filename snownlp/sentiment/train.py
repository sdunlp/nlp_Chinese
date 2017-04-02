from snownlp import sentiment
sentiment.train('neg.txt', 'pos_word.txt')
sentiment.save('sentiment2.marshal')