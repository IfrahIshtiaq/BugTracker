from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# List to store created bugs (simulating a database)
bugs = []

# Define route for bug creation form and bug display
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission and bug creation
        summary = request.form['summary']
        description = request.form['description']
        project_key = request.form['project_key']
        issue_type = request.form['issue_type']
        priority = request.form['priority']
        reporter = request.form['reporter']
        assignee = request.form['assignee']
        labels = request.form['labels']
        # Create a dictionary to represent the bug
        bug = {
            'id': len(bugs) + 1,
            'summary': summary,
            'description': description,
            'project_key': project_key,
            'issue_type': issue_type,
            'priority': priority,
            'reporter': reporter,
            'assignee': assignee,
            'labels': labels
        }
        bugs.append(bug)  # Add bug to the list
        return render_template('bug_form.html', bugs=bugs)
    return render_template('bug_form.html', bugs=bugs)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)