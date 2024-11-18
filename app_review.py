from google_play_scraper import reviews
from textblob import TextBlob
import pandas as pd

# Function to fetch app reviews
def get_app_reviews(app_id, num_reviews=100):
    result, _ = reviews(app_id, lang='en', country='us', count=num_reviews)
    return result

# Function to analyze sentiment
def analyze_sentiment(review_text):
    analysis = TextBlob(review_text)
    return "positive" if analysis.sentiment.polarity > 0 else "negative"

# Save reviews and sentiment to CSV
def save_reviews_to_csv(reviews_data, filename):
    processed_reviews = [
        {
            'content': review['content'],
            'score': review['score'],
            'sentiment': analyze_sentiment(review['content'])
        }
        for review in reviews_data
    ]
    df = pd.DataFrame(processed_reviews)
    df.to_csv(filename, index=False)
    print(f"Reviews saved to {filename}")

# Example usage
if __name__ == "__main__":
    APP_ID = "com.competitor.app"
    reviews_data = get_app_reviews(APP_ID, num_reviews=50)
    if reviews_data:
        save_reviews_to_csv(reviews_data, "competitor_app_reviews.csv")
