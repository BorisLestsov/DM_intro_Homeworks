import numpy as np
import math
import string as s

docs = []
docs.append("John likes to watch movies.")
docs.append("Mary likes movies too.")
docs.append("John also likes football.")

def TF_IDF(docs, stopwords = []):
    sym_from = ',.!@#$%^&*()-_=+/*<>,;:[]\{\}\\:\"~\''
    sym_to = ' ' * len(sym_from) 
    trans_table = s.maketrans(sym_from, sym_to)
    
    words_in_docs = [doc.translate(trans_table).split() for doc in docs]
    
    def word_tf(word, doc_words):
        return float(doc_words.count(word)) / len(doc_words)
        
    def word_idf(word, words_in_docs):
        counter = 0
        for doc_words in words_in_docs:
            if word in doc_words:
                counter += 1
        return  math.log10(len(words_in_docs) / float(counter))
    
    
    all_words = set()
    
    for words in words_in_docs:
        for word in words:
            if not word in stopwords:
                all_words.add(word)
    
    m = np.zeros([len(all_words), len(docs)])
    
    for i, word in enumerate(sorted(all_words)):
        for j, words_in_doc in enumerate(words_in_docs):
            m[i, j] = word_tf(word, words_in_doc) * word_idf(word, words_in_docs)
        
    return m

m = TF_IDF(docs, 'to')

print 'docs:'
for doc in docs:
	print doc

np.set_printoptions(formatter={'float': '{: 0.4f}'.format})
print m