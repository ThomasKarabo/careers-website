from flask import Flask, render_template, jsonify, request
from database import add_application
import sqlite3

app = Flask(__name__)

'''JOBS = [
    {
        'id':1,
        'title': 'Junior Data Analyst',
        'experience': '1-2 years',
        'location': 'Johannesburg, Gauteng',
        'salary': 'R35,000.00'
    },
    {
        'id':2,
        'title': 'Senior Data Analyst',
        'experience': '3-5 years',
        'location': 'Cape Town, Western Cape',
        'salary': 'R55,000.00'
    },
    {
        'id':3,
        'title': 'Data Scientist',
        'experience': '5+ years',
        'location': 'Durban, KwaZulu-Natal',
        'salary': 'R75,000.00'
    },
    {
        'id':4,
        'title': 'Machine Learning Engineer',
        'experience': '3-5 years',
        'location': 'Pretoria, Gauteng',
        'salary': 'R85,000.00'
    },
    {
        'id':5,
        'title': 'Data Engineer',
        'experience': '2-4 years',
        'location': 'Port Elizabeth, Eastern Cape',
        'salary': 'R65,000.00',
    }
]
'''
def load_jobs_from_db():
    connection = sqlite3.connect('careers_db.db')
    cursor = connection.cursor()
    result = cursor.execute('''SELECT * FROM jobs''')
    columns = [desc[0] for desc in cursor.description]
    result_all = result.fetchall()
    # Convert rows to list of dictionaries
    result_dicts = [dict(zip(columns, row)) for row in result_all]
    return result_dicts



@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name="Data")

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<int:id>")
def job_detail(id):
    job = load_jobs_from_db()[id-1]
    try:
        return jsonify(job)
    except IndexError:
        return jsonify({"error": "Job not found"}), 404
    
@app.route("/jobpage/<int:id>")
def job_page(id):
    job = load_jobs_from_db()[id-1]
    try:
        return render_template("jobpage.html", job=job)
    except IndexError:
        return "Error: Job not found", 404
    
@app.route("/jobpage/<int:id>/apply", methods=['POST'])
def apply_job(id):
    data = request.form
    add_application(id, data)
    return render_template('submitted.html', application=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)