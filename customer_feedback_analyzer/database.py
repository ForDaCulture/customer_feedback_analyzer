import sqlite3

def create_table():
    """Create the reviews table if it doesn’t exist."""
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  business_name TEXT,
                  platform TEXT,
                  review_text TEXT,
                  rating REAL,
                  review_date TEXT,
                  sentiment TEXT)''')
    conn.commit()
    conn.close()

def insert_review(review):
    """Insert a review into the database."""
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''INSERT INTO reviews (business_name, platform, review_text, rating, review_date, sentiment)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (review['business_name'], review['platform'], review['review_text'],
               review['rating'], review['review_date'], review['sentiment']))
    conn.commit()
    conn.close()