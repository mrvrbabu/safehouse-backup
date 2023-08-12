from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'Title': 'Data Analyst',
        'Location': 'Bengaluru, India',
        'Salary': 'Rs.1000000'
    },
    {
        'id': 2,
        'Title': 'DevOps Engineer',
        'Location': 'Gurgaon, India',
        'Salary': 'Rs.1000000'
    },
    {
        'id': 3,
        'Title': 'Software Architect',
        'Location': 'Delhi, India',
        'Salary': 'Rs.10000000'
    },
    {
        'id': 4,
        'Title': 'Backend Engineer',
        'Location': 'San Francisco, USA',
        'Salary': '$150000'
    }
]


@app.route('/')
def home():
    return render_template('index.html', jobs=JOBS, company_name="SafeHouse")


@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
