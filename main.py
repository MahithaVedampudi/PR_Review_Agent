import os
from dotenv import load_dotenv
from pr_agent import get_pr_diff, parse_diff
from ai_module import generate_ai_feedback

def main():
    # Load environment variables
    load_dotenv()

    # Ask the user for their preferred input method
    source_choice = input("Enter 'live' to test a live PR or 'file' to use sample_pr_diff.md: ").lower()

    if source_choice == 'file':
        # Read the content directly from the local file
        try:
            with open('sample_pr_diff.md', 'r') as f:
                diff_content = f.read()
        except FileNotFoundError:
            print("Error: sample_pr_diff.md not found. Please create the file.")
            return
    elif source_choice == 'live':
        # Get live PR details from user
        repo_owner = input("Enter the repository owner: ")
        repo_name = input("Enter the repository name: ")
        pr_number = input("Enter the pull request number: ")
        
        print(f"\nFetching PR #{pr_number} from {repo_owner}/{repo_name}...")
        diff_content = get_pr_diff(repo_owner, repo_name, pr_number)
    else:
        print("Invalid choice. Please enter 'live' or 'file'.")
        return

    if not diff_content:
        print("Failed to get PR diff. Please check the details and try again.")
        return

    print("PR diff fetched successfully. Parsing code changes...")

    # The rest of your code remains the same
    code_changes = parse_diff(diff_content)
    
    if not code_changes:
        print("No new code found in the PR. Nothing to review.")
        return

    print("\nSending code changes to AI for review...")

    feedback = generate_ai_feedback(code_changes)
    
    print("\n--- AI Code Review ---")
    print(feedback)
    print("-----------------------")

if __name__ == "__main__":
    main()
