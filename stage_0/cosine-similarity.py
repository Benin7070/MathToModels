import math
#data
data = [
 "I love AI AI",
 "AI loves math",
 "I love math"
]

N_vocab={}
dataset_vectors=[]

#vocabulary_list_updation
def vocabulary_update(sentences):
    vocabulary_list={}
    for i in sentences:
        words=[j.lower() for j in i.split()]
        # Count Document Frequency (df): only count a word once per document
        unique_words_in_doc = set(words)
        for word in unique_words_in_doc:
            try:
                N_vocab[word]+=1
            except KeyError:
                N_vocab[word]=1
                
        for word in words:
            vocabulary_list[word]=0
    return vocabulary_list

#term frequency
def tf(words,vocabulary_list):
    voc_len=len(vocabulary_list)
    token_dict=vocabulary_list.copy()
    for word in words:
        if word in token_dict:
            token_dict[word]+=1
    return token_dict

#inverse document frequency
def idf(vocabulary_list, total_documents):
    idf_dict = vocabulary_list.copy()
    for word in idf_dict:
        if word in N_vocab and N_vocab[word] > 0:
            idf_dict[word] = math.log10(total_documents / N_vocab[word])
        else:
            idf_dict[word] = 0.0
    return idf_dict

#tf-idf
def tfidf(tf_dict, idf_dict):
    tfidf_dict = tf_dict.copy()
    for word in tfidf_dict:
        tfidf_dict[word] = round(tf_dict[word] * idf_dict[word], 4)
    return list(tfidf_dict.values())

#cosine similarity
def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude1 = math.sqrt(sum(a * a for a in v1))
    magnitude2 = math.sqrt(sum(b * b for b in v2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

print("welcome to the similarity checking system")
vocab=vocabulary_update(data)
total_docs = len(data)
# Calculate IDF once for the entire vocabulary based on the dataset
global_idf = idf(vocab, total_docs)

for i in data:
    words=[word.lower() for word in i.split()]
    term_frequency=tf(words,vocab)
    vector_data=tfidf(term_frequency, global_idf)
    dataset_vectors.append(vector_data)
    print(f"Document vector for '{i}': {vector_data}")
print("vocabulary updated")

query=input("Enter the query:")    

query_words = [q.lower() for q in query.split()]
query_tf = tf(query_words, vocab)
query_vector = tfidf(query_tf, global_idf)

print("Query vector:", query_vector)
print("\nCosine Similarities:")
for idx, doc_vector in enumerate(dataset_vectors):
    sim = cosine_similarity(query_vector, doc_vector)
    print(f'Document {idx+1} ("{data[idx]}"): {sim:.4f}')
