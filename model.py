import numpy as np
import pandas as pd
import pickle
import fasttext

from tensorflow.keras import preprocessing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, GRU, Bidirectional, Input, Embedding, Flatten, SimpleRNN
from tensorflow.keras.optimizers import SGD
from tensorflow import stack
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,  accuracy_score
from dadmatools.embeddings import get_embedding, get_all_embeddings_info, get_embedding_info
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier