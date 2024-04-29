from flask import Flask, render_template, request
from pymongo import MongoClient

application = Flask(__name__)
app = application

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['user_data']  # Connect to the 'user_data' database
collection = db['users']  # Connect to the 'users' collection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    age = request.form['age']
    gender = request.form['gender']
    total_income = request.form['total_income']
    location = request.form['location']
    marital_status = request.form['marital_status']
    occupation = request.form['occupation']
    education_level = request.form['education_level']
    
    # Retrieve expenses data
    utilities = request.form.get('utilities')
    utilities_amount = request.form['utilities_amount'] if utilities else None
    
    entertainment = request.form.get('entertainment')
    entertainment_amount = request.form['entertainment_amount'] if entertainment else None
    
    school_fees = request.form.get('school_fees')
    school_fees_amount = request.form['school_fees_amount'] if school_fees else None
    
    shopping = request.form.get('shopping')
    shopping_amount = request.form['shopping_amount'] if shopping else None
    
    healthcare = request.form.get('healthcare')
    healthcare_amount = request.form['healthcare_amount'] if healthcare else None
    
    # Insert user data and expenses into MongoDB
    user_data = {
        'age': age,
        'gender': gender,
        'total_income': total_income,
        'location': location,
        'marital_status': marital_status,
        'occupation': occupation,
        'education_level': education_level,
        'utilities': utilities_amount,
        'entertainment': entertainment_amount,
        'school_fees': school_fees_amount,
        'shopping': shopping_amount,
        'healthcare': healthcare_amount
    }
    collection.insert_one(user_data)
    
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
