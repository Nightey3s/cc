from datetime import datetime
import uuid
from botocore.exceptions import ClientError
from db_connection import users_table

def generate_user_id():
    return f"user_{str(uuid.uuid4())}"

def create_user(name, email, password):
    """Create a new user in DynamoDB."""
    try:
        # Check if email exists using GSI
        response = users_table.query(
            IndexName='EmailIndex',
            KeyConditionExpression='email = :email',
            ExpressionAttributeValues={
                ':email': email
            }
        )
        
        if response['Items']:
            return {"status": "error", "message": "Email already exists"}

        user_id = generate_user_id()
        user = {
            'user_id': user_id,
            'name': name,
            'email': email,
            'password': password,  # In production, ensure this is hashed
            'created_at': datetime.now().isoformat()
        }
        
        users_table.put_item(Item=user)
        return {"status": "success", "user_id": user_id}
    except ClientError as e:
        print(f"Error creating user: {str(e)}")
        return {"status": "error", "message": str(e)}

def user_login(email, password):
    """Verify user login credentials."""
    try:
        response = users_table.query(
            IndexName='EmailIndex',
            KeyConditionExpression='email = :email',
            ExpressionAttributeValues={
                ':email': email
            }
        )
        
        if not response['Items']:
            return None
            
        user = response['Items'][0]
        if user['password'] == password:  # In production, use proper password verification
            return user
        return None
    except ClientError as e:
        print(f"Error during login: {str(e)}")
        return None

def update_user_profile(user_id, name, email):
    """Update user profile information."""
    try:
        users_table.update_item(
            Key={'user_id': user_id},
            UpdateExpression='SET #name = :name, email = :email',
            ExpressionAttributeNames={
                '#name': 'name'  # 'name' is a reserved word in DynamoDB
            },
            ExpressionAttributeValues={
                ':name': name,
                ':email': email
            }
        )
        return True
    except ClientError as e:
        print(f"Error updating user profile: {str(e)}")
        return False

def is_email_used(email):
    """Check if the email is already registered."""
    try:
        response = users_table.query(
            IndexName='EmailIndex',
            KeyConditionExpression='email = :email',
            ExpressionAttributeValues={
                ':email': email
            }
        )
        return len(response['Items']) > 0
    except ClientError as e:
        print(f"Error checking email: {str(e)}")
        return False