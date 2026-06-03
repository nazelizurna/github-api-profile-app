**README created:** 

### Clean README content (no emojis):

```markdown
# GitHub Profile Fetcher

Simple Python script to fetch basic public information from any GitHub user profile using the GitHub REST API.

## Description

This script retrieves a user's name, number of public repositories, and follower count. It uses a personal access token for authenticated requests (recommended to avoid rate limits).

## Requirements

- Python 3.6+
- requests library

## Setup

1. Install the dependency:
   ```bash
   pip install requests
   ```

2. Set the following environment variables:

   - `MY_GITHUB_TOKEN` — Your GitHub Personal Access Token (classic or fine-grained with `read:user` scope)
   - `MY_GITHUB_USERNAME` — The GitHub username you want to look up

## Usage

Run the script:

```bash
python github_profile.py
```

## Output Example

```
Success!
Name: The Octocat
Repos: 8
Followers: 12345
```

## Notes

- The token is only used for authentication and higher rate limits.
- Never commit your token to version control.
- For production use, consider the official `PyGithub` library.

## License

MIT
```

Would you like me to also create a `requirements.txt` or improve the script itself (better error handling, JSON output, etc.)?
