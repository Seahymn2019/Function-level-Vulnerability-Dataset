# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:38:06 2019

@author: Seahymn, Daniel Lin
    
Train a Word2vec model on the code base (unsupervised).
    
"""

import argparse
import os
import pickle
from gensim.models import Word2Vec
from keras.preprocessing.text import Tokenizer

from src.DataLoader import getCFilesFromText

# Arguments
parser = argparse.ArgumentParser(description='Train a Word2vec model on the code base.')
parser.add_argument('--data_dir', default='data/', type=str, help='The path of the code base for training.')
parser.add_argument('--output_dir', default='result/', type=str, help='The output path of the trained Word2vec model.')
parser.add_argument('--n_workers', default=4, type=int, help='Number of threads for training.', required=False)
parser.add_argument('--size', default=100, type=int, help='Dimensionality of the word vectors. This is the Embedding dimension.', required=False)
parser.add_argument('--window', default=5, type=int, help='Maximum distance between the current and predicted word within a sentence.', required=False)
parser.add_argument('--min_count', default=5, type=int, help='Ignores all words with total frequency lower than this.', required=False)
parser.add_argument('--algorithm', default=0, type=int, help='Training algorithm: 1 for skip-gram; otherwise CBOW.', required=False)
parser.add_argument('--seed', default=1, type=int, help='Seed for the random number generator.', required=False)
paras = parser.parse_args()

total_list, total_list_id = getCFilesFromText(paras.data_dir)
print ("The length of the list is : " + str(len(total_list)))

#--------------------------------------------------------#
# 1. Tokenization: convert the loaded text

tokenizer = Tokenizer(num_words=None, filters=',', lower=False, char_level=False, oov_token=None) 
tokenizer.fit_on_texts(total_list)

# Save the tokenizer.
with open(paras.output_dir + 'tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle)
    
# ----------------------------------------------------- #
# 2. Train a Vocabulary with Word2Vec -- using the function provided by gensim
w2vModel = Word2Vec(total_list, workers = paras.n_workers, size = paras.size, window = paras.window, min_count = paras.min_count, sg = paras.algorithm, seed = paras.seed)

print ("----------------------------------------")
print ("The trained word2vec model: ")
print (w2vModel)

w2vModel.wv.save_word2vec_format(paras.output_dir + "w2v_model_CBOW_dict.txt", binary=False)