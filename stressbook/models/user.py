from datetime import datetime
from db_connection import users_collection 
from bson import ObjectId
from pymongo.errors import DuplicateKeyError

def create_user(name, email, password):
    """Create a new user in the database."""
    user = {
        "name": name,
        "email": email,
        "password": password,
        "created_at": datetime.now().isoformat(),
    }
    try:
        result = users_collection.insert_one(user)
        return {"status": "success", "user_id": str(result.inserted_id)}
    except DuplicateKeyError:
        return {"status": "error", "message": "Email already exists"} 
    
def user_login(email,password):
    user_data = users_collection.find_one({"email": email})
    if user_data and user_data['password'] == password:
        return user_data  # Return user data if login is successful
    
# models/user.py
def update_user_profile(user_id, name, email):
    """Update user profile information in the database."""
    users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {
            "name": name,
            "email": email,
        }}
    )

def is_email_used(email):
    """Check if the email is already registered in the database."""
    return users_collection.find_one({"email": email})