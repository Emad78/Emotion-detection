import numpy as np
import pandas as pd
import pickle
import fasttext
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,  accuracy_score
from dadmatools.embeddings import get_embedding, get_all_embeddings_info, get_embedding_info
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

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

