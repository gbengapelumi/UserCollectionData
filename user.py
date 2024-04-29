class User:
    def __init__(self, age, gender, total_income, location, marital_status, occupation, education_level, utilities, entertainment, school_fees, shopping, healthcare):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.location = location
        self.marital_status = marital_status
        self.occupation = occupation
        self.education_level = education_level
        self.utilities = utilities
        self.entertainment = entertainment
        self.school_fees = school_fees
        self.shopping = shopping
        self.healthcare = healthcare
    
    def __str__(self):
        return f"User(age={self.age}, gender={self.gender}, total_income={self.total_income}, location={self.location}, marital_status={self.marital_status}, occupation={self.occupation}, education_level={self.education_level}, utilities={self.utilities}, entertainment={self.entertainment}, school_fees={self.school_fees}, shopping={self.shopping}, healthcare={self.healthcare})"
