import streamlit as st

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

from pickle import dump, load
#
# classifier_loc = "pickle/logit_model.pkl"
# encoder_loc = "pickle/countvectorizer.pkl"
# image_loc = "img/twitter_img.jpg"


def preprocess(tweet):
    # Removing special characters and digits
    letters_only = re.sub("[^a-zA-Z]", " ",tweet)

    # change sentence to lower case
    letters_only = letters_only.lower()

    # tokenize into words
    words = letters_only.split()

    # remove stop words
    words = [w for w in words if not w in stopwords.words("english")]

    # Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    clean_sentence = " ".join(words)

    return clean_sentence



def predict(tweet):

    # Loading pretrained CountVectorizer from pickle file
    vectorizer = load(open('pickle/countvectorizer.pkl', 'rb'))

    # Loading pretrained logistic classifier from pickle file
    classifier = load(open('pickle/logit_model.pkl', 'rb'))

    # Preprocessing the tweet
    clean_tweet = preprocess(tweet)

    # Converting text to numerical vector
    clean_tweet_encoded = vectorizer.transform([clean_tweet])

    # Converting sparse matrix to dense matrix
    tweet_input = clean_tweet_encoded.toarray()

    # Prediction
    prediction = classifier.predict(tweet_input)

    return prediction



def main():

    st.image("img/twitter_img.jpg", use_column_width = True)

    tweet = st.text_input('Enter your tweet')

    prediction = predict(tweet)

    if(tweet):
        st.subheader("Prediction:")
        if(prediction == 0):
            st.write("Negative Tweet :cry:")
        else:
            st.write("Positive Tweet :sunglasses:")



if(__name__ == '__main__'):
    main()
