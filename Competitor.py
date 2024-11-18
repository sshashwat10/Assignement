import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape job postings
def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = []
    for job in soup.find_all('div', class_='job_seen_beacon'):
        title = job.find('h2', class_='jobTitle').text if job.find('h2', class_='jobTitle') else "N/A"
        company = job.find('span', class_='companyName').text if job.find('span', class_='companyName') else "N/A"
        location = job.find('div', class_='companyLocation').text if job.find('div', class_='companyLocation') else "N/A"
        job_listings.append({'title': title, 'company': company, 'location': location})

    return job_listings

# Function to save jobs to CSV
def save_jobs_to_csv(jobs, filename):
    df = pd.DataFrame(jobs)
    df.to_csv(filename, index=False)
    print(f"Jobs saved to {filename}")

# Example usage
if __name__ == "__main__":
    JOB_URL = "https://www.indeed.com/jobs?q=competitor"
    jobs = scrape_jobs(JOB_URL)
    if jobs:
        save_jobs_to_csv(jobs, "competitor_jobs.csv")
