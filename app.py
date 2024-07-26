from flask import Flask, render_template, request , jsonify
from pymongo import MongoClient


app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/chat')
def chatbot():
    return render_template('chatbot.html')

@app.route('/student-portal')
def student_portal():
    return render_template('student_portal.html')

client = MongoClient("mongodb+srv://aqadry:1234@cluster.xxaj6ri.mongodb.net/")
db = client["Student_Future"]
student_collection = db["student"]

@app.route('/submit-form', methods=['POST'])
def submit_form():

    full_name = request.form['full-name']
    date_of_birth = request.form['date-of-birth']
    email = request.form['email']
    mobile_number = request.form['mobile-number']
    gender = request.form['gender']
    city = request.form['city']
    student_id = request.form['student-id']
    school_name = request.form['school-name']
    education_level = request.form['education-level']
    grade_level = request.form['grade-level']
    stream = request.form['stream']
    specialty = request.form['specialty']

    student_data = {
        'full_name': full_name,
        'date_of_birth': date_of_birth,
        'email': email,
        'mobile_number': mobile_number,
        'gender': gender,
        'city': city,
        'student_id': student_id,
        'school_name': school_name,
        'education_level': education_level,
        'grade_level': grade_level,
        'stream': stream,
        'specialty': specialty
    }

    student_collection.insert_one(student_data)

    return render_template('login.html')

@app.route('/login')
def login_pgae() : 
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)