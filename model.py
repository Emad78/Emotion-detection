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


def NN_prepare_data(train, temp):
  enc = LabelBinarizer()
  test, valid = train_test_split(temp, test_size=0.5)

  x_train = np.array(train['text'].apply(fast_text0.get_sentence_vector))
  x_test = np.array(test['text'].apply(fast_text0.get_sentence_vector))
  x_val = np.array(valid['text'].apply(fast_text0.get_sentence_vector))

  x_train1 = np.array(train['text'].apply(fast_text1.embedding_text))
  x_test1 = np.array(test['text'].apply(fast_text1.embedding_text))
  x_val1 = np.array(valid['text'].apply(fast_text1.embedding_text))

  for i in range(len(x_train)):
    x_train[i] = np.concatenate((x_train[i], x_train1[i]), axis=0)

  for i in range(len(x_test)):
    x_test[i] = np.concatenate((x_test[i], x_test1[i]), axis=0)

  for i in range(len(x_val)):
    x_val[i] = np.concatenate((x_val[i], x_val1[i]), axis=0)


  enc.fit(train['label'])
  y_train = enc.transform(train['label'])
  y_test = enc.transform(test['label'])
  y_val = enc.transform(valid['label'])

  return x_train, y_train, x_test, y_test, x_val, y_val, enc

def create_model(input_size, output_size):
  model = Sequential()
  model.add(Input(input_size))
  model.add(Dense(10, activation='relu'))
  model.add(Dense(output_size, activation='softmax'))
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
  return model

data = pd.read_csv("drive/MyDrive/Work/CleanData_arman.csv")
data = data[['text', 'label']]

train, test = train_test_split(data, test_size=0.3)
train.reset_index(drop=True, inplace=True)
test.reset_index(drop=True, inplace=True)

#train = train[train.label != 'OTHER']
#test = test[test.label != 'OTHER']

try : 
    fast_text0 = fasttext.load_model('resources/embedding/fast_test0.model')
except:
    text = ''
    for i in range(len(train)):
        text += train.loc[i, 'text'] + " __label__"+train.loc[i, 'label'] + "\n"

    with open("train_fasttext.txt", 'w', encoding='UTF-8') as file:
        file.write(text)
    fast_text0 = fasttext.FastText.train_supervised("train_fasttext.txt", lr=0.5, epoch=25, wordNgrams=3, bucket=200000, dim=100, loss='ova')
    fast_text0.save_model("resources/embedding/fast_text0.model")

try : 
    fast_text1 = fasttext.load_model('resources/embedding/fast_test1.model')
except:
    fast_text1 = get_embedding('fasttext-commoncrawl-bin')
    fast_text1.model.save_model('resources/embedding/fast_text1.model')

