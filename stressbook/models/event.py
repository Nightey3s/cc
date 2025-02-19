from datetime import datetime
import uuid
from botocore.exceptions import ClientError
from db_connection import events_table

def generate_event_id():
    return f"event_{str(uuid.uuid4())}"

def create_events_onload():
    """Initialize sample events if none exist."""
    try:
        # Check if events already exist
        response = events_table.scan(Limit=1)
        if response['Items']:
            print("Events already initialized.")
            return

        # Sample events data
        sample_events = [{
            'event_id': 'event_id_001',
            'type': 'Concert',
            'name': 'Honkai Impact Music Fest 2024',
            'date': '15/12/2024 19:00:00',
            'location': 'Singapore Indoor Stadium',
            'available_tickets': 12000,
            'reserved_tickets': 0,
            'sold_tickets': 0,
            'image_url': 'static/images/concert_one.jpeg',
            'duration': '2 hours',
            'age_advisory': 'PG-13',
            'description': 'Experience the magical world of Honkai Impact through an orchestral performance.',
            'artist': 'HOYO-MiX Symphony Orchestra',
            'organizer': 'HoYoverse Entertainment',
            'highlights': [
                'Live orchestral performance',
                'HD screen projections',
                'Exclusive merchandise',
                'Meet & greet opportunities'
            ]
        },
        # Add other sample events here...
        ]

        # Insert events one by one
        for event in sample_events:
            events_table.put_item(Item=event)
        print("Sample events inserted successfully.")

    except ClientError as e:
        print(f"Error initializing events: {str(e)}")

def retrieve_events():
    """Get all events from the database."""
    try:
        response = events_table.scan()
        return response.get('Items', [])
    except ClientError as e:
        print(f"Error retrieving events: {str(e)}")
        return []

def get_event_by_id(event_id):
    """Get a specific event by ID."""
    try:
        response = events_table.get_item(
            Key={'event_id': event_id}
        )
        return response.get('Item')
    except ClientError as e:
        print(f"Error retrieving event: {str(e)}")
        return None

def update_ticket_count(event_id, quantity, action="sold"):
    """Update ticket counts atomically."""
    try:
        if action == "sold":
            response = events_table.update_item(
                Key={'event_id': event_id},
                UpdateExpression='SET available_tickets = available_tickets - :qty, '
                               'sold_tickets = sold_tickets + :qty',
                ConditionExpression='available_tickets >= :qty',
                ExpressionAttributeValues={':qty': quantity},
                ReturnValues='UPDATED_NEW'
            )
        elif action == "refund":
            response = events_table.update_item(
                Key={'event_id': event_id},
                UpdateExpression='SET available_tickets = available_tickets + :qty, '
                               'sold_tickets = sold_tickets - :qty',
                ExpressionAttributeValues={':qty': quantity},
                ReturnValues='UPDATED_NEW'
            )
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            # Not enough tickets available
            return False
        print(f"Error updating ticket count: {str(e)}")
        return False

def check_ticket_availability(event_id, quantity):
    """Check if enough tickets are available."""
    try:
        response = events_table.get_item(
            Key={'event_id': event_id}
        )
        event = response.get('Item')
        if not event:
            return False
        return event.get('available_tickets', 0) >= quantity
    except ClientError as e:
        print(f"Error checking ticket availability: {str(e)}")
        return False

def reset_events():
    """Reset events to initial state."""
    try:
        # Delete all existing events
        existing_events = retrieve_events()
        for event in existing_events:
            events_table.delete_item(
                Key={'event_id': event['event_id']}
            )
        
        # Create new events
        create_events_onload()
        
        # Verify the reset
        all_events = retrieve_events()
        print(f"Database reset with {len(all_events)} events")
        
        # Print all events to verify
        for event in all_events:
            print(f"Event in DB: {event['event_id']}")
            
    except ClientError as e:
        print(f"Error resetting events: {str(e)}")