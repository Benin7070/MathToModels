import math
#data
data = [
 "I love AI AI",
 "AI loves math",
 "I love math"
]


N_vocab={}

#vocabulary_list_updation
def vocabulary_update(sentences):
    vocabulary_list={}
    for i in sentences:
        words=[j.lower() for j in i.split()]
        for word in words:
            vocabulary_list[word]=0
            try:
                N_vocab[word]+=1
            except KeyError:
                N_vocab[word]=1
    return vocabulary_list

    
#term frequency
def tf(words,vocabulary_list):
    voc_len=len(vocabulary_list)
    token_dict=vocabulary_list.copy()
    for word in words:
        token_dict[word]+=1
    return token_dict


def idf(token_dict):
    idf_dict = token_dict.copy()
    for i in idf_dict:
        if idf_dict[i] != 0:
            idf_dict[i] = math.log10(N_vocab[i] / idf_dict[i])
    return idf_dict

def tfidf(N_t,t_dict):
    tfidf_dict = t_dict.copy()
    for i in tfidf_dict:
        tfidf_dict[i] = round(tfidf_dict[i] * N_t[i], 2)
    return list(tfidf_dict.values())

vocab=vocabulary_update(data)
for i in data:
    words=[i.lower() for i in i.split()]
    term_frequency=tf(words,vocab)
    inverse_document_frequceny=idf(term_frequency)
    print(tfidf(term_frequency,inverse_document_frequceny))
    

