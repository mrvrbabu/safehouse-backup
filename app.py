# import os
# import psycopg2
# from dotenv import load_dotenv

import sqlalchemy
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rbabu:talktome@192.168.0.169:5432/safehousedb'


db = SQLAlchemy(app)

# load_dotenv()


# url = os.getenv("DATABASE_URL")
# connection = psycopg2.connect(url)

class Safehouse(db.Model):
    __tablename__ = 'safehouse'
    id = db.Column(db.Integer, primary_key=True)
    house_name = db.Column(db.String(50), unique=True, nullable=False)
    location = db.Column(db.String(40))
    # floors = db.Column(db.Integer)
    # cameras = db.Column(db.Integer)

    def __init__(self, house_number, house_name, location):
        self.id = house_number
        self.house_name = house_name
        self.location = location
        # self.floors = floors
        # self.cameras = cameras


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/submit', methods=['POST'])
# @app.route('/submit', methods=['POST'])

@app.route('/submit', methods=['POST'])
def submit():
    id = request.form['house_number']
    house_name = request.form['house_name']
    location = request.form['location']
#   pet=request.form['pets']

    safehouse = Safehouse(id, house_name, location)
    db.session.add(safehouse)
    db.session.commit()

    # # fetch a certain student2
    # studentResult = db.session.query(Student).filter(Student.id == 1)
    # for result in studentResult:
    #     print(result.fname)

    return render_template('success.html', data=house_name)


if __name__ == '__main__':  # python interpreter assigns "__main__" to the file you run
    app.run(debug=True)
