from dateutil import parser

def process_reviews(reviews):
    """Clean and standardize review data."""
    for review in reviews:
        # Remove extra whitespace from review text
        review['review_text'] = ' '.join(review['review_text'].split())
        # Convert review_date to ISO format
        try:
            review['review_date'] = parser.parse(review['review_date']).isoformat()
        except (ValueError, TypeError):
            review['review_date'] = None  # Handle unparsable dates
    return reviews