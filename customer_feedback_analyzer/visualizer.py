import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sqlite3
import os

def get_reviews(business_name):
    """Retrieve reviews for a business from the database."""
    conn = sqlite3.connect('reviews.db')
    query = "SELECT * FROM reviews WHERE business_name = ?"
    df = pd.read_sql_query(query, conn, params=(business_name,))
    conn.close()
    return df

def plot_sentiment_distribution(df, business_name):
    """Plot bar chart of sentiment distribution."""
    sentiment_counts = df['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
    plt.title(f'Sentiment Distribution for {business_name}')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.savefig(f'plots/sentiment_distribution_{sanitize_filename(business_name)}.png')
    plt.close()

def plot_sentiment_trend(df, business_name):
    """Plot line chart of sentiment trend over time."""
    df['review_date'] = pd.to_datetime(df['review_date'])
    df = df.sort_values('review_date')
    df['polarity'] = df['review_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df.groupby('review_date')['polarity'].mean().plot()
    plt.title(f'Sentiment Trend for {business_name}')
    plt.xlabel('Date')
    plt.ylabel('Average Polarity')
    plt.savefig(f'plots/sentiment_trend_{sanitize_filename(business_name)}.png')
    plt.close()

def generate_wordcloud(df, sentiment='negative', business_name=''):
    """Generate word cloud for reviews of a specific sentiment."""
    text = ' '.join(df[df['sentiment'] == sentiment]['review_text'])
    if text:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud for {sentiment.capitalize()} Reviews - {business_name}')
        plt.savefig(f'plots/wordcloud_{sentiment}_{sanitize_filename(business_name)}.png')
        plt.close()

def generate_plots(business_name):
    """Generate all plots for a business."""
    if not os.path.exists('plots'):
        os.makedirs('plots')
    df = get_reviews(business_name)
    if not df.empty:
        plot_sentiment_distribution(df, business_name)
        plot_sentiment_trend(df, business_name)
        generate_wordcloud(df, 'negative', business_name)

def sanitize_filename(name):
    """Sanitize business name for use in filenames."""
    return ''.join(c for c in name if c.isalnum() or c in ' _-').strip()