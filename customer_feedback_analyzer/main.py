import argparse
from urllib.parse import urlparse
import scraper
import processor
import analyzer
import database
import visualizer
import sqlite3

def main():
    parser = argparse.ArgumentParser(description='Customer Feedback Analyzer')
    subparsers = parser.add_subparsers(dest='mode', required=True)

    # Scrape mode
    scrape_parser = subparsers.add_parser('scrape', help='Scrape and store reviews')
    scrape_parser.add_argument('--urls', nargs='+', required=True, help='List of review page URLs')

    # Visualize mode
    subparsers.add_parser('visualize', help='Generate visualizations from stored data')

    args = parser.parse_args()

    if args.mode == 'scrape':
        database.create_table()
        for url in args.urls:
            domain = urlparse(url).netloc
            if 'yelp.com' in domain:
                reviews = scraper.scrape_yelp(url)
            elif 'google.com' in domain:
                reviews = scraper.scrape_google(url)
            else:
                print(f"Unsupported platform for {url}")
                continue

            processed_reviews = processor.process_reviews(reviews)
            for review in processed_reviews:
                review['sentiment'] = analyzer.analyze_sentiment(review['review_text'])
                database.insert_review(review)
            print(f"Processed and stored {len(reviews)} reviews from {url}")

    elif args.mode == 'visualize':
        conn = sqlite3.connect('reviews.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT business_name FROM reviews")
        business_names = [row[0] for row in c.fetchall()]
        conn.close()
        for business_name in business_names:
            visualizer.generate_plots(business_name)
            print(f"Generated plots for {business_name}")

if __name__ == '__main__':
    main()