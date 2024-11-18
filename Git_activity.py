import requests
import json
from datetime import datetime

# Function to fetch GitHub activity
def get_github_activity(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/events"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

# Function to parse and save activity to a JSON file
def save_activity_to_file(activity, repo_name):
    with open(f"{repo_name}_github_activity.json", "w") as file:
        json.dump(activity, file, indent=4)
    print(f"Activity saved to {repo_name}_github_activity.json")

# Example usage
if __name__ == "__main__":
    GITHUB_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"
    COMPETITOR_OWNER = "competitor-org"
    REPO_NAME = "competitor-repo"

    activity = get_github_activity(COMPETITOR_OWNER, REPO_NAME, GITHUB_TOKEN)
    if activity:
        save_activity_to_file(activity, REPO_NAME)
