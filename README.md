# **AI-Powered PR Review Agent**

An intelligent agent that automates the code review process by analyzing pull request changes and providing AI-driven feedback on code quality, potential bugs, and security vulnerabilities. This project was developed as part of the **SRM Hackathon** using **CodeMate Build** and the **CodeMate Extension**.

## **Features**

  * **Live Web Interface:** Provides a simple, user-friendly web form to get an instant AI review for any GitHub pull request.
  * **Automated Code Review:** Analyzes new code added in a pull request to provide constructive feedback.
  * **Bug and Security Detection:** Uses a powerful AI model to identify common bugs, logical errors, and potential security vulnerabilities.
  * **Code Quality Assessment:** Provides feedback on code style and readability, helping maintain a consistent codebase.
  * **Modular Architecture:** The project's structure is clean and modular, making it easy to extend for compatibility with other Git platforms (e.g., GitLab, Bitbucket).

## **Technologies Used**

  * **Python:** The core backend language.
  * **Flask:** The web framework used to create the live-hosted application.
  * **`requests`:** For making API calls to GitHub.
  * **`python-dotenv`:** For securely managing API keys.
  * **`mistralai`**: The AI client for connecting to the chosen Large Language Model.
  * **Git & GitHub API:** The foundation for fetching and analyzing pull requests.
  * **CodeMate Build & Extension:** Mandatory AI tools used throughout the development process for coding assistance and project management.

## **How to Run the Project**

### **Step 1: Clone the Repository**

Clone this repository to your local machine.

```bash
git clone https://github.com/MahithaVedampudi/PR_Review_Agent.git
cd PR_Review_Agent
```

### **Step 2: Set Up the Environment**

Create a Python virtual environment and install the required dependencies.

```bash
# Create a virtual environment
py -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### **Step 3: Configure API Keys**

Create a file named `.env` in the root directory and add your API keys. **This file should not be pushed to GitHub.**

```
GITHUB_TOKEN="your_personal_access_token_here"
MISTRAL_API_KEY="your_mistral_ai_api_key_here"
```

### **Step 4: Run the Web Server**

To run the web application locally, execute the `app.py` file.

```bash
py app.py
```

This will start a local server. You can access your project by navigating to `http://127.0.0.1:5000` in your web browser.

## **Live Deployment**

To make this project accessible via a live URL, the command-line interface was wrapped in a simple web framework. The hosted application provides a web form where users can submit a GitHub URL and PR number to get an instant AI-powered review.
<img width="1064" height="514" alt="image" src="https://github.com/user-attachments/assets/1686adab-53d8-4573-a97c-083ceb170e2d" />


## **Submission Details**

This project was created for the SRM Hackathon as a solution to Problem Statement 2 (PR Review Agent).

  * **GitHub Repository:** `[https://github.com/MahithaVedampudi/PR_Review_Agent]`
  * **Live Hosted URL:** `[http://127.0.0.1:5000]`
  * **Working Video:** `[Insert Your Video Link Here]`
