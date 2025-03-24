# Customer Feedback Analyzer

A Python tool to scrape customer reviews, analyze sentiment, and visualize insights for business process optimization.

## Overview

This tool demonstrates MIS skills by:
- **Web Scraping:** Collecting reviews from Yelp (extendable to other platforms).
- **Data Processing:** Cleaning and standardizing data.
- **Database Management:** Storing reviews in SQLite.
- **Sentiment Analysis:** Classifying feedback as positive, negative, or neutral.
- **Visualization:** Generating bar charts, trend lines, and word clouds.

It supports business process optimization (e.g., BPM, Balanced Scorecard) by identifying customer satisfaction issues for actionable improvements.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd customer_feedback_analyzer
   Install dependencies:
bash

pip install -r requirements.txt

Ensure Python 3.6+ is installed.

Usage
Scrape Reviews
bash

python main.py scrape --urls https://www.yelp.com/biz/example-business

Scrapes reviews from the provided URLs and stores them in reviews.db.

Generate Visualizations
bash

python main.py visualize

Creates plots for all businesses in the database, saved in the plots/ directory.

Example Output
sentiment_distribution_<business>.png: Bar chart of sentiment counts.

sentiment_trend_<business>.png: Line chart of sentiment over time.

wordcloud_negative_<business>.png: Word cloud of negative review terms.

Business Value
BPM: Identifies process bottlenecks (e.g., slow service) for redesign.

Balanced Scorecard (Customer Perspective): Tracks satisfaction trends.

Porter’s Differentiation: Highlights unique strengths or weaknesses.

For example, a spike in negative reviews about “wait times” suggests staffing optimization, improving efficiency and customer experience.
Technical Notes
Scraping: Uses BeautifulSoup for Yelp; Google Reviews require Selenium or API due to dynamic content.

API Placeholder: In scraper.py, comments indicate where Google Places API or Yelp Fusion API can replace scraping with an API key.

Limitations: Scraping is limited to 3 pages per URL; duplicates may occur without unique review IDs.

Ethics: Includes 1-second delays between requests to respect platform terms.

Future Enhancements
Support for Google Reviews via API or Selenium.

Alerts for sentiment drops.

Web interface with Flask.

License
MIT License

---

### Step 5: Where APIs Are Needed

- **Google Reviews (`scraper.py` - `scrape_google`):**
  - Current implementation is a placeholder because Google Reviews load dynamically via JavaScript. A comment suggests using the **Google Places API** with an API key for reliable data.
  - Example:
    ```python
    # api_key = 'YOUR_API_KEY'
    # place_id = extract_place_id(url)
    # reviews = fetch_reviews_from_google_api(place_id, api_key)
    ```
- **Yelp Alternative (`scraper.py` - `scrape_yelp`):**
  - While scraping works, a comment suggests the **Yelp Fusion API** as a more ethical and robust alternative:
    ```python
    # api_key = 'YOUR_API_KEY'
    # business_id = extract_business_id(url)
    # reviews = fetch_reviews_from_yelp_api(business_id, api_key)
    ```

---

### Step 6: Running the Tool

1. **Scrape Reviews:**
   ```bash
   python main.py scrape --urls https://www.yelp.com/biz/sample-business

Stores reviews in reviews.db.

Visualize Data:
bash

python main.py visualize

Generates plots in the plots/ directory.

Conclusion
This implementation provides a complete, functional Customer Feedback Analyzer that:
Showcases MIS skills for your GitHub portfolio.

Ties to business optimization concepts like BPM and the Balanced Scorecard.

Includes placeholders for APIs to indicate scalability and ethical alternatives.

Is well-documented for employers to understand its value.

Adjust selectors in scraper.py as needed based on current platform HTML, and consider testing with sample HTML files to enhance professionalism.

