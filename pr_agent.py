import os
import requests
from github import Github

def get_pr_diff(repo_owner, repo_name, pr_number):
    """
    Fetches the raw diff of a pull request from GitHub.
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GitHub token not found. Check your .env file.")
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.diff"
    }
    
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PR diff: {e}")
        return None

def parse_diff(diff_content):
    """
    Parses a diff to extract added/modified code lines.
    This is a simplified approach for demonstration.
    """
    added_lines = []
    
    for line in diff_content.splitlines():
        if line.startswith('+') and not line.startswith('+++'):
            added_lines.append(line[1:].strip())
            
    return "\n".join(added_lines)
