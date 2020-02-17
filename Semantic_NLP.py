# Author: Raymond Jing
#Date: Feb 15 2020

from __future__ import print_function, division
from future.utils import iteritems
from builtins import range
from sklearn.utils import shuffle
from nltk.stem import WordNetLemmatizer
from sklearn.linear_model import LogisticRegression
from bs4 import BeautifulSoup

import os
import nltk
import numpy as np
import glob 
import matplotlib as plt
import requests
import re
import matplotlib.pyplot as plt
import matplotlib as mpl


wordindex_hash = {}
word_index = 0
positive_reviews_tokenization = []
negative_reviews_tokenization = []
orig_reviews = []
wordnet_lemmatizer = WordNetLemmatizer()
stopwords = set(word.rstrip() for word in open('/Users/ranjing/Desktop/Amazon_reviews/stopwords.txt'))#creat stopword set


positive_reviews = BeautifulSoup(open("/Users/ranjing/Desktop/Amazon_reviews/electronics/positive.review.txt").read(), features="html5lib")
positive_reviews = positive_reviews.findAll('review_text')

negative_reviews = BeautifulSoup(open('/Users/ranjing/Desktop/Amazon_reviews/electronics/negative.review.txt').read(), features="html5lib")
negative_reviews = negative_reviews.findAll('review_text')


# create a word-to-index hashmap to create the word-frequency vectors 

def tokenization(s):
    s = s.lower() 
    tokens = nltk.tokenize.word_tokenize(s) # split string into words (tokens)
    tokens = [i for i in tokens if len(i) > 2] # remove short words, they're probably not useful
    tokens = [wordnet_lemmatizer.lemmatize(i) for i in tokens] # put words into base form
    tokens = [i for i in tokens if i not in stopwords] # delete the stopwords
    return tokens

for review in positive_reviews:
    orig_reviews.append(review.text)
    tokens = tokenization(review.text)
    positive_reviews_tokenization.append(tokens)
    for i in tokens:
        if i not in wordindex_hash:
            wordindex_hash[i] = word_index
            word_index += 1


for review in negative_reviews:
    orig_reviews.append(review.text)
    tokens = tokenization(review.text)
    negative_reviews_tokenization.append(tokens)
    for i in tokens:
        if i not in wordindex_hash:
            wordindex_hash[i] = word_index
            word_index += 1

print("len(wordindex_hash):", len(wordindex_hash))

# setup the input matrices
def tokens_to_vector(tokens, label):
    x = np.zeros(len(wordindex_hash) + 1) 
    for t in tokens:
        i = wordindex_hash[t]
        x[i] += 1
    x = x / x.sum() # normalization
    x[-1] = label
    return x

N = len(positive_reviews_tokenization) + len(negative_reviews_tokenization)
# (N x D+1 matrix - keeping them together for now so we can shuffle more easily later
data = np.zeros((N, len(wordindex_hash) + 1))
i = 0
for tokens in positive_reviews_tokenization:
    xy = tokens_to_vector(tokens, 1)
    data[i,:] = xy
    i += 1

for tokens in negative_reviews_tokenization:
    xy = tokens_to_vector(tokens, 0)
    data[i,:] = xy
    i += 1


# shuffle the data and create training and testing dadaset
# Does the training dataset will affect the results? I will try multiple times by increasing/decreasing the size of the training dataset!
orig_reviews, data = shuffle(orig_reviews, data)

X = data[:,:-1]
Y = data[:,-1]

#checking the size of the input matrix
print(np.size(X))
print(np.size(Y))

# try 1000, 2000, 3000, 4000 rows for the test
#Xtrain = X[:-500,]
#Ytrain = Y[:-500,]
#Xtest = X[-100:,]
#Ytest = Y[-100:,]

#Xtrain = X[:-1000,]
#Ytrain = Y[:-1000,]
#Xtest = X[-100:,]
#Ytest = Y[-100:,]

#Xtrain = X[:-1500,]
#Ytrain = Y[:-1500,]
#Xtest = X[-100:,]
#Ytest = Y[-100:,]

Xtrain = X[:-100,]
Ytrain = Y[:-100,]
Xtest = X[-100:,]
Ytest = Y[-100:,]


model = LogisticRegression()
model.fit(Xtrain, Ytrain)
print("Training data accuracy:", model.score(Xtrain, Ytrain))
print("Classification rate:", model.score(Xtest, Ytest))


# let's look at the weights for each word
# try it with different threshold values!
threshold = 0.5
feature_pos = {}
feature_neg = {}

for word, index in iteritems(wordindex_hash):
    weight = model.coef_[0][index]
    if weight > threshold:
        feature_pos[word] = weight
    
    elif weight < -threshold:
        feature_neg[word] = weight

feature_pos_sort = sorted(feature_pos.items(), key = lambda item:item[1])
feature_neg_sort = sorted(feature_neg.items(), key = lambda item:item[1])

print(feature_pos_sort)       
print(feature_neg_sort)


def draw_bar(labels,quants):
    width = 0.4
    ind = np.linspace(0.5,9.5,10)
    # make a square figure
    fig = plt.figure(1)
    ax  = fig.add_subplot(111)
    
    # Bar Plot
    #ax.bar(ind-width/2, quants,width,color='green')
    ax.bar(ind-width/2, quants,width,color='red')
    
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    
    # labels
    ax.set_xlabel('Word features')
    ax.set_ylabel('Weights for each word')
    
    # title
    #ax.set_title('Top 10 positive word features (Training data size: 100)', bbox={'facecolor':'0.8', 'pad':5})
    ax.set_title('Top 10 negative word features (Training data size: 100)', bbox={'facecolor':'0.8', 'pad':5})
    
    plt.grid(True)
    plt.show()
    plt.savefig("bar.jpg")
    plt.close()

labels   = []
quants   = []
'''
for i in range(0, 10):
    labels.append(feature_pos_sort[i][0])

for i in range(0, 10):
    quants.append(feature_pos_sort[i][1])
'''
for i in range(0, 10):
    labels.append(feature_neg_sort[i][0])

for i in range(0, 10):
    quants.append(feature_neg_sort[i][1])

#print(labels)  
#print(quants) 

draw_bar(labels,quants)


# check misclassified examples
preds = model.predict(X)
P = model.predict_proba(X)[:,1] # p(y = 1 | x)

# since there are many, just print the "most" wrong samples
minP_whenYis1 = 1
maxP_whenYis0 = 0
wrong_positive_review = None
wrong_negative_review = None
wrong_positive_prediction = None
wrong_negative_prediction = None
for i in range(N):
    p = P[i]
    y = Y[i]
    if y == 1 and p < 0.5:
        if p < minP_whenYis1:
            wrong_positive_review = orig_reviews[i]
            wrong_positive_prediction = preds[i]
            minP_whenYis1 = p
    elif y == 0 and p > 0.5:
        if p > maxP_whenYis0:
            wrong_negative_review = orig_reviews[i]
            wrong_negative_prediction = preds[i]
            maxP_whenYis0 = p

print("Most wrong positive review (prob = %s, pred = %s):" % (minP_whenYis1, wrong_positive_prediction))
print(wrong_positive_review)
print("Most wrong negative review (prob = %s, pred = %s):" % (maxP_whenYis0, wrong_negative_prediction))
print(wrong_negative_review)
