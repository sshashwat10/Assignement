import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape product prices
def scrape_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', {'class': 'price'}).text.strip() if soup.find('span', {'class': 'price'}) else "N/A"
    return price

# Save price data
def save_price_data(product_name, price, filename):
    data = {'product': [product_name], 'price': [price]}
    df = pd.DataFrame(data)
    df.to_csv(filename, mode='a', header=False, index=False)
    print(f"Price data saved to {filename}")

# Example usage
if __name__ == "__main__":
    PRODUCT_URL = "https://www.competitor.com/product"
    PRODUCT_NAME = "Competitor Product"
    price = scrape_price(PRODUCT_URL)
    if price:
        save_price_data(PRODUCT_NAME, price, "competitor_pricing.csv")
