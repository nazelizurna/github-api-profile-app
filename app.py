import os
import requests

GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")
USERNAME = os.getenv("MY_GITHUB_USERNAME")


def fetch_github_profile():
    if not GITHUB_TOKEN or not USERNAME:
        print("❌ CRITICAL ERROR: Environment variables are missing!")
        print("Please configure 'MY_GITHUB_TOKEN' and 'MY_GITHUB_USERNAME'.")
        return

    url = f"https://github.com{USERNAME}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    print(f"Connecting securely to GitHub API...\n")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("🎉 SECURE INTEGRATION SUCCESSFUL!")
        print("-" * 40)
        print(f"👤 Account Name: {data.get('name', 'N/A')}")
        print(f"📂 Public Repos: {data.get('public_repos')}")
        print(f"👥 Followers:    {data.get('followers')}")
        print("-" * 40)
    else:
        print(f"❌ Connection Failed. Status Code: {response.status_code}")


if __name__ == "__main__":
    fetch_github_profile()
