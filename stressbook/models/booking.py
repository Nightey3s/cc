from datetime import datetime
from db_connection import db

bookings_collection = db['bookings']
events_collection = db["events"]
seats_collection = db["seats"]

# Create indexes
def create_indexes():
    """Create indexes for the bookings collection"""
    # Index for querying bookings by user_id
    bookings_collection.create_index("user_id")
    
    # Compound index for querying by event_id and status
    bookings_collection.create_index([("event_id", 1), ("status", 1)])
    
    # Index for timestamp to optimize sorting by date
    bookings_collection.create_index("timestamp")

# Call create_indexes when initializing the application
create_indexes()

def create_booking(user_id, event_id, section, quantity, price_per_ticket, event_name, event_location):
    """Create a new booking without transactions."""
    try:
        # Check and update event tickets atomically
        event_update_result = events_collection.update_one(
            {"_id": event_id, "available_tickets": {"$gte": quantity}},  # Ensure enough tickets are available
            {
                "$inc": {
                    "available_tickets": -quantity,
                    "sold_tickets": quantity
                }
            }
        )

        if event_update_result.modified_count == 0:
            return {"error": "Not enough tickets available for the event."}

        # Check and update seat tickets atomically
        seat_update_result = seats_collection.update_one(
            {"_id": f"seat_section_{event_id}_{section}", "available_tickets": {"$gte": quantity}},
            {
                "$inc": {
                    "available_tickets": -quantity,
                    "sold_tickets": quantity
                }
            }
        )

        if seat_update_result.modified_count == 0:
            # Rollback event update if seat section fails
            events_collection.update_one(
                {"_id": event_id},
                {
                    "$inc": {
                        "available_tickets": quantity,
                        "sold_tickets": -quantity
                    }
                }
            )
            return {"error": "Not enough tickets available in the seat section."}

        # Insert booking document
        booking = {
            "_id": f"booking_{event_id}_{user_id}_{section}_{datetime.now().timestamp()}",
            "user_id": user_id,
            "event_id": event_id,
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "total_price": price_per_ticket * quantity,
            "seat_details": [{
                "section": section,
                "tickets_booked": quantity,
                "price_per_ticket": price_per_ticket
            }],
            "event_name": event_name,
            "event_location": event_location
        }
        bookings_collection.insert_one(booking)

        return {"success": "Booking successful"}
    except Exception as e:
        print(f"Booking error: {str(e)}")
        return {"error": str(e)}

def get_user_bookings(user_id):
    """Get all bookings for a specific user"""
    try:
        return list(bookings_collection.find({"user_id": user_id}))
    except Exception as e:
        print(f"Error fetching user bookings: {str(e)}")
        return []