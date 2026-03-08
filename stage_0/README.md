# Stage 0: Basic Text Vectorization Methods

This directory (`stage_0`) contains basic implementations of fundamental Natural Language Processing (NLP) text vectorization techniques from scratch.

> **Note**: The code in this directory may not be highly optimized. It was written primarily for learning and understanding the basic concepts of text representation in LLMs and NLP.

## Files and Implementations

### 1. `bag_of_words.py`
This script implements a basic **Bag of Words (BoW)** model. 
- **`vocabulary_update`**: Iterates through the corpus to extract a unique list of lowercased words, acting as our vocabulary.
- **`bow`**: Generates a binary vector representation for a given sentence. It checks if each word in the vocabulary is present in the sentence (assigns `1`) or not (assigns `0`).

### 2. `term_frequency.py`
This script expands on the binary BoW concept by implementing raw **Term Frequency (TF)**.
- **`vocabulary_update`**: Same as in the BoW script.
- **`tf`**: Instead of a simple binary presence indicator, this function calculates the actual frequency of each vocabulary word in the given sentence. This provides a vector where each element represents the count of a specific word.

### 3. `tf-idf.py`
This script introduces **Term Frequency-Inverse Document Frequency (TF-IDF)** to penalize globally common words and highlight rare, informative words.
- **`idf`**: Calculates the Inverse Document Frequency for each word based on its occurrence across documents in the corpus.
- **`tfidf`**: Multiplies the `tf` and `idf` scores to create TF-IDF vectors for documents.

### 4. `cosine-similarity.py`
This script acts as a basic search engine, utilizing TF-IDF vectors to compare documents mathematically via **Cosine Similarity**.
- Calculates the TF-IDF vector for a user query.
- Uses `cosine_similarity()` (dot product / product of magnitudes) to calculate the similarity scores between the query and the documents in the corpus.
