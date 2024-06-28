import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import numpy as np
import os
import urllib.request
import gensim.downloader as api
from sentence_transformers import SentenceTransformer

# Step 1: Load the Jester dataset
file_path = 'jester-data-1.xls'
jester_data = pd.read_excel(file_path)


print(jester_data.head())

# Function to extract labels
def extract_labels(data):
    labels = data.iloc[:, 1]  
    return labels

# Step 2: Load the pre-trained FastText model using gensim
fasttext_model = api.load('fasttext-wiki-news-subwords-300')

def extract_fasttext_embeddings(texts):
    embeddings = np.array([np.mean([fasttext_model[word] for word in text.split() if word in fasttext_model], axis=0) for text in texts])
    return embeddings

# Step 3: Extract BERT Embeddings
bert_model = SentenceTransformer('bert-base-cased')

def extract_bert_embeddings(texts):
    embeddings = bert_model.encode(texts)
    return embeddings


texts_list = jester_data.iloc[:, 0].astype(str).tolist() 
fasttext_embeddings = extract_fasttext_embeddings(texts_list)
bert_embeddings = extract_bert_embeddings(texts_list)

# Combine FastText and BERT embeddings
features = np.hstack((fasttext_embeddings, bert_embeddings))
labels = extract_labels(jester_data)

# Step 4: Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(features, labels, test_size=0.2, random_state=42)

# Verify the shapes of the splits
print(f'X_train shape: {X_train.shape}')
print(f'X_val shape: {X_val.shape}')
print(f'y_train shape: {y_train.shape}')
print(f'y_val shape: {y_val.shape}')

# Step 5: Train a Basic MLP Model
mlp = MLPRegressor(solver='sgd', alpha=0.0, learning_rate='constant', random_state=42)
mlp.fit(X_train, y_train)

# Plot the training loss curve
plt.plot(mlp.loss_curve_)
plt.title('MLP Training Loss Curve')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()

# Step 6: Experiment with Learning Rates
learning_rates = [0.001, 0.01, 0.1]
for lr in learning_rates:
    mlp = MLPRegressor(solver='sgd', alpha=0.0, learning_rate_init=lr, random_state=42)
    mlp.fit(X_train, y_train)
    plt.plot(mlp.loss_curve_, label=f'LR={lr}')

plt.title('MLP Training Loss Curve for Different Learning Rates')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Step 7: Experiment with Model Sizes
neuron_counts = [10, 50, 100]
for count in neuron_counts:
    mlp = MLPRegressor(hidden_layer_sizes=(count,), solver='sgd', alpha=0.0, learning_rate='constant', random_state=42)
    mlp.fit(X_train, y_train)
    plt.plot(mlp.loss_curve_, label=f'Neurons={count}')

plt.title('MLP Training Loss Curve for Different Model Sizes')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Step 8: Evaluate the Best Model

best_mlp = MLPRegressor(hidden_layer_sizes=(50,), solver='sgd', alpha=0.0, learning_rate_init=0.01, random_state=42)
best_mlp.fit(X_train, y_train)


new_joke = "Why don't scientists trust atoms? Because they make up everything!"
new_joke_fasttext = extract_fasttext_embeddings([new_joke])
new_joke_bert = extract_bert_embeddings([new_joke])
new_joke_features = np.hstack((new_joke_fasttext, new_joke_bert))

# Predict the funniness score
predicted_score = best_mlp.predict(new_joke_features)
print(f'Predicted funniness score: {predicted_score}')

# Step 9: Optional Parameter Investigation (Regularization)
alphas = [0.0001, 0.001, 0.01]
for alpha in alphas:
    mlp = MLPRegressor(solver='sgd', alpha=alpha, learning_rate='constant', random_state=42)
    mlp.fit(X_train, y_train)
    plt.plot(mlp.loss_curve_, label=f'Alpha={alpha}')

plt.title('MLP Training Loss Curve for Different Regularization Parameters')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
