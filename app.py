import requests
import os

MY_GITHUB_TOKEN = os.getenv("MY_GITHUB_TOKEN")
MY_GITHUB_USERNAME = os.getenv("MY_GITHUB_USERNAME")

def fetch_github_profile():
    url = f"https://api.github.com/users/{MY_GITHUB_USERNAME}"
    headers = {
        "Authorization": f"token {MY_GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Success!")
        print(f"Name: {data.get('name')}")
        print(f"Repos: {data.get('public_repos')}")
        print(f"Followers: {data.get('followers')}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    fetch_github_profile()
