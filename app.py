from flask import Flask, render_template, request
from pr_agent import get_pr_diff, parse_diff
from ai_module import generate_ai_feedback

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        repo_owner = request.form['repo_owner']
        repo_name = request.form['repo_name']
        pr_number = request.form['pr_number']

        # Get the diff from the live PR
        diff_content = get_pr_diff(repo_owner, repo_name, pr_number)
        
        if not diff_content:
            return render_template('index.html', feedback="Failed to get PR diff. Please check the details and try again.")
        
        # Parse the code and get AI feedback
        code_changes = parse_diff(diff_content)
        
        if not code_changes:
            return render_template('index.html', feedback="No new code found in the PR. Nothing to review.")
        
        feedback = generate_ai_feedback(code_changes)
        
        # Display the AI feedback on the web page
        return render_template('index.html', feedback=feedback)

    # Render the initial page with the form
    return render_template('index.html', feedback="")

if __name__ == '__main__':
    app.run(debug=True)
