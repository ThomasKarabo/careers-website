from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
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

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS, company_name="Data")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)