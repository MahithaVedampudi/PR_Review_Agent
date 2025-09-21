# PR_Review_Agent

AI-Powered PR Review Agent
An intelligent agent that automates the code review process by analyzing pull request changes and providing AI-driven feedback on code quality, potential bugs, and security vulnerabilities. This project was developed as part of the SRM Hackathon using CodeMate Build and the CodeMate Extension.

Features:
  Automated Code Review: Analyzes new code added in a pull request to provide constructive feedback.
  Bug and Security Detection: Uses a powerful AI model to identify common bugs, logical errors, and potential security vulnerabilities.
  Code Quality Assessment: Provides feedback on code style and readability, helping maintain a consistent codebase.

Flexible Inputs: Can be run on any public GitHub pull request or on a local diff file for quick, offline testing.
Modular Architecture: The project's structure is clean and modular, making it easy to extend for compatibility with other Git platforms (e.g., GitLab, Bitbucket).

Technologies Used
  Python: The core backend language.
  requests: For making API calls to GitHub.
  python-dotenv: For securely managing API keys.

mistralai : The AI client for connecting to the chosen Large Language Model.
Git & GitHub API: The foundation for fetching and analyzing pull requests.
CodeMate Build & Extension: Mandatory AI tools used throughout the development process for coding assistance and project management.

How to Run the Project
Step 1: Clone the Repository
Clone this repository to your local machine.

Bash
git clone https://github.com/MahithaVedampudi/PR_Review_Agent.git
cd PR_Review_Agent
Step 2: Set Up the Environment
Create a Python virtual environment and install the required dependencies.

Bash
# Create a virtual environment
py -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Step 3: Configure API Keys
Create a file named .env in the root directory and add your API keys. This file should not be pushed to GitHub.

GITHUB_TOKEN="your_personal_access_token_here"
MISTRAL_API_KEY="your_mistral_ai_api_key_here"
Step 4: Run the Agent
You can run the agent in two modes:

A. Live PR Review
This mode fetches a real pull request from GitHub. 
  Bash
  py main.py
  When prompted, enter live, and provide the repository owner, repository name, and the pull request number.

B. Local Diff File Review
This mode uses a local file for quick, offline testing.  
  Bash
  py main.py
  When prompted, enter file. The agent will read from sample_pr_diff.md and provide a review.

Submission Details
This project was created for the SRM Hackathon as a solution to Problem Statement 2 (PR Review Agent).

GitHub Repository: [Insert Your GitHub Repository Link Here]

Live Hosted URL: [Insert Your Live Hosted URL Here]

Working Video: [Insert Your Video Link Here]
