import re
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score
# Class 1: 
doc1 = "The gold medal price is high effort"
doc2 = "Winning a gold medal needs a high jump"
doc3 = "Market for a gold medal is a trade of sweat"
doc4 = "The athlete will trade all for a gold medal"

# Class 2: 
doc5 = "The gold bars price is high today"
doc6 = "Investing in gold bars needs a high rate"
doc7 = "Market for gold bars is a trade of money"
doc8 = "The bank will trade all for gold bars"

# task1

def processingThetext(text):
    
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    return tokens
#n-gram extraction and vectorization
def ngram_vectorise(doc, n_gram_size):
    
    processed_doc = []
    for doc in doc:
        tokens = processingThetext(doc)
            # extract n-grams
        ngrams = []
        for i in range(len(tokens) - n_gram_size + 1):
            gram = " ".join(tokens[i:i+n_gram_size])
            ngrams.append(gram)
        processed_doc.append(ngrams)

    # build vocab
    vocab = sorted(set(g for doc in processed_doc for g in doc))
    vocab_index = {word:i for i,word in enumerate(vocab)}

    # vectorization
    vectors = []
    for doc in processed_doc:
        vec = [0]*len(vocab)

        for word in doc:
            vec[vocab_index[word]] += 1

        vectors.append(vec)

    return np.array(vectors)

# Run
all_doc = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]

# 1-gram Experiment
d1 = ngram_vectorise(all_doc, n_gram_size=1)
km1 = KMeans(n_clusters=2, random_state=42).fit(d1)

# 2-gram Experiment
d2 = ngram_vectorise(all_doc, n_gram_size=2)
km2 = KMeans(n_clusters=2, random_state=42).fit(d2)

print(f"1-gram clusters: {km1.labels_}")
print(f"2-gram clusters: {km2.labels_}")
# compare accuracy and precision
true_labels = [0, 0, 0, 0, 1, 1, 1, 1]

labels1, labels2 = km1.labels_, km2.labels_

acc1, acc2 = accuracy_score(true_labels, labels1), accuracy_score(true_labels, labels2)
prec1, prec2 = precision_score(true_labels, labels1), precision_score(true_labels, labels2)

print("\n compare accuracy and precision")
print(f"1-gram = Accuracy: {acc1:.2f}, Precision: {prec1:.2f}")
print(f"2-gram = Accuracy: {acc2:.2f}, Precision: {prec2:.2f}")

msg = ("2-gram performs better." if acc2 > acc1
       else "1-gram performs better." if acc1 > acc2
       else "Both models have similar performance.")
print(msg)
#task2 
# Documents
D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"
# Preprocessing (without padding, the first and last words lose context)
def add_padding(tokens):
    return ["<s>"] + tokens + ["</s>"]

# Extract windows of size 3 (1 word on each side)
def extract_windows(tokens, window_size=1):
    windows = []
    i = window_size
    while i < len(tokens) - window_size:
        windows.append(" ".join(tokens[i - window_size:i + window_size + 1]))
        i += 1
    return windows

def build_vocab(all_windows):
    vocab = sorted(set(all_windows))
    return vocab, {w: i for i, w in enumerate(vocab)}

def vectorize_doc(doc_windows, vocab_index):
    vector = [0] * len(vocab_index)
    i = 0
    while i < len(doc_windows):
        if doc_windows[i] in vocab_index:
            vector[vocab_index[doc_windows[i]]] = 1
        i += 1
    return vector

# Run
all_windows = []
doc_windows = []
i = 0
all_docs = [D1, D2, D3]

while i < len(all_docs):
    tokens = extract_windows(add_padding(processingThetext(all_docs[i])), 1)
    doc_windows.append(tokens)
    all_windows.extend(tokens)
    i += 1

vocab, vocab_index = build_vocab(all_windows)

print("\nVocabulary:")
print(vocab)
print("\nVectors:")

i = 0
while i < len(doc_windows):
    print(f"D{i+1}:", vectorize_doc(doc_windows[i], vocab_index))
    i += 1