import pandas as pd
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
from bs4 import BeautifulSoup
import string
from typing import List, Dict, Union, Any

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
dataset_path = '/home/orjan/Documents/GitHub/masters-project/dataset.csv'
class EmailScanner:


        def __init__(self, dataset_path): # add path to dataset
            self.dataset = pd.read_csv(dataset_path)
            print(self.dataset.head()) # added to test to see if the dataset is loaded correctly
            self.stop_words = nltk.corpus.stopwords.words('english')
            self.preprocess_dataset()
            self.train_model()
    

        def preprocess_dataset(self):

            # Convert to lowercase
            self.dataset['Message'] = self.dataset['Message'].str.lower()

            # Tokenize
            self.dataset['Message'] = self.dataset['Message'].apply(nltk.word_tokenize)

            # Remove URLs and email addresses
            self.dataset['Message'] = self.dataset['Message'].apply(lambda x: ['URL' if word.startswith(('http://', 'https://', 'www.')) else word for word in x])
            self.dataset['Message'] = self.dataset['Message'].apply(lambda x: ['EMAILADDRESS' if '@' in word else word for word in x])

            # Remove stopwords and punctuation
            self.dataset['Message'] = self.dataset['Message'].apply(lambda x: [word for word in x if word not in self.stop_words and word not in string.punctuation])


            # Joining the tokens back to a string
            self.dataset['Message'] = self.dataset['Message'].apply(lambda x: ' '.join(x))

        

        def train_model(self):
            # initialise a CountVectorizer. this will convert text into a vectors using the bag-og-word method.
            self.vectorizer = CountVectorizer()
            # Fit the vectorizer to the 'Message' column in the dataset. This will create a vocabulary of words.
            x = self.vectorizer.fit_transform(self.dataset['Message'])
            # Extracting the #Catergoy# colum from the dateset as the target variable.
            y = self.dataset['Category']

            # Sample to demonstrate the vectorizer
            sample_message = self.dataset['Message'][0]
            vectorized_sample = self.vectorizer.transform([sample_message])

            # Print the vectorized sample
            print("\nEffect of Vectorization:")
            print(f"Original Message: {sample_message}")
            print(f"Vectorized Representation: {vectorized_sample.toarray()}\n")

            # Print the vocabulary
            print("Vocabulary:" , self.vectorizer.vocabulary_)


            # Split the dataset into training and testing sets.
            self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=0)
            self.model = MultinomialNB()
            self.model.fit(self.x_train, self.y_train)

            # Printing label distribution in the training set.
            print("Label distribution in training set: ")
            print(self.y_train.value_counts()) #(pandas library)

            # Printing the metrics of the traning model. y_pred predicts the labels of the test set. (pandas library)
            y_pred = self.model.predict(self.x_test)
            
            # Prints a report showing the main classification metrics for each label (spam and ham).
            print("Classification report: ")
            print(classification_report(self.y_test, y_pred, target_names=['spam', 'ham']))
            # Prints the confusion matrix (true positives, false positives, true negatives, false negatives)
            print("Confusion matrix: ")
            print(confusion_matrix(self.y_test, y_pred))

            # Calculate and print precision, recall, and F1 score. Using the 'spam' label as the positive label.
            print("Precision:", precision_score(self.y_test, y_pred, pos_label='spam'))
            print("Recall:", recall_score(self.y_test, y_pred, pos_label='spam'))
            print("F1 Score:", f1_score(self.y_test, y_pred, pos_label='spam'))


        def preprocess_single_email(self, email: str) -> str:
            # Convert the email to lowercase for consistency
            email = email.lower()

            # Remove any HTML tags that might be present in the email
            email = BeautifulSoup(email, 'lxml').get_text()

            # Tokenize the email into individual words
            tokens = nltk.word_tokenize(email)

            # Replace any URLs in the email with the word 'URL'
            tokens = ['URL' if word.startswith(('http://', 'https://', 'www.')) else word for word in tokens]

            # Replace any email addresses in the email with the word 'EMAILADDRESS'
            tokens = ['EMAILADDRESS' if '@' in word else word for word in tokens]


            # Remove stopwords and punctuation from the tokens
            tokens = [word for word in tokens if word not in self.stop_words and word not in string.punctuation]

            # Join the processed tokens back together into a single string
            return ' '.join(tokens)
        
        def scan(self, email: str) -> bool:
            email = self.preprocess_single_email(email)
            email_vec = self.vectorizer.transform([email])
            prediction = self.model.predict(email_vec)

            # Print the prediction probability
            prediction_prob = self.model.predict_proba(email_vec)
            print(f"Prediction probability for email: {prediction_prob}")

            return prediction[0] == "spam"
        

    # Specify the path to your dataset
#dataset_path = '/home/orjan/Documents/GitHub/masters-project/dataset.csv'

# Create an instance of the EmailScanner class using the path
scanner = EmailScanner(dataset_path)

# Test the function preprocess_single_email. 
#sample_email = scanner.dataset['Message'][100]
#print("Original email: ", sample_email)
#print("\nProcessed Email:", scanner.preprocess_single_email(sample_email))