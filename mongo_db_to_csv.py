from pymongo import MongoClient
import csv
from user import User  # Assuming you have defined the User class in a separate file named user.py

# Function to connect to MongoDB and retrieve user data
def get_user_data_from_mongodb():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['user_data']
    collection = db['users']
    
    # Query MongoDB to retrieve user data
    user_data = collection.find({}, {'_id': 0})  # Exclude _id field from results
    print("Retrieved user data from MongoDB successfully.")
    return user_data

# Function to process user data and write it to a CSV file
def write_user_data_to_csv(user_data, csv_file_path):
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["age", "gender", "total_income", "location", "marital_status", "occupation", "education_level", "utilities", "entertainment", "school_fees", "shopping", "healthcare"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write header row
        writer.writeheader()
        
        # Write data for each user
        for user_dict in user_data:
            user = User(**user_dict)  # Create User object from dictionary
            writer.writerow({
                "age": user.age,
                "gender": user.gender,
                "total_income": user.total_income,
                "location": user.location,
                "marital_status": user.marital_status,
                "occupation": user.occupation,
                "education_level": user.education_level,
                "utilities": user.utilities,
                "entertainment": user.entertainment,
                "school_fees": user.school_fees,
                "shopping": user.shopping,
                "healthcare": user.healthcare
            })

# Main function to execute the process
def main():
    user_data = get_user_data_from_mongodb()
    csv_file_path = "user_data.csv"
    write_user_data_to_csv(user_data, csv_file_path)
    print("Data written to CSV file successfully.")

if __name__ == "__main__":
    main()
