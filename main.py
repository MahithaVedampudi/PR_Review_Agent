import os
from dotenv import load_dotenv
from pr_agent import get_pr_diff, parse_diff
from ai_module import generate_ai_feedback

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get user input for the PR to review
    repo_owner = input("Enter the repository owner (e.g., 'octocat'): ")
    repo_name = input("Enter the repository name (e.g., 'Spoon-Knife'): ")
    pr_number = input("Enter the pull request number: ")

    print(f"\nFetching PR #{pr_number} from {repo_owner}/{repo_name}...")

    # Fetch the PR diff
    diff_content = get_pr_diff(repo_owner, repo_name, pr_number)
    
    if not diff_content:
        print("Failed to get PR diff. Please check the details and try again.")
        return

    print("PR diff fetched successfully. Parsing code changes...")

    # Extract added code from the diff
    code_changes = parse_diff(diff_content)
    
    if not code_changes:
        print("No new code found in the PR. Nothing to review.")
        return

    print("\nSending code changes to AI for review...")

    # Get AI feedback on the code changes
    feedback = generate_ai_feedback(code_changes)
    
    print("\n--- AI Code Review ---")
    print(feedback)
    print("-----------------------")
    
if __name__ == "__main__":
    main()