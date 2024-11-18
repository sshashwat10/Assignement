### **README.md**

# Competitor Tracking System MVP

This project is a **Competitor Tracking System** that automates monitoring of competitor activity across multiple sources, including GitHub repositories, job postings, app reviews, and pricing changes. It aggregates the data and generates daily reports.

---

## **Features**
1. **GitHub Activity Tracking**:
   - Monitors public GitHub repositories for commits, issues, and pull requests.
2. **Job Postings Monitoring**:
   - Scrapes job boards like Indeed for competitor job postings.
3. **App Reviews Sentiment Analysis**:
   - Fetches app reviews and analyzes sentiment (positive/negative).
4. **Pricing Change Alerts**:
   - Tracks product pricing from competitor websites.
5. **Daily Reports**:
   - Summarizes all data and emails it to stakeholders.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/sshashwat10/Assignment.git
cd Assignment
```

### **2. Install Dependencies**
Install all Python dependencies using:
```bash
pip install -r requirements.txt
```

### **3. Configure API Keys**
- **GitHub API**:
  - Create a [GitHub Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) with `repo` scope.
  - Add it to the code where indicated (`GITHUB_TOKEN`).
- **Google Play Scraper**:
  - No API key needed.
- **SMTP Email**:
  - Use your email credentials for sending reports. Ensure the sender email has SMTP enabled (e.g., Gmail requires enabling "Allow less secure apps" or creating an App Password).

### **4. Update URLs and Competitor Data**
- Replace placeholders in the code (`COMPETITOR_OWNER`, `REPO_NAME`, `JOB_URL`, `APP_ID`, `PRODUCT_URL`) with actual competitor data.

### **5. Schedule Scripts**
Automate the scripts using:
- **Cron Jobs** (Linux/macOS) or **Task Scheduler** (Windows):
  - Example cron job to run the GitHub tracker daily:
    ```bash
    0 9 * * * /usr/bin/python3 /path/to/github_tracker.py
    ```

---



## **Project Structure**
```
competitor-tracking-system/
│
├── Github_activity.py         # Tracks GitHub activity
├── Competitor.py            # Scrapes job postings
├── app_review.py    # Fetches and analyzes app reviews
├── Price_changes.py        # Tracks pricing changes
├── reports.py            # Sends daily summary reports via email
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── data/                     # Folder for storing output files (JSON, CSV)
```

---

## **Requirements**
- Python 3.8+
- Libraries listed in `requirements.txt`

---

## **Dependencies**

- `requests`: HTTP requests to APIs and websites.
- `beautifulsoup4`: Web scraping for job postings and pricing data.
- `google-play-scraper`: Fetching app reviews from the Google Play Store.
- `textblob`: Sentiment analysis for app reviews.
- `pandas`: Data manipulation and CSV creation.
- `smtplib`: Sending email reports.
---

## **Contributing**
Contributions are welcome! Feel free to submit issues or pull requests.

---

## **License**
MIT License
```




