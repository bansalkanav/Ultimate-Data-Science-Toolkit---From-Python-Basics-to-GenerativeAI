import numpy as np
import pandas as pd

import nltk

from wordcloud import WordCloud,STOPWORDS


dataset_loc = "data/Tweets.csv"

# WordCloud
def load_wordcloud(df, kind):
    temp_df = df.loc[df['airline_sentiment']==kind, :]
    words = ' '.join(temp_df['text'])
    cleaned_word = " ".join([word for word in words.split() if 'http' not in word and not word.startswith('@') and word != 'RT'])
    wc = WordCloud(stopwords=STOPWORDS, background_color='black', width=1600, height=800).generate(cleaned_word)
    return wc


def main():
    nltk.download('stopwords')

    df = pd.read_csv(dataset_loc)
    wc = load_wordcloud(df, "positive")
    wc.to_file("img/pos.png")

    wc = load_wordcloud(df, "negative")
    wc.to_file("img/neg.png")


if(__name__=="__main__"):
    main()
