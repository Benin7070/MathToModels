
#data
sentences = [
 "I love AI AI",
 "AI loves math",
 "I love math"
]



#vocabulary_list_updation
def vocabulary_update(sentences):
    vocabulary_list={}
    for i in sentences:
        words=[i.lower() for i in i.split()]
        for word in words:
            if word not in vocabulary_list:
                vocabulary_list[word]=0

    return vocabulary_list

    
#term frequency
def tf(words,vocabulary_list):
    voc_len=len(vocabulary_list)
    token_dict=vocabulary_list.copy()
    for word in words:
        token_dict[word]+=1
    return list(token_dict.values())



vocab=vocabulary_update(sentences)
print(vocab)
for i in sentences:
    words=[i.lower() for i in i.split()]
    print(tf(words,vocab))

