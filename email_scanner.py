import pandas as pd
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split



class EmailScanner:
    def __init__(self, dataset_path) # add path to dataset
        self.dataset = pd.read_csv(dataset_path)
        self.preprocess_dataset()
        self.train_model()    

    def preprocess_dataset(self):


    def train_model(self):


    