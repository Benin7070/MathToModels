
#data
sentences = [
 "I love AI Ai",
 "AI loves math",
 "I love math"
]



#bag_of_words
def vocabulary_update(sentences):
    vocabulary_list=[]
    for i in sentences:
        words=[i.lower() for i in i.split()]
        for word in words:
            if word not in vocabulary_list:
                vocabulary_list.append(word)

    return vocabulary_list

    
#bag of words
def bow(words,vocabulary_list):
    voc_len=len(vocabulary_list)
    token=[0]*voc_len
    for i in range(voc_len):
        if vocabulary_list[i] in words:
            token[i]=1
    return token



vocab=vocabulary_update(sentences)
print(vocab)
for i in sentences:
    words=[i.lower() for i in i.split()]
    print(bow(words,vocab))

