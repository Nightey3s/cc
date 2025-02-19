from datetime import datetime
import uuid
from botocore.exceptions import ClientError
from db_connection import bookings_table
from models.event import update_ticket_count

def generate_booking_id():
    return f"booking_{str(uuid.uuid4())}"

def create_booking(user_id, event_id, section, quantity, price_per_ticket, event_name, event_location):
    """Create a new booking."""
    try:
        # First, try to update the event tickets
        if not update_ticket_count(event_id, quantity, "sold"):
            return {"error": "Not enough tickets available"}

        # Create the booking
        booking_id = generate_booking_id()
        booking = {
            'booking_id': booking_id,
            'user_id': user_id,
            'event_id': event_id,
            'status': 'completed',
            'timestamp': datetime.now().isoformat(),
            'total_price': price_per_ticket * quantity,
            'seat_details': {
                'section': section,
                'tickets_booked': quantity,
                'price_per_ticket': price_per_ticket
            },
            'event_name': event_name,
            'event_location': event_location
        }
        
        bookings_table.put_item(Item=booking)
        return {"success": "Booking successful"}
            
    except ClientError as e:
        # If booking fails, try to rollback the ticket count
        update_ticket_count(event_id, quantity, "refund")
        print(f"Error creating booking: {str(e)}")
        return {"error": str(e)}

def get_user_bookings(user_id):
    """Get all bookings for a specific user."""
    try:
        response = bookings_table.query(
            IndexName='UserBookingsIndex',
            KeyConditionExpression='user_id = :uid',
            ExpressionAttributeValues={
                ':uid': user_id
            }
        )
        return response.get('Items', [])
    except ClientError as e:
        print(f"Error retrieving user bookings: {str(e)}")
        return []

def get_booking_by_id(booking_id):
    """Get a specific booking by ID."""
    try:
        response = bookings_table.get_item(
            Key={'booking_id': booking_id}
        )
        return response.get('Item')
    except ClientError as e:
        print(f"Error retrieving booking: {str(e)}")
        return None

def update_booking_status(booking_id, new_status):
    """Update the status of a booking."""
    try:
        bookings_table.update_item(
            Key={'booking_id': booking_id},
            UpdateExpression='SET #status = :status',
            ExpressionAttributeNames={
                '#status': 'status'  # status is a reserved word in DynamoDB
            },
            ExpressionAttributeValues={
                ':status': new_status
            }
        )
        return True
    except ClientError as e:
        print(f"Error updating booking status: {str(e)}")
        return False