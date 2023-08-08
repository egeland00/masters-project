import pandas as pd
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')



class EmailScanner:
    class EmailScanner:
        def __init__(self, dataset_path): # add path to dataset
            self.dataset = pd.read_csv(dataset_path)
            self.preprocess_dataset()
            self.train_model()    

        def preprocess_dataset(self):
            # add code to preprocess dataset
            pass

        def train_model(self):
            # initialise a CountVectorizer. this will convert text into a vectors using the bag-og-word method.
            self.vectorizer = CountVectorizer()
            # Fit the vectorizer to the 'Message' column in the dataset. This will create a vocabulary of words.
            x = self.vectorizer.fit_transform(self.dataset['Message'])
            # Extracting the #Catergoy# colum from the dateset as the target variable.
            y = self.dataset['Category']

            # Split the dataset into training and testing sets.
            self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=0)
        
            # Printing label distribution in the training set.
            print("Label distribution in training set: ")
            print(self.y_train.value_counts()) #(pandas library)

            # Printing the metrics of the traning model. y_pred predicts the labels of the test set. (pandas library)
            y_pred = self.model.predict(self.x_test)
            
            # Prints a report showing the main classification metrics for each label (spam and ham).
            print("Classification report: ")
            print(classification_report(self.y.test, y_pred, target_names=['spam', 'ham']))
            # Prints the confusion matrix (true positives, false positives, true negatives, false negatives)
            print("Confusion matrix: ")
            print(confusion_matrix(self.y_test, y_pred))

            # Calculate and print precision, recall, and F1 score. Using the 'spam' label as the positive label.
            print("Precision:", precision_score(self.y_test, y_pred, pos_label='spam'))
            print("Recall:", recall_score(self.y_test, y_pred, pos_label='spam'))
            print("F1 Score:", f1_score(self.y_test, y_pred, pos_label='spam'))

        