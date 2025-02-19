import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_dynamodb_resource():
    """Create and return a DynamoDB resource object"""
    return boto3.resource('dynamodb',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN'),  # Required for AWS Academy
        region_name=os.getenv('AWS_REGION', 'us-east-1')
    )

# Create DynamoDB resource
dynamodb = get_dynamodb_resource()

# Get table resources
users_table = dynamodb.Table('StressBook_Users')
events_table = dynamodb.Table('StressBook_Events')
seats_table = dynamodb.Table('StressBook_Seats')
bookings_table = dynamodb.Table('StressBook_Bookings')